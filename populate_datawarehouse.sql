INSERT INTO city (CityID, CityName, Region, Country) VALUES
(1, 'Beijing', 'Beijing', 'CN'),
(2, 'Shanghai', 'Shanghai', 'CN'),
(3, 'Guangzhou', 'Guangdong', 'CN'),
(4, 'Shenzhen', 'Guangdong', 'CN'),
(5, 'Chengdu', 'Sichuan', 'CN'),
(6, 'Xi', 'Shaanxi', 'CN'),
(7, 'Hangzhou', 'Zhejiang', 'CN'),
(8, 'Chongqing', 'Chongqing', 'CN'),
(9, 'Wuhan', 'Hubei', 'CN'),
(10, 'Tianjin', 'Tianjin', 'CN'),
(11, 'New York', 'New York', 'US'),
(12, 'Los Angeles', 'California', 'US'),
(13, 'Chicago', 'Illinois', 'US'),
(14, 'Houston', 'Texas', 'US'),
(15, 'Phoenix', 'Arizona', 'US'),
(16, 'Philadelphia', 'Pennsylvania', 'US'),
(17, 'San Antonio', 'Texas', 'US'),
(18, 'San Diego', 'California', 'US'),
(19, 'Dallas', 'Texas', 'US'),
(20, 'San Jose', 'California', 'US'),
(21, 'London', 'England', 'GB'),
(22, 'Birmingham', 'England', 'GB'),
(23, 'Leeds', 'England', 'GB'),
(24, 'Glasgow', 'Scotland', 'GB'),
(25, 'Sheffield', 'England', 'GB'),
(26, 'Manchester', 'England', 'GB'),
(27, 'Edinburgh', 'Scotland', 'GB'),
(28, 'Liverpool', 'England', 'GB'),
(29, 'Bristol', 'England', 'GB'),
(30, 'Cardiff', 'Wales', 'GB');

INSERT INTO station (StationID, StationName, Location) VALUES
(1, 'Station A', 'Location A'),
(2, 'Station B', 'Location B'),
(3, 'Station C', 'Location C'),
(4, 'Station D', 'Location D'),
(5, 'Station E', 'Location E'),
(6, 'Station F', 'Location F'),
(7, 'Station G', 'Location G'),
(8, 'Station H', 'Location H'),
(9, 'Station I', 'Location I'),
(10, 'Station J', 'Location J'),
(11, 'Station K', 'Location K'),
(12, 'Station L', 'Location L'),
(13, 'Station M', 'Location M'),
(14, 'Station N', 'Location N'),
(15, 'Station O', 'Location O'),
(16, 'Station P', 'Location P'),
(17, 'Station Q', 'Location Q'),
(18, 'Station R', 'Location R'),
(19, 'Station S', 'Location S'),
(20, 'Station T', 'Location T');

INSERT INTO time (TimeID, Date, Time, Year, Month, Day, Hour)
SELECT 
    TO_CHAR(datum, 'yyyymmdd')::INT AS TimeID,
    datum AS Date,
    '00:00:00' AS Time,
    EXTRACT(YEAR FROM datum) AS Year,
    EXTRACT(MONTH FROM datum) AS Month,
    EXTRACT(DAY FROM datum) AS Day,
    0 AS Hour
FROM (
    SELECT generate_series(
        TIMESTAMP '2021-01-01 00:00:00', 
        TIMESTAMP '2021-12-31 23:00:00', 
        INTERVAL '1 hour'
    ) AS datum
) AS generated_series
ON CONFLICT (TimeID) DO NOTHING;


INSERT INTO pollutant_metrics (MetricID, MetricName, Min, Max, Median, Standard_Deviation) VALUES
(1, 'pressure', 1010.5, 1043.5, 1026, 50),
(2, 'temperature', -15, 40, 12, 15),
(3, 'humidity', 20, 100, 60, 20),
(4, 'pm10', 0, 200, 50, 30),
(5, 'pm2.5', 0, 150, 35, 25),
(6, 'ozone', 10, 200, 100, 40),
(7, 'sulfur dioxide', 0, 20, 5, 5),
(8, 'nitrogen dioxide', 0, 40, 20, 10),
(9, 'carbon monoxide', 0, 10, 2, 3),
(10, 'ammonia', 0, 100, 50, 10);

INSERT INTO meteorological_metrics (MetricID, MetricName, Min, Max, Median, Standard_Deviation) VALUES
(1, 'temperature', -10, 38, 15, 20),
(2, 'humidity', 0, 100, 60, 15),
(3, 'precipitation', 0, 300, 50, 75),
(4, 'wind speed', 0, 150, 25, 35),
(5, 'visibility', 0, 10, 8, 3),
(6, 'dew point', -20, 25, 10, 10),
(7, 'UV index', 0, 11, 5, 4),
(8, 'air pressure', 950, 1050, 1013, 25),
(9, 'cloud cover', 0, 100, 60, 20),
(10, 'snow depth', 0, 200, 30, 50);

INSERT INTO data_entry (
    EntryID, 
    CityID, 
    StationID, 
    TimeID, 
    WeatherCondition, 
    Temperature, 
    Humidity, 
    WindSpeed, 
    Visibility, 
    AirPressure, 
    DataQualityIndicator, 
    Remarks, 
    PollutionMetricID, 
    MeteorologicalMetricID
) VALUES
(1, 1, 1, 1, 'Clear', 20.5, 40, 5.2, 10, 1015, 'Good', 'No remarks', 1, 1),
(2, 2, 1, 2, 'Cloudy', 22.0, 50, 3.5, 8, 1020, 'Good', 'Slight cloud cover', 2, 2),
(3, 3, 2, 3, 'Rainy', 18.0, 85, 7.0, 5, 1010, 'Moderate', 'Light rain', 3, 3),
(4, 4, 2, 4, 'Sunny', 25.0, 30, 4.0, 12, 1022, 'Excellent', 'Clear skies', 4, 4),
(5, 5, 3, 5, 'Windy', 17.5, 45, 20.0, 6, 1011, 'Good', 'High winds', 5, 5),
(6, 1, 3, 6, 'Foggy', 16.0, 95, 1.0, 2, 1009, 'Poor', 'Low visibility', 6, 6),
(7, 2, 4, 7, 'Snow', -5.0, 80, 10.0, 3, 997, 'Moderate', 'Light snowfall', 7, 7),
(8, 3, 4, 8, 'Hail', 0.0, 100, 15.0, 1, 1005, 'Poor', 'Hailstorm', 8, 8),
(9, 4, 5, 9, 'Sunny', 30.0, 25, 6.0, 14, 1018, 'Good', 'Very warm and clear', 9, 9),
(10, 5, 5, 10, 'Cloudy', 20.0, 55, 2.0, 9, 1012, 'Good', 'Overcast', 10, 10),
(11, 1, 6, 11, 'Rainy', 15.0, 90, 8.0, 4, 1002, 'Moderate', 'Heavy rain', 11, 11),
(12, 2, 6, 12, 'Foggy', 10.0, 98, 1.5, 1, 1000, 'Poor', 'Dense fog', 12, 12),
(13, 3, 7, 13, 'Windy', 22.0, 40, 25.0, 10, 1007, 'Good', 'Strong winds', 13, 13),
(14, 4, 7, 14, 'Sunny', 28.0, 30, 5.0, 13, 1015, 'Excellent', 'Sunny and pleasant', 14, 14),
(15, 5, 8, 15, 'Thunderstorm', 19.0, 70, 12.0, 2, 1003, 'Poor', 'Thunder and lightning', 15, 15),
(16, 1, 8, 16, 'Drizzle', 17.0, 85, 3.0, 7, 1009, 'Moderate', 'Light drizzle', 16, 16),
(17, 2, 9, 17, 'Overcast', 21.0, 60, 4.5, 8, 1011, 'Good', 'Gloomy sky', 17, 17),
(18, 3, 9, 18, 'Mist', 14.0, 95, 2.0, 3, 1004, 'Moderate', 'Misty conditions', 18, 18),
(19, 4, 10, 19, 'Clear', 26.0, 35, 8.0, 15, 1020, 'Excellent', 'Sunny and warm', 1, 2),
(20, 5, 10, 20, 'Cloudy', 18.0, 60, 4.0, 10, 1015, 'Good', 'Partly cloudy', 2, 3),
(21, 1, 11, 21, 'Rainy', 14.0, 80, 6.5, 5, 1005, 'Moderate', 'Steady rain', 3, 4),
(22, 2, 11, 22, 'Sunny', 29.0, 28, 7.0, 16, 1022, 'Excellent', 'Sunny and hot', 4, 5),
(23, 3, 12, 23, 'Windy', 23.0, 45, 18.0, 6, 1009, 'Good', 'Strong gusts', 5, 6),
(24, 4, 12, 24, 'Foggy', 10.0, 98, 2.0, 2, 1000, 'Poor', 'Thick fog', 6, 7),
(25, 5, 13, 25, 'Snow', -2.0, 75, 12.0, 4, 998, 'Moderate', 'Heavy snowfall', 7, 8),
(26, 1, 13, 26, 'Thunderstorm', 20.0, 70, 14.0, 3, 1003, 'Poor', 'Thunder and rain', 8, 9),
(27, 2, 14, 27, 'Drizzle', 16.0, 88, 3.5, 7, 1006, 'Moderate', 'Light rain', 9, 10),
(28, 3, 14, 28, 'Overcast', 19.0, 65, 5.0, 8, 1010, 'Good', 'Gray skies', 10, 11),
(29, 5, 10, 29, 'Cloudy', 18.0, 60, 4.0, 10, 1015, 'Good', 'Partly cloudy', 2, 3),
(30, 1, 11, 30, 'Rainy', 14.0, 80, 6.5, 5, 1005, 'Moderate', 'Steady rain', 3, 4
),
(
  31, 2, 11, 31, 'Sunny', 29.0, 28, 7.0, 16, 1022, 'Excellent', 'Sunny and hot', 4, 5
),
(
  32, 3, 12, 32, 'Windy', 23.0, 45, 18.0, 6, 1009, 'Good', 'Strong gusts', 5, 6
),
(
  33, 4, 12, 33, 'Foggy', 10.0, 98, 2.0, 2, 1000, 'Poor', 'Thick fog', 6, 7
),
(
  34, 5, 13, 34, 'Snow', -2.0, 75, 12.0, 4, 998, 'Moderate', 'Heavy snowfall', 7, 8
),
(
  35, 1, 13, 35, 'Thunderstorm', 20.0, 70, 14.0, 3, 1003, 'Poor', 'Thunder and rain', 8, 9
),
(
  36, 2, 14, 36, 'Drizzle', 16.0, 88, 3.5, 7, 1006, 'Moderate', 'Light rain', 9, 10
),
(
  37, 3, 14, 37, 'Overcast', 19.0, 65, 5.0, 8, 1010, 'Good', 'Gray skies', 10, 11
),
(
  38, 4, 15, 38, 'Mist', 15.0, 90, 2.5, 4, 1007, 'Moderate', 'Hazy conditions', 11, 12
),
(
  39, 5, 15, 39, 'Sunny', 30.0, 30, 7.0, 15, 1021, 'Excellent', 'Bright and clear', 12, 13
),
(
  40, 1, 16, 40, 'Cloudy', 22.0, 55, 4.0, 9, 1014, 'Good', 'Partly overcast', 13, 14
),
(
  41, 2, 16, 41, 'Rainy', 16.0, 85, 6.5, 6, 1006, 'Moderate', 'Steady rainfall', 14, 15
),
(
  42, 3, 17, 42, 'Sunny', 28.0, 25, 5.5, 14, 1019, 'Excellent', 'Warm and sunny', 15, 16
),
(
  43, 4, 17, 43, 'Foggy', 10.0, 95, 1.0, 3, 1002, 'Poor', 'Dense fog', 16, 17
),
(
  44, 5, 18, 44, 'Snow', -3.0, 75, 11.0, 4, 996, 'Moderate', 'Snow showers', 17, 18
),
(
  45, 1, 18, 45, 'Thunderstorm', 18.0, 70, 15.0, 2, 1001, 'Poor', 'Thunder and rain', 18, 19
),
(
  46, 2, 19, 46, 'Drizzle', 15.0, 88, 3.0, 7, 1005, 'Moderate', 'Light drizzle', 19, 20
),
(
  47, 3, 19, 47, 'Overcast', 20.0, 60, 4.5, 8, 1011, 'Good', 'Overcast skies', 20, 21
),
(
  48, 4, 20, 48, 'Mist', 14.0, 92, 2.0, 2, 1004, 'Moderate', 'Hazy conditions', 21, 22
),
(
  49, 5, 20, 49, 'Sunny', 31.0, 28, 8.0, 16, 1025, 'Excellent', 'Sunny and hot', 22, 23
),
(
  50, 1, 21, 50, 'Clear', 27.0, 35, 7.0, 14, 1018, 'Excellent', 'Clear and pleasant', 23, 24
),
(
  51, 2, 21, 51, 'Cloudy', 19.0, 55, 3.5, 9, 1013, 'Good', 'Partly cloudy', 24, 25
),
(
  52, 3, 22, 52, 'Rainy', 13.0, 80, 6.0, 5, 1008, 'Moderate', 'Steady rain', 25, 26
),
(
  53, 4, 22, 53, 'Sunny', 30.0, 30, 5.0, 12, 1021, 'Excellent', 'Clear skies', 26, 27
),
(
  54, 5, 23, 54, 'Windy', 20.0, 45, 22.0, 7, 1006, 'Good', 'Strong winds', 27, 28
),
(
  55, 1, 23, 55, 'Foggy', 11.0, 97, 1.5, 1, 999, 'Poor', 'Dense fog', 28, 29
),
(
  56, 2, 24, 56, 'Snow', -1.0, 78, 10.5, 3, 995, 'Moderate', 'Snowfall', 29, 30
),
(
  57, 3, 24, 57, 'Hail', 2.0, 100, 16.0, 1, 1007, 'Poor', 'Hailstorm', 30, 31
),
(
  58, 4, 25, 58, 'Sunny', 32.0, 26, 6.5, 14, 1016, 'Excellent', 'Very hot and sunny', 31, 32
),
(
  59, 5, 25, 59, 'Cloudy', 21.0, 60, 4.0, 10, 1014, 'Good', 'Partly cloudy', 32, 33
),
(
  60, 1, 26, 60, 'Rainy', 16.0, 87, 8.0, 5, 1003, 'Moderate', 'Heavy rainfall', 33, 34
),
(
  61, 2, 26, 61, 'Foggy', 10.0, 95, 1.0, 2, 1002, 'Poor', 'Low visibility', 34, 35
),
(
  62, 3, 27, 62, 'Windy', 24.0, 42, 24.0, 8, 1008, 'Good', 'Blustery conditions', 35, 36
),
(
  63, 4, 27, 63, 'Sunny', 29.0, 28, 5.0, 12, 1020, 'Excellent', 'Sunny and warm', 36, 37
),
(
  64, 5, 28, 64, 'Thunderstorm', 18.0, 70, 14.0, 3, 1005, 'Poor', 'Thunder and lightning', 37, 38
),
(
  65, 1, 28, 65, 'Drizzle', 15.0, 88, 3.0, 7, 1009, 'Moderate', 'Light drizzle', 38, 39
),
(
  66, 2, 29, 66, 'Overcast', 20.0, 60, 4.5, 8, 1011, 'Good', 'Overcast skies', 39, 40
),
(
  67, 3, 29, 67, 'Mist', 15.0, 92, 2.0, 2, 1004, 'Moderate', 'Hazy conditions', 40, 41
),
(
  68, 4, 30, 68, 'Sunny', 31.0, 28, 7.0, 15, 1023, 'Excellent', 'Clear and hot', 41, 42
),
(
  69, 5, 30, 69, 'Clear', 28.0, 33, 6.0, 14, 1017, 'Excellent', 'Clear and pleasant', 42, 43
),
(
  70, 1, 31, 70, 'Cloudy', 20.0, 55, 4.0, 9, 1013, 'Good', 'Partly cloudy', 43, 44
),
(
  71, 2, 31, 71, 'Rainy', 16.0, 85, 6.5, 6, 1006, 'Moderate', 'Steady rainfall', 44, 45
),
(
  72, 3, 32, 72, 'Sunny', 27.0, 26, 5.5, 13, 1020, 'Excellent', 'Warm and sunny', 45, 46
),
(
  73, 4, 32, 73, 'Foggy', 10.0, 95, 1.0, 3, 1003, 'Poor', 'Dense fog', 46, 47
),
(
  74, 5, 33, 74, 'Snow', -4.0, 73, 11.0, 5, 994, 'Moderate', 'Snowfall', 47, 48
),
(
  75, 1, 33, 75, 'Thunderstorm', 17.0, 72, 15.0, 2, 1000, 'Poor', 'Thunder and rain', 48, 49
),
(
  76, 2, 34, 76, 'Drizzle', 14.0, 90, 3.0, 7, 1004, 'Moderate', 'Light drizzle', 49, 50
),
(
  77, 3, 34, 77, 'Overcast', 19.0, 62, 4.5, 8, 1012, 'Good', 'Cloudy skies', 50, 51
),
(
  78, 4, 35, 78, 'Mist', 14.0, 91, 2.0, 2, 1005, 'Moderate', 'Misty conditions', 51, 52
),
(
  79, 5, 35, 79, 'Sunny', 32.0, 29, 7.0, 15, 1022, 'Excellent', 'Clear and hot', 52, 53
),
(
  80, 1, 36, 80, 'Clear', 26.0, 36, 6.5, 13, 1016, 'Excellent', 'Clear and pleasant', 53, 54
),
(
  81, 2, 36, 81, 'Cloudy', 19.0, 57, 3.5, 9, 1014, 'Good', 'Partly cloudy', 54, 55
); 
