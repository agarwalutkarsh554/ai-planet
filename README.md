# Data Engineer Assignment: Scalable ETL Pipeline

## Objective
The goal of this assignment is to design and implement a scalable ETL pipeline and work with databases.

## Prerequisites
- PostgreSQL database set up on your local machine or a cloud instance.
- Python environment with necessary libraries installed (Pandas, SQLAlchemy, Metaflow, etc.).
- GitHub account for code repository.

## Assignment Overview
This project involves designing and implementing a scalable ETL pipeline using the publicly available Airbnb New York City dataset from Kaggle. The pipeline will include data ingestion, transformation, and loading into a PostgreSQL database. Additionally, Python will be used for data processing and Metaflow to manage the ETL workflow.

## References/Resources
- [Metaflow Docs](https://docs.metaflow.org/)
- [New York City Airbnb Open Data | Kaggle](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data)
- [Metaflow GitHub Example](https://github.com/ashishtele/MetaFlow_MLOps)

---

## Instructions for Setting Up and Running the Project

### Clone the Repository:
```bash
git clone https://github.com/agarwalutkarsh554/ai-planet.git
```
### Set Up the Python Environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### Install the required libraries:
```python
pip install -r requirements.txt
```
### Set Up PostgreSQL Database:
- Ensure PostgreSQL is running on your local machine or cloud instance.
- Create a database and update the connection details in the configuration file.
### Run the ETL Pipeline with Metaflow:
Execute the Metaflow script to process the data:
``` python
python metaflow_workflow.py
