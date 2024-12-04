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
    db1_path = os.path.join(root, "data", "dataset_1.db")
    db2_path = os.path.join(root, "data", "dataset_2.db")
    print(root)
    print(db1_path)
    print(db2_path)

    assert os.path.exists(db1_path)
    assert os.path.exists(db2_path)

    # conn = sqlite3.connect(db1_path)

    # expected_row_counts_db1 = 

    # for table_name, expected_row_count in expected_row_counts.items():
    #     db_data = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    # #     assert len(db_data) == expected_row_count
    
    # conn.close()