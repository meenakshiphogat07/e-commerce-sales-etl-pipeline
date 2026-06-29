from src.extract import extract_csv
from src.transform import (
    inspect_data,
    remove_duplicates,
    remove_missing_values,
    save_processed_data
)
from src.database import engine
from src.load import load_to_postgres

datasets = {
    "customers": "olist_customers_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "order_payments": "olist_order_payments_dataset.csv",
    "order_reviews": "olist_order_reviews_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "geolocation": "olist_geolocation_dataset.csv",
    "category_translation": "product_category_name_translation.csv"
}


def main():

    for table_name, file_name in datasets.items():

        print(f"\n{'='*50}")
        print(f"Processing {table_name}")
        print(f"{'='*50}")

        try:
            df = extract_csv(f"data/raw/{file_name}")

            if df is None:
                continue

            inspect_data(df)

            df = remove_duplicates(df)

            df = remove_missing_values(df)

            save_processed_data(
                df,
                f"data/processed/{table_name}_cleaned.csv"
            )

            load_to_postgres(
                df,
                table_name,
                engine
            )

            print(f"{table_name} completed successfully!")

        except Exception as e:
            print(f"Error processing {table_name}: {e}")


if __name__ == "__main__":
    main()


