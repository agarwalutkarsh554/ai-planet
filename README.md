# Data Engineer Assignment: Scalable ETL Pipeline

## Objective
The goal of this assignment is to design and implement a scalable ETL pipeline and work with databases.

## Prerequisites
- PostgreSQL database set up on your local machine or a cloud instance.
- Python environment with necessary libraries installed (Pandas, SQLAlchemy, Metaflow, etc.).
- GitHub account for code repository.

## Assignment Overview
This project involves designing and implementing a scalable ETL pipeline using the publicly available Airbnb New York City dataset from Kaggle. The pipeline will include data ingestion, transformation, and loading into a PostgreSQL database. Additionally, Python will be used for data processing and Metaflow to manage the ETL workflow.

## Tasks

### Step 1: Data Ingestion and Storage

1. **Dataset Selection:**
   - Use the [Airbnb New York City dataset](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data) from Kaggle.

2. **Database Setup:**
   - Set up a PostgreSQL database.

3. **Data Loading:**
   - Write a script to load the dataset into a PostgreSQL table.
   - Ensure the table schema is designed to handle the dataset efficiently.

### Step 2: ETL Process

1. **Data Extraction:**
   - Extract the data from the PostgreSQL database using SQLAlchemy or a similar library.

2. **Data Transformation:**
   - Normalize the data (e.g., separate the date and time into different columns).
   - Calculate additional metrics (e.g., average price per neighborhood).
   - Handle missing values appropriately (e.g., fill, remove, or flag them).

3. **Data Loading:**
   - Load the transformed data into a new table in the PostgreSQL database.

### Step 3: Workflow Management with Metaflow

1. **Workflow Implementation:**
   - Use Metaflow to manage the ETL workflow.
   - Implement steps in Metaflow to handle the ETL process from data ingestion to loading the transformed data into the PostgreSQL database.
   - Ensure the workflow is reproducible and can handle failures gracefully.

## Deliverables

1. **GitHub Repository:**
   - All code related to the assignment.
   - Well-organized repository with a clear directory structure.
   - README file with instructions on how to set up and run the project.

2. **Documentation:**
   - Detailed explanation of the ETL process and data transformations.
   - Instructions for running the Metaflow workflow.

3. **Demonstration:**
   - Short video or series of screenshots demonstrating the working ETL pipeline.

## Submission Guidelines
- **GitHub Repository Link:** Submit the link to your GitHub repository.
- **Additional Documentation:** Include any additional documentation or demonstration videos/screenshots in the GitHub repository or provide separate links if needed.

## Evaluation Criteria

1. **Code Quality and Organization:**
   - Clean, readable, and well-documented code.
   - Proper use of version control with meaningful commit messages.

2. **Functionality:**
   - Correct implementation of the ETL pipeline and data processing tasks.

3. **Scalability and Performance:**
   - Design and implementation of scalable solutions.
   - Performance optimization for database queries and data processing tasks.

4. **Documentation and Demonstration:**
   - Clear and comprehensive documentation.
   - Effective demonstration of the implemented tasks.

## References/Resources
- [Metaflow Docs](https://docs.metaflow.org/)
- [New York City Airbnb Open Data | Kaggle](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data)
- [Metaflow GitHub Example](https://github.com/ashishtele/MetaFlow_MLOps)

---

## Instructions for Setting Up and Running the Project

### Clone the Repository:
```bash
git clone <your-repository-link>
cd <your-repository-directory>
