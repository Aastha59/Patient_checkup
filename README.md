Project Overview

This project involves analyzing patient records from a dataset to uncover insights into key healthcare metrics such as patient age, length of stay, and their statistical trends. By using Python and its powerful data analysis libraries, we calculate and present meaningful statistics to assist in decision-making and improve healthcare outcomes.

Features

Data Loading: Reads patient data from a CSV file.

Statistical Analysis:

Calculates mean, median, and standard deviation for patient age and length of stay.

Provides a summary of key healthcare statistics.

Output Results: Prints the calculated statistics to the console for easy interpretation.

Requirements

To run this project, you need the following:

Python 3.x

pandas library

Installation

Clone the repository or download the script.

Ensure Python 3.x is installed on your system.

Install the required library by running:

pip install pandas

Place the dataset file (hospital_treatment.csv) in the same directory as the script.

Usage

Run the script using the following command:

python <script_name>.py

The script will output statistical information about patient age and length of stay, including:

Mean

Median

Standard deviation

Dataset

The dataset used in this project contains the following columns:

Pulmonology: Index or reference for patient records.

Patient_Name: Name of the patient.

Age: Age of the patient.

Gender: Gender of the patient.

Diagnosis: Diagnosis details.

Length of Stay (days): Number of days the patient stayed in the hospital.

Hospital department: Department responsible for the patient's treatment.

Example Output

Age Statistics:
Mean: 35.67
Median: 30.0
Standard Deviation: 15.2

Length of Stay Statistics:
Mean: 4.2
Median: 4.0
Standard Deviation: 1.5

Future Enhancements

Add data visualization for better insights.

Handle missing or inconsistent data more robustly.

Provide graphical summaries of department-specific trends.

License

This project is open-source and available under the MIT License.
