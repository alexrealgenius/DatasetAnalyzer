import pandas as pd


def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: Could not find the dataset at {file_path}")
        return None
