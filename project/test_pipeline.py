import os
import sqlite3
import pandas as pd
import pytest
from pipeline import extract_data, transform_data, load_data


def test_data_pipeline():
    df1, df2 = extract_data()
    df1, df2 = transform_data(df1, df2)
    load_data(df1, df2)

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(root, "data", "airquality_on_ev.db")

    assert os.path.exists(db_path)

def test_data_quality():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(root, "data", "airquality_on_ev.db")

    conn = sqlite3.connect(db_path)

    expected_row_counts = {
        "airquality": 173076,
        "electric_vehicle": 18025
    }

    for table_name, expected_row_count in expected_row_counts.items():
        db_data = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        assert len(db_data) == expected_row_count
    
    conn.close()