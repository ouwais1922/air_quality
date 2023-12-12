import pandas as pd
from faker import Faker
from sqlalchemy import create_engine
import psycopg2
from datetime import datetime, timedelta
import random

# Database connection parameters
db_params = {
    "host": "your_host",
    "database": "your_database",
    "user": "your_user",
    "password": "your_password",
    "port": "your_port",
}

# Create a Faker instance
fake = Faker()

# Number of rows to generate
num_rows = 100

# Generate random data for the city table
city_data = {
    'CityID': range(1, num_rows + 1),
    'CityName': [fake.city() for _ in range(num_rows)],
    'Region': [fake.word() for _ in range(num_rows)],
    'Country': [fake.country_code() for _ in range(num_rows)]
}
city_df = pd.DataFrame(city_data)

# Generate random data for the station table
station_data = {
    'StationID': range(1, num_rows + 1),
    'StationName': [fake.word() for _ in range(num_rows)],
    'Location': [fake.word() for _ in range(num_rows)]
}
station_df = pd.DataFrame(station_data)

# Generate random data for the time table
time_data = {
    'TimeID': range(1, num_rows + 1),
    'Timestamp': [fake.date_time_this_decade() for _ in range(num_rows)],
    'Date': [fake.date_between(start_date='-365d', end_date='today') for _ in range(num_rows)],
    'Time': [fake.time_object() for _ in range(num_rows)],
    'Year': [fake.random_int(2000, 2022) for _ in range(num_rows)],
    'Month': [fake.random_int(1, 12) for _ in range(num_rows)],
    'Day': [fake.random_int(1, 28) for _ in range(num_rows)],
    'Hour': [fake.random_int(0, 23) for _ in range(num_rows)]
}
time_df = pd.DataFrame(time_data)

# Generate random data for pollutant_metrics table
pollutant_metrics_data = {
    'MetricID': range(1, num_rows + 1),
    'MetricName': [fake.word() for _ in range(num_rows)],
    'Min': [random.uniform(0, 10) for _ in range(num_rows)],
    'Max': [random.uniform(10, 20) for _ in range(num_rows)],
    'Median': [random.uniform(5, 15) for _ in range(num_rows)],
    'Standard_Deviation': [random.uniform(1, 5) for _ in range(num_rows)]
}
pollutant_metrics_df = pd.DataFrame(pollutant_metrics_data)

# Generate random data for meteorological_metrics table
meteorological_metrics_data = {
    'MetricID': range(1, num_rows + 1),
    'MetricName': [fake.word() for _ in range(num_rows)],
    'Min': [random.uniform(-10, 0) for _ in range(num_rows)],
    'Max': [random.uniform(0, 10) for _ in range(num_rows)],
    'Median': [random.uniform(-5, 5) for _ in range(num_rows)],
    'Standard_Deviation': [random.uniform(1, 5) for _ in range(num_rows)]
}
meteorological_metrics_df = pd.DataFrame(meteorological_metrics_data)

# Generate random data for data_entry table
data_entry_data = {
    'EntryID': range(1, num_rows + 1),
    'CityID': [fake.random_int(1, num_rows) for _ in range(num_rows)],
    'StationID': [fake.random_int(1, num_rows) for _ in range(num_rows)],
    'TimeID': [fake.random_int(1, num_rows) for _ in range(num_rows)],
    'WeatherCondition': [fake.word() for _ in range(num_rows)],
    'Temperature': [random.uniform(-10, 30) for _ in range(num_rows)],
    'Humidity': [random.uniform(0, 100) for _ in range(num_rows)],
    'WindSpeed': [random.uniform(0, 20) for _ in range(num_rows)],
    'Visibility': [random.uniform(0, 10) for _ in range(num_rows)],
    'AirPressure': [random.uniform(900, 1100) for _ in range(num_rows)],
    'DataQualityIndicator': [fake.word() for _ in range(num_rows)],
    'Remarks': [fake.text() for _ in range(num_rows)],
    'PollutionMetricID': [fake.random_int(1, num_rows) for _ in range(num_rows)],
    'MeteorologicalMetricID': [fake.random_int(1, num_rows) for _ in range(num_rows)]
}
data_entry_df = pd.DataFrame(data_entry_data)

# Convert 'Date' column to the proper format
data_entry_df['Date'] = pd.to_datetime(data_entry_df['Date'])

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(**db_params)

# Create a SQLAlchemy engine
engine = create_engine(f"postgresql+psycopg2://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}")

# Write the DataFrames to the PostgreSQL database
city_df.to_sql('city', engine, if_exists='replace', index=False)
station_df.to_sql('station', engine, if_exists='replace', index=False)
time_df.to_sql('time', engine, if_exists='replace', index=False)
pollutant_metrics_df.to_sql('pollutant_metrics', engine, if_exists='replace', index=False)
meteorological_metrics_df.to_sql('meteorological_metrics', engine, if_exists='replace', index=False)
data_entry_df.to_sql('data_entry', engine, if_exists='replace', index=False)

# Close the database connection
conn.close()