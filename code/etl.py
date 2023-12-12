import psycopg2
from faker import Faker
from random import randint, uniform
import datetime


# Connect to the PostgreSQL database
conn = psycopg2.connect(
 host="localhost",
    database="newdb",
    user="postgres",
    password="postgres"
)
cursor = conn.cursor()

# Create a Faker instance
fake = Faker()

# Function to generate random datetime within a range
def random_date(start_date, end_date):
    start_datetime = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    return fake.date_time_between_dates(datetime_start=start_datetime, datetime_end=end_datetime)

# Function to generate random weather conditions
def random_weather_condition():
    conditions = ['Clear', 'Cloudy', 'Rainy', 'Snowy', 'Foggy']
    return fake.random_element(elements=conditions)

# Function to generate random metric values
def generate_random_metrics():
    return (
        round(uniform(0, 100), 2),   # Min
        round(uniform(100, 200), 2), # Max
        round(uniform(50, 150), 2),  # Median
        round(uniform(0, 10), 2)     # Standard Deviation
    )

# Insert data into pollutant_metrics table
for metric_id in range(1, 6):
    metric_values = generate_random_metrics()
    cursor.execute("""
        INSERT INTO pollutant_metrics (MetricID, MetricName, Min, Max, Median, Standard_Deviation)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (metric_id, f'Metric_{metric_id}', *metric_values))

# Insert data into meteorological_metrics table
for metric_id in range(6, 11):
    metric_values = generate_random_metrics()
    cursor.execute("""
        INSERT INTO meteorological_metrics (MetricID, MetricName, Min, Max, Median, Standard_Deviation)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (metric_id, f'Metric_{metric_id}', *metric_values))

# Insert data into city table
for city_id in range(1, 11):
    cursor.execute("""
        INSERT INTO city (CityID, CityName, Region, Country)
        VALUES (%s, %s, %s, %s)
    """, (city_id, f'City_{city_id}', f'Region_{city_id}', f'Country_{city_id}'))

# Insert data into station table
for station_id in range(1, 21):
    cursor.execute("""
        INSERT INTO station (StationID, StationName, Location)
        VALUES (%s, %s, %s)
    """, (station_id, f'Station_{station_id}', f'Location_{station_id}'))

# Insert data into time table
for time_id in range(1, 101):
    timestamp = random_date(start_date="2022-01-01", end_date="2023-12-31")
    date, time = timestamp.date(), timestamp.time()
    cursor.execute("""
        INSERT INTO time (TimeID, Timestamp, Date, Time, Year, Month, Day, Hour)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (time_id, timestamp, date, time, timestamp.year, timestamp.month, timestamp.day, timestamp.hour))

# Insert data into data_entry table
# Insert data into data_entry table
for _ in range(10000):
    city_id = randint(1, 10)
    station_id = randint(1, 20)
    time_id = randint(1, 100)

    data_entry_values = (
        city_id,
        station_id,
        time_id,
        random_weather_condition(),
        round(uniform(-10, 40), 2),
        round(uniform(0, 100), 2),
        round(uniform(0, 20), 2),
        round(uniform(0, 50), 2),
        round(uniform(900, 1100), 2),
        fake.random_element(elements=['Good', 'Moderate', 'Poor', 'Very Poor', 'Hazardous']),
        fake.text(),
        randint(1, 5),
        randint(6, 10)
    )

    cursor.execute("""
        INSERT INTO data_entry 
        (CityID, StationID, TimeID, WeatherCondition, Temperature, Humidity, 
        WindSpeed, Visibility, AirPressure, DataQualityIndicator, Remarks, 
        PollutionMetricID, MeteorologicalMetricID) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, data_entry_values)


# Commit the changes and close the connection
conn.commit()
conn.close()
