from src.extract import extract_csv 
from src.transform import (inspect_data, remove_duplicates, remove_missing_values,save_processed_data)
from src.database import engine
from src.load import load_to_postgres

def main():
    # Step 1: Extract data from CSV
    customers = extract_csv("data/raw/olist_customers_dataset.csv")

    if customers is None:
        print("Failed to extract data.")
        return
    
    inspect_data(customers)

    customers = remove_duplicates(customers)

    customers = remove_missing_values(customers)

    save_processed_data(customers, "data/processed/customers_cleaned.csv")

    load_to_postgres(customers, "customers", engine)

    print("ETL process completed successfully!")
    
if __name__ == "__main__":
    main()  


