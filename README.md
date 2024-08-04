# VE3_ASSIGNMENT
Create a Django-based web application that allows users to upload CSV files, performs data analysis using pandas and numpy, and displays the results and visualizations on the web interface.

## Setup Instructions

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd VE3_Assignment
    cd csv_analysis_project
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Start the development server:
    ```sh
    python manage.py runserver
    ```

6. Open a web browser and navigate to `http://127.0.0.1:8000/` to upload a CSV file and view the analysis
results.

## Project Explanation

This Django project offers functionality for users to upload, analyze, and visualize CSV files with the following features:

CSV File Upload: Users can upload their CSV files via a dedicated form.

Data Analysis: The project processes the uploaded CSV file to compute summary statistics such as mean, median, and standard deviation,min,max,count,uniqueness and generates histograms for numeric columns.

Data Visualization: It creates histograms for each numeric column to represent the data distribution visually.

Styled HTML Tables: The project includes enhanced styling for HTML tables to improve data presentation.

Requirements
- Python 3.12.4
- Django
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Sample CSV File For Testing Purpose

A sample CSV file for testing purposes is included in the repository.
Folder Name = Sample_CSV_Files

