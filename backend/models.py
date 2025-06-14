from sqlalchemy import Column, Integer, String, Date
from database import Base

class CPE(Base):
    __tablename__ = "cpes"

    id = Column(Integer, primary_key=True)
    cpe_title = Column(String)
    cpe_22_uri = Column(String)
    cpe_23_uri = Column(String)
    cpe_22_deprecation_date = Column(String)
    cpe_23_deprecation_date = Column(String)
    reference_links = Column(String)

    def to_dict(self):
        import json
        return {
            "id": self.id,
            "cpe_title": self.cpe_title,
            "cpe_22_uri": self.cpe_22_uri,
            "cpe_23_uri": self.cpe_23_uri,
            "cpe_22_deprecation_date": self.cpe_22_deprecation_date,
            "cpe_23_deprecation_date": self.cpe_23_deprecation_date,
            "reference_links": json.loads(self.reference_links or "[]")
        }
