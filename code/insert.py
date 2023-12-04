import psycopg2
from faker import Faker
import random
from datetime import datetime, timedelta

# PostgreSQL connection parameters
postgres_params = {
    'host': '10.121.23.200',
    'user': 'postgres',
    'password': 'postgres',
    'database': 'dataware',
}

# Connect to PostgreSQL
connection = psycopg2.connect(**postgres_params)
cursor = connection.cursor()

# Function to generate fake data
fake = Faker()

def generate_fake_measurement():
    return fake.date_between(start_date='-30d', end_date='today'), fake.random_int(1, 10), fake.word(), fake.random_int(10, 100), fake.random_number(), fake.random_number(), fake.random_number()

def generate_fake_pollutant_metric():
    return fake.word(), fake.word(), fake.random_number()

def generate_fake_meteorological_metric():
    return fake.word(), fake.word(), fake.random_number()

# Insert data into MeasurementsDimension
for _ in range(100):
    date, count, specie, min_value, max_value, median, variance = generate_fake_measurement()
    cursor.execute("INSERT INTO MeasurementsDimension (date, count, specie, min_value, max_value, median, variance) VALUES (%s, %s, %s, %s, %s, %s, %s)", (date, count, specie, min_value, max_value, median, variance))

# Insert data into PollutantMetricsDimension
for _ in range(5):
    pollutant_name, unit, measurement_value = generate_fake_pollutant_metric()
    cursor.execute("INSERT INTO PollutantMetricsDimension (pollutant_name, unit, measurement_value) VALUES (%s, %s, %s)", (pollutant_name, unit, measurement_value))

# Insert data into MeteorologicalMetricsDimension
for _ in range(5):
    metric_name, unit, measurement_value = generate_fake_meteorological_metric()
    cursor.execute("INSERT INTO MeteorologicalMetricsDimension (metric_name, unit, measurement_value) VALUES (%s, %s, %s)", (metric_name, unit, measurement_value))

# Insert data into CitiesDimension
for _ in range(10):
    city_name = fake.unique.city()
    country_code = fake.country_code()
    cursor.execute("INSERT INTO CitiesDimension (city_name, country_code) VALUES (%s, %s)", (city_name, country_code))

# Insert data into FactTable
for _ in range(50000):
    # Generate a random measurement_id or retrieve an existing one from MeasurementsDimension
    cursor.execute("SELECT measurement_id FROM MeasurementsDimension ORDER BY RANDOM() LIMIT 1")
    result = cursor.fetchone()
    measurement_id = result[0] if result else None

    # Ensure that the 'city_id' exists in CitiesDimension
    cursor.execute("SELECT city_id FROM CitiesDimension ORDER BY RANDOM() LIMIT 1")
    result = cursor.fetchone()
    city_id = result[0] if result else None

    pollutant_metric_id = random.randint(1, 5)
    meteorological_metric_id = random.randint(1, 5)
    value = random.uniform(1.0, 100.0)

    cursor.execute("INSERT INTO FactTable (measurement_id, city_id, pollutant_metric_id, meteorological_metric_id, value) VALUES (%s, %s, %s, %s, %s)", (measurement_id, city_id, pollutant_metric_id, meteorological_metric_id, value))

# Commit changes and close connection
connection.commit()
cursor.close()
connection.close()
