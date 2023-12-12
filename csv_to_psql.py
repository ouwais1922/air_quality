import pandas as pd
import psycopg2
from psycopg2 import sql

# Database connection parameters
db_params = {
    "dbname": "waqi",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost"
}

# Connect to the database
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# Read CSV file
csv_file = '/home/aui/datawarehouse/dataset/covid.csv'
df = pd.read_csv(csv_file)

# Functions to get IDs from dimension tables (conceptual, needs actual implementation)
def get_city_id(city_name, cursor):
    try:
        # Prepare the SQL query to find the CityID
        query = "SELECT CityID FROM city WHERE CityName = %s;"
        
        # Execute the query with the city_name parameter
        cursor.execute(query, (city_name,))
        
        # Fetch the result
        result = cursor.fetchone()
        
        # Check if a result was found
        if result:
            return result[0]  # Return the CityID
        else:
            return None  # No matching city found
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def get_station_id(station_name, cursor):
    try:
        # Prepare the SQL query to find the StationID
        query = "SELECT StationID FROM station WHERE StationName = %s;"
        
        # Execute the query with the station_name parameter
        cursor.execute(query, (station_name,))
        
        # Fetch the result
        result = cursor.fetchone()
        
        # Check if a result was found
        if result:
            return result[0]  # Return the StationID
        else:
            return None  # No matching station found
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def get_time_id(date, time, cursor):
    try:
        # Format the date and time into the format stored in your database
        # Assuming your date format is 'YYYY-MM-DD' and time format is 'HH:MM:SS'
        formatted_date_time = f"{date} {time}"

        # Prepare the SQL query to find the TimeID
        # Assuming your table has a combined date and time column named 'DateTime'
        query = "SELECT TimeID FROM time WHERE DateTime = %s;"
        
        # Execute the query with the formatted_date_time parameter
        cursor.execute(query, (formatted_date_time,))
        
        # Fetch the result
        result = cursor.fetchone()
        
        # Check if a result was found
        if result:
            return result[0]  # Return the TimeID
        else:
            return None  # No matching time found
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_pollutant_metric_id(specie, cursor):
    try:
        # Prepare the SQL query to find the MetricID
        query = "SELECT MetricID FROM pollutant_metrics WHERE MetricName = %s;"
        
        # Execute the query with the specie parameter
        cursor.execute(query, (specie,))
        
        # Fetch the result
        result = cursor.fetchone()
        
        # Check if a result was found
        if result:
            return result[0]  # Return the MetricID
        else:
            return None  # No matching metric found
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_meteorological_metric_id(specie, cursor):
    try:
        # Prepare the SQL query to find the MetricID
        query = "SELECT MetricID FROM meteorological_metrics WHERE MetricName = %s;"
        
        # Execute the query with the specie parameter
        cursor.execute(query, (specie,))
        
        # Fetch the result
        result = cursor.fetchone()
        
        # Check if a result was found
        if result:
            return result[0]  # Return the MetricID
        else:
            return None  # No matching metric found
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def default_time_id(date, cursor):
    # Insert a new entry into the time table with the given date and default time
    # Then return the newly created TimeID
    try:
        default_time = '00:00:00'  # Default time
        cursor.execute("INSERT INTO time (Date, Time) VALUES (%s, %s) RETURNING TimeID;", (date, default_time))
        time_id = cursor.fetchone()[0]
        return time_id
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
# Define a default temperature value
default_temperature = 0.0  # or any other value that makes sense in your context


# Iterate over DataFrame rows
for index, row in df.iterrows():
    # Map CSV data to dimension IDs. This step is conceptual.
    # You need to replace the logic with actual ID retrieval or mapping based on your data.
    city_id = get_city_id(row['City'], cursor)  # Function to get city_id from city name
    station_id = get_station_id(row['Station'], cursor) if 'Station' in df.columns else None
  # Similar function for station
    time_id = get_time_id(row['Date'], row['Time'], cursor) if 'Time' in df.columns else default_time_id
    temperature = row['Temperature'] if 'Temperature' in df.columns else default_temperature

  # Function to get time_id
    pollutant_metric_id = get_pollutant_metric_id(row['Specie'], cursor)  # Function for pollutant_metric
    meteorological_metric_id = get_meteorological_metric_id(row['Specie'], cursor)  # Function for meteorological_metric

    # Generate SQL insert statement
    cursor.execute(
        sql.SQL("INSERT INTO data_entry (EntryID, CityID, StationID, TimeID, Temperature, Humidity, WindSpeed, Visibility, AirPressure, DataQualityIndicator, Remarks, PollutionMetricID, MeteorologicalMetricID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"),
        (index, city_id, station_id, time_id, row['Temperature'], row['Humidity'], row['WindSpeed'], row['Visibility'], row['AirPressure'], row['DataQualityIndicator'], row['Remarks'], pollutant_metric_id, meteorological_metric_id)
    )

# Commit and close the database connection
conn.commit()
cursor.close()
conn.close()




