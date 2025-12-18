import pandas as pd
from sqlalchemy import create_engine

# SQLite database path
DB_PATH = "sqlite:///salary.db"

# Create engine
engine = create_engine(DB_PATH)

def load_data(csv_path="data/Salary Data.csv"):
    """Load salary.csv into SQLite database (run once)"""
    df = pd.read_csv(csv_path)
    df.to_sql("salary", con=engine, if_exists="replace", index=False)
    print("✅ Data loaded into database.")
