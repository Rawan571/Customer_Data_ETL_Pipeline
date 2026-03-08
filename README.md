# Customer Data ETL Pipeline

## 📌 Project Overview
This project demonstrates a functional **ETL (Extract, Transform, Load)** pipeline built with Python and the Pandas library. It processes raw customer transaction data to prepare it for business analysis.

## 🛠️ Tech Stack
- **Language:** Python 3
- **Library:** Pandas

## ⚙️ ETL Workflow
1.  **Extract:** Generated a sample dataset of customer transactions within the script for demonstration.
2.  **Transform (Data Cleaning):**
    - Filtered records to include only 'purchase' transactions.
    - Handled missing values (Nulls) to ensure data accuracy.
    - Converted date columns to proper datetime objects.
3.  **Aggregate:** Grouped data by `customer_id` to calculate the total transaction amount per customer.
4.  **Load:** Exported the processed summary into a structured CSV file (`customer_purchase_summary.csv`).

## 🚀 How to Run
1. Clone the repository.
2. Ensure you have `pandas` installed: `pip install pandas`.
3. Run the script: `python etl_script.py`.


