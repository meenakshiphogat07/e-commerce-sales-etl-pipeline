import pandas as pd

def inspect_data(df):
    """
    Inspects a pandas DataFrame and prints various information about it."""

    print("\n===========DATASET SUMMARY============")

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nMissing Values in Each Column:")
    print(df.isnull().sum())

    print("\nDuplicated Rows:")
    print(df.duplicated().sum())

    print("\nData Types:")
    print(df.dtypes)

def remove_duplicates(df):
    """Removess duplicate rows from the Dataafarame."""

    before=len(df)

    df=df.drop_duplicates()

    after=len(df)

    print(f"\nDuplicate rows removed: {before - after}")

    return df

def remove_missing_values(df):
    """Removes rows containing missing values."""

    before=len(df)

    df=df.dropna()

    after=len(df)

    print(f"\nRows removed due to missing values: {before - after}")

    return df

def save_processed_data(df, output_path):
    """Saves the processed DataFrame to a CSV file."""

    try:
        df.to_csv(output_path, index=False)
        print(f"\nProcessed data saved to {output_path}")
    except Exception as e:
        print(f"\nError saving processed data: {e}")