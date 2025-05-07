# NYC 311 Big Data Project

This project was created as part of my Big Data course to demonstrate a full data pipeline using Python, MongoDB Atlas, Tableau, and Matplotlib.

## Project Overview

- Ingested raw NYC 311 Service Request data using the NYC 311 API
- Stored raw data into MongoDB Atlas (`raw_data` collection)
- Cleaned and processed data in Python (`clean_data` collection)
- Aggregated and analyzed data to create insights
- Visualized results in Tableau and Matplotlib

---

## 🛠 Tools Used

- Python (Jupyter Notebooks, Pandas, Matplotlib)
- MongoDB Atlas (Big Data Application)
- Tableau Public (Visualization)

---

## Project Files

- `bronze1.ipynb` / `bronze1.py` → Raw data ingestion (Bronze layer)
- `silver1.ipynb` / `silver1.py` → Data cleaning (Silver layer)
- `gold1.ipynb` / `gold1.py` → Data aggregation + CSV export (Gold layer)
- `gold_aggregated_data.csv` → Aggregated dataset for visualization
- `Book1.twb` → Tableau workbook with 2 charts
- `README.md` → This project description

---

## Highlights

- Pulled **100,000+ records** using the NYC 311 API
- Stored raw and cleaned data into MongoDB Atlas
- Aggregated complaints by **borough** and **complaint type**
- Visualized:
  - Bar chart of complaints per borough (Tableau)
  - Top 10 complaint types (Tableau)
  - Complaints per hour (Matplotlib)

---

## How to Run

1. Install required Python packages:
