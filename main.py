from src.extract import extract_csv 
from src.transform import (inspect_data, remove_duplicates, remove_missing_values,)

customers = extract_csv("data/raw/olist_customers_dataset.csv")

if customers is not None:
    inspect_data(customers)

    customers = remove_duplicates(customers)

    customers = remove_missing_values(customers)

    print("\n Final shape")
    print(customers.shape)