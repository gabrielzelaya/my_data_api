Data Analytics API
This project is a FastAPI-based web API designed for data analytics. It allows users to perform basic data operations like calculating the mean, sum, and statistical descriptions of specific columns in a CSV file.

Features
Calculate Mean: Compute the average value of a specified column.
Calculate Sum: Compute the total sum of a specified column.
Describe Column: Get a statistical summary of a specified column, including count, mean, std, min, 25%, 50%, 75%, and max.
Data
The API uses a sample data file named sample_data.csv with the following columns:

organizationIdentifier
orgType
location.locationIdentifier
name
division
sourceLink
Endpoints
GET /: Root endpoint to verify the API is running.
POST /mean: Calculate the mean of a specified column.
POST /sum: Calculate the sum of a specified column.
POST /describe: Get a statistical summary of a specified column.
Setup
Clone the repository:

bash

git clone https://github.com/yourusername/data-analytics-api.git
cd data-analytics-api
Create and activate a virtual environment:

bash

python -m venv env
source env/bin/activate  # On Windows use `.\env\Scripts\Activate.ps1`
Install the dependencies:

bash

pip install -r requirements.txt
Run the API:

bash

uvicorn main:app --reload
Access the API documentation at http://127.0.0.1:8000/docs.

Requirements
Python 3.8+
FastAPI
Uvicorn
Pandas
NumPy
Pydantic