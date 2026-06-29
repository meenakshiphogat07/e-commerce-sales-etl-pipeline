# E-Commerce Sales ETL Pipeline

## Overview

This project is an end-to-end ETL (Extract, Transform, Load) pipeline built using Python and PostgreSQL. It extracts data from the Brazilian Olist E-Commerce dataset, performs data cleaning and transformation using Pandas, and loads the processed data into PostgreSQL.

The project demonstrates the fundamentals of data engineering, including data ingestion, preprocessing, and database loading.

---

## Project Architecture

```text
           Olist CSV Files
                  │
                  ▼
         Extract (Python)
                  │
                  ▼
      Transform (Pandas)
                  │
                  ▼
      Load (PostgreSQL)
```

---

## Technologies Used

* Python
* Pandas
* PostgreSQL
* SQLAlchemy
* Psycopg2
* Git
* GitHub

---

## Features

* Extract data from CSV files
* Clean and transform data
* Handle missing values
* Remove duplicate records
* Convert appropriate data types
* Create PostgreSQL tables
* Load cleaned data into PostgreSQL
* Modular ETL pipeline structure

---

## Dataset

The project uses the **Olist Brazilian E-Commerce Dataset**.

Current datasets processed:

* Customers
* Orders
* Order Items
* Payments
* Products
* Sellers
* Reviews
* Geolocation
* Product Category Translation

---

## Project Structure

```text
e-commerce-sales-etl-pipeline/
│
├── data/
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── database.py
│   └── utils.py
│
├── screenshots/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Future Improvements

* Apache Spark integration
* Apache Kafka integration
* Apache Airflow workflow orchestration
* Data quality validation
* Automated testing
* SQL analytics and reporting
* Power BI dashboard
