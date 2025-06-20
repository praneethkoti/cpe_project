import xml.etree.ElementTree as ET
from database import SessionLocal, engine
from models import CPE, Base
import json
import gzip
from datetime import datetime

Base.metadata.create_all(bind=engine)

def parse_and_store(xml_path):
    session = SessionLocal()

    # Handle .gz compressed file input
    if xml_path.endswith('.gz'):
        with gzip.open(xml_path, 'rb') as f:
            tree = ET.parse(f)
    else:
        tree = ET.parse(xml_path)

    root = tree.getroot()

    ns = {
        'cpe': 'http://cpe.mitre.org/dictionary/2.0',
        'cpe-23': 'http://scap.nist.gov/schema/cpe-extension/2.3'
    }

    for item in root.findall('{http://cpe.mitre.org/dictionary/2.0}cpe-item'):
        cpe_22 = item.get('name')

        title_elem = item.find('{http://cpe.mitre.org/dictionary/2.0}title')
        title = title_elem.text if title_elem is not None else 'Unknown Title'

        refs_parent = item.find('{http://cpe.mitre.org/dictionary/2.0}references')
        links = []
        if refs_parent is not None:
            for ref in refs_parent.findall('{http://cpe.mitre.org/dictionary/2.0}reference'):
                href = ref.get('href')
                if href:
                    links.append(href)

        cpe23_elem = item.find('{http://scap.nist.gov/schema/cpe-extension/2.3}cpe23-item')
        cpe_23 = cpe23_elem.get('name') if cpe23_elem is not None else None

        dep_elem = item.find('{http://cpe.mitre.org/dictionary/2.0}deprecation')
        dep_date_22 = None
        if dep_elem is not None:
            raw_date = dep_elem.get('date')
            if raw_date:
                try:
                    dep_date_22 = datetime.strptime(raw_date, "%Y-%m-%d").date()
                except:
                    pass 

        cpe_entry = CPE(
            cpe_title=title,
            cpe_22_uri=cpe_22,
            cpe_23_uri=cpe_23,
            reference_links=json.dumps(links),
            cpe_22_deprecation_date=dep_date_22,
            cpe_23_deprecation_date=None
        )
        session.add(cpe_entry)

    session.commit()
    session.close()

parse_and_store("official-cpe-dictionary_v2.3.xml.gz")
