#  CPE Data Collection and API
This project is to collect and parse XML data, save it in database, create API using Flask and then show that data on web using React frontend.

> ✅ **GitHub Repository:** [https://github.com/praneethkoti/cpe\_project](https://github.com/praneethkoti/cpe_project)


## What is our Objective?

The goal of this assignment was to:

* Parse **NVD CPE dictionary XML** feed (version 2.3)
* Convert it into structured format
* Store it inside a relational database
* Build a **REST API** to fetch data with pagination and filters
* Show the data in a clean and responsive **React UI**


## 🧠 Logical Approach

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
# Setup virtual environment
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

# Step 1: Parse XML
python cpe_parser.py

# Step 2: Create DB
python db_setup.py

# Step 3: Insert data into DB
python data_insert.py

# Step 4: Start API server
python api_server.py
```

### 🌐 Frontend (React)

```bash
cd cpe-frontend
npm install
npm start
```

---

## 📸 Screenshots

### ✅ API Output

* `/api/cpes?page=1&limit=10`
* `/api/cpes/search?cpe_title=windows&deprecation_date=2024-01-01`

### ✅ React UI

* Paginated table (15–50 entries per page)
* Filters on title, uri, and deprecation date
* “+X more” links with popover
* Fallback screen when no results

> 📁 Please check the `screenshots/` folder in this repo for all sample images.

---

## Evaluation Criteria Mapping

| Criteria            | How It Is Completed                                               |
| ------------------- | ----------------------------------------------------------------- |
| **Correctness**     | Data is parsed, stored, and queried correctly                     |
| **Code Quality**    | Code is modular and comments are added for understanding          |
| **Database Design** | Clean schema using proper types and JSON fields                   |
| **API Design**      | Flask RESTful API with filters and pagination                     |
| **Frontend UI**     | React app with filters, clean UI, and fallback when no data found |

---

## Project Structure

```
.
├── cpe_parser.py          # For parsing XML
├── db_setup.py            # Creates tables
├── data_insert.py         # Puts JSON into DB
├── api_server.py          # Flask server
├── cpe_data.db            # Database file
├── parsed_cpe_data.json   # Parsed JSON
├── cpe-frontend/          # React App
├── screenshots/           # Screenshot folder
└── README.md              # Project Report
```

---

## About Me

**Sai Praneeth Koti**
Master’s in Cybersecurity, University of Maryland
https://linkedin.com/in/praneeth-koti | https://github.com/praneethkoti
