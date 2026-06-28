import pandas as pd

def extract_csv(file_path):
    """
    Reads a CSV file and returns a pandas DataFrame."""
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully read the CSV file: {file_path}")
        return df
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return None
    

