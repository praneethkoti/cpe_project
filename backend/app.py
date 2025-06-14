from flask import Flask, request, jsonify
from flask_cors import CORS
from models import CPE
from database import SessionLocal
from sqlalchemy import or_

app = Flask(__name__)
CORS(app)

@app.route("/cpes", methods=["GET"])
def get_cpes():
    session = SessionLocal()
    try:
        page = int(request.args.get("page", 1))
        limit = int(request.args.get("limit", 15))
        cpes = session.query(CPE).offset((page - 1) * limit).limit(limit).all()
        total = session.query(CPE).count()

        return jsonify({
            "data": [cpe.to_dict() for cpe in cpes],
            "page": page,
            "limit": limit,
            "total": total
        })
    finally:
        session.close()

@app.route("/cpes/search", methods=["GET"])
def search_cpes():
    session = SessionLocal()
    try:
        page = int(request.args.get("page", 1))
        limit = int(request.args.get("limit", 15))

        title = request.args.get("cpe_title", "")
        uri = request.args.get("cpe_uri", "")
        deprecation_date = request.args.get("deprecation_date", "")

        query = session.query(CPE)

        if title:
            query = query.filter(CPE.cpe_title.ilike(f"%{title}%"))
        if uri:
            query = query.filter(or_(CPE.cpe_22_uri.ilike(f"%{uri}%"), CPE.cpe_23_uri.ilike(f"%{uri}%")))
        if deprecation_date:
            query = query.filter(or_(
                CPE.cpe_22_deprecation_date == deprecation_date,
                CPE.cpe_23_deprecation_date == deprecation_date
            ))

        total = query.count()
        cpes = query.offset((page - 1) * limit).limit(limit).all()

        return jsonify({
            "data": [cpe.to_dict() for cpe in cpes],
            "page": page,
            "limit": limit,
            "total": total
        })
    finally:
        session.close()

if __name__ == "__main__":
    app.run(debug=True)
