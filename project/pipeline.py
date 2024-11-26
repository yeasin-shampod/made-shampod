import requests
import pandas as pd
import sqlite3
from io import BytesIO

# Function to download data from a URL and load into pandas DataFrame
def load_data_from_url(url, is_excel=True):
    response = requests.get(url)
    response.raise_for_status()  # Ensure request was successful
    
    if is_excel:
        # For Excel files
        excel_data = BytesIO(response.content)
        return pd.read_excel(excel_data, sheet_name="AllData")
    else:
        # For CSV files
        return pd.read_csv(BytesIO(response.content))


# Air quality data (Excel)
air_quality_url = "https://apps.epa.vic.gov.au/datavic/Data_Vic/AirWatch/2022_All_sites_air_quality_hourly_avg_AIR-I-F-V-VH-O-S1-DB-M2-4-0.xlsx"
df_air_quality = load_data_from_url(air_quality_url, is_excel=True)

# NYC dataset (CSV)
nyc_data_url = "https://data.cityofnewyork.us/api/views/c3uy-2p5r/rows.csv?accessType=DOWNLOAD"
df_nyc = load_data_from_url(nyc_data_url, is_excel=False)

# Example of cleaning, you can add specific transformations here
df_air_quality = df_air_quality.dropna()  # Drop missing values
# df_air_quality['Date'] = pd.to_datetime(df_air_quality['Date'], errors='coerce')

df_nyc = df_nyc.dropna()  # Drop missing values
# df_nyc['datetime_AEST'] = pd.to_datetime(df_nyc['Date'], errors='coerce')

# Step 3: Store the data in SQLite
conn = sqlite3.connect('./data/combined_data.db')

# Store both datasets into separate tables
df_air_quality.to_sql('air_quality_data', conn, if_exists='replace', index=False)
df_nyc.to_sql('nyc_data', conn, if_exists='replace', index=False)

# Step 4: Close the connection
conn.close()

print("Data pipeline executed successfully and both datasets stored in SQLite.")
