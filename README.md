#  CPE Data Collection and API
This project is to collect and parse XML data, save it in database, create API using Flask and then show that data on web using React frontend.


## Project's Objective?

The goal of this assignment was to:

* Parse **NVD CPE dictionary XML** feed (version 2.3)
* Convert it into structured format
* Store it inside a relational database
* Build a **REST API** to fetch data with pagination and filters
* Show the data in a clean and responsive **React UI**


## My Logical Approach

1. **XML Parsing**:

   * Used `lxml` to parse large XML file
   * Managed namespace correctly
   * Extracted `cpe_title`, `cpe_22_uri`, `cpe_23_uri`, `reference_links`, and `deprecation_date`
   * First saved as JSON to check output

2. **Database Setup**:

   * Used **SQLite** for fast setup
   * Designed schema with right data types like `TEXT`, `DATE`, and `JSON`
   * Inserted data using Python script

3. **REST API**:

   * Created with **Flask**
   * Main Endpoints:

     * `/api/cpes` → for pagination
     * `/api/cpes/search` → for searching/filtering
   * Supported search by title, uri, and date

4. **Frontend UI**:

   * Made using **React.js**
   * Used Axios to call APIs
   * Features include:

     * Pagination (15–50 per page)
     * Column filters
     * Truncated long reference links with tooltip or “+X more”
     * Date format changed to `MM DD YYYY`
     * Show message when no data is found




## How to Run or replicate

### 🔧 Backend (Flask + SQLite)

```bash
# 1. Setup virtual environment
python -m venv venv

# If you see an error about scripts being disabled (ExecutionPolicy), run this first:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# Then activate the virtual environment:
./venv/Scripts/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Parse XML to create database
cd backend
# Parse XML
python parse_cpe.py # This creates 'cpes.db' which contains the required data

# 4. Start API server
python app.py
```

### Frontend (React)
### In a new terminal window:
```bash
cd frontend
npm install
npm start

# This will launch the frontend React app (usually at http://localhost:3000) and connect to the backend API (on http://localhost:5000).
```

---

## Screenshots

### API Output

* `/api/cpes?page=1&limit=15`
* `/api/cpes/search?cpe_title=windows`

### React UI

* Paginated table (15–50 entries per page)
* Filters on title, uri, and deprecation date
* “+X more” links with popover
* Fallback screen when no results

> Please check the `screenshots/` folder in this repo for all sample images.

---

## Project Structure

```
├── backend/
│   ├── app.py              # Flask API server
│   ├── database.py         # DB setup and connection
│   ├── models.py           
│   └── parse_cpe.py        # CPE data parser
│
├── frontend/
│   ├── public/
│   │   └── index.html      # HTML entry point
│   └── src/
│       ├── App.js
│       ├── CpeTable.jsx
│       ├── ReferenceLinks.jsx
│       ├── api.js
│       └── index.js
│
├── Screenshots/            # Sample output images
│   ├── CPE_Data_Viewer.png
│   └── ...
│
├── .gitignore
├── .gitattributes
├── README.md
├── requirements.txt        # Python dependencies
└── package.json            # Frontend dependencies
```
---

## About Me

**Sai Praneeth Koti**
Master’s in Cybersecurity, University of Maryland
https://linkedin.com/in/praneeth-koti | https://github.com/praneethkoti
