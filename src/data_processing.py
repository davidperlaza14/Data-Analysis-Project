import os
import pandas as pd


# Function to load data from a CSV file.
def load_data(filepath=None):
    if filepath is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(base_dir, '../data/dataset.csv')
    else:
        if not os.path.isabs(filepath):
            base_dir = os.path.dirname(os.path.abspath(__file__))
            filepath = os.path.join(base_dir, filepath)

    print(f"Loading data from: {filepath}")
    return pd.read_csv(filepath, delimiter=';')

# Function to clean and prepare data.
def preprocess_data(df):
    df.columns.str.strip()
    
    df = df.replace({'Pachac�mac': 'Pachacámac', 'Mi Per�': 'Mi Perú'}, regex=True)
    
    df['Area'] = pd.to_numeric(df['Area'], errors='coerce')
    df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
    df['Mantenimiento'] = pd.to_numeric(df['Mantenimiento'], errors='coerce')
    df['Impuesto'] = pd.to_numeric(df['Impuesto'], errors='coerce')
    df['Valor m2'] = pd.to_numeric(df['Valor m2'], errors='coerce')
    
    return df

if __name__ == "__main__":
    data = load_data('../data/dataset.csv')
    data = preprocess_data(data)
    print(data.head())