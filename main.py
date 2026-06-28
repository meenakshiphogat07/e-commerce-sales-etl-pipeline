from src.extract import extract_csv 
from src.transform import (inspect_data, remove_duplicates, remove_missing_values,save_processed_data)

customers = extract_csv("data/raw/olist_customers_dataset.csv")

if customers is not None:
    inspect_data(customers)

    customers = remove_duplicates(customers)

    customers = remove_missing_values(customers)

    save_processed_data(customers, "data/processed/customers_cleaned.csv")

    print("\n Final shape")
    print(customers.shape)