import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import random

# CSV file path
csv_file_path = '../dataset/covid.csv'
# PostgreSQL connection parameters
postgres_connection_params = {
    'host': '10.121.23.200',
    'port': '5432',
    'user': 'postgres',
    'password': 'postgres',
    'database': 'covid',
}

# Read CSV file into a Pandas DataFrame
df = pd.read_csv(csv_file_path)

# Connect to PostgreSQL database
engine = create_engine(
    f"postgresql+psycopg2://{postgres_connection_params['user']}:{postgres_connection_params['password']}@{postgres_connection_params['host']}:{postgres_connection_params['port']}/{postgres_connection_params['database']}"
)

# Insert data into 'cities' table
df_cities = df[['Country', 'City']].drop_duplicates().reset_index(drop=True)
df_cities.to_sql('cities', engine, if_exists='replace', index=False)

# Insert data into 'measurements' table
df_measurements = df[['Date', 'Country', 'City', 'Specie', 'count', 'min', 'max', 'median', 'variance']]
df_measurements.to_sql('measurements', engine, if_exists='replace', index=False)

# Generate random data for 'pollutant_metrics' and 'meteorological_metrics'
num_records = 1000  # Adjust as needed

pollutant_metrics_data = []
meteorological_metrics_data = []

for _ in range(num_records):
    city_id = random.choice(df_cities.index)
    measurement_id = random.choice(df_measurements.index)
    pollutant_name = f'Pollutant_{random.randint(1, 5)}'
    metric_name = f'Metric_{random.randint(1, 5)}'
    unit = 'unit'
    measurement_value = random.uniform(1.0, 100.0)

    # Print information about the row being created
    print(f"Creating row - city_id: {city_id}, measurement_id: {measurement_id}, pollutant_name: {pollutant_name}, metric_name: {metric_name}, unit: {unit}, measurement_value: {measurement_value}")

    pollutant_metrics_data.append({'city_id': city_id, 'measurement_id': measurement_id, 'pollutant_name': pollutant_name, 'unit': unit, 'measurement_value': measurement_value})
    meteorological_metrics_data.append({'city_id': city_id, 'measurement_id': measurement_id, 'metric_name': metric_name, 'unit': unit, 'measurement_value': measurement_value})

# Insert data into 'pollutant_metrics' table
df_pollutant_metrics = pd.DataFrame(pollutant_metrics_data)
df_pollutant_metrics.to_sql('pollutant_metrics', engine, if_exists='replace', index=False)

# Insert data into 'meteorological_metrics' table
df_meteorological_metrics = pd.DataFrame(meteorological_metrics_data)
df_meteorological_metrics.to_sql('meteorological_metrics', engine, if_exists='replace', index=False)

engine.dispose()
