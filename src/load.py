import pandas as pd


def load_to_postgres(df, table_name, engine):
    """
    Loads a Pandas DataFrame into a PostgreSQL table.
    """
    try:
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace",
            index=False
        )

        print(f"Data successfully loaded into table '{table_name}'")

    except Exception as e:
        print(f"Error loading data: {e}")