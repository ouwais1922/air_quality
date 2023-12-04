Cities Table:

No direct relationships with other tables.
Measurements Table:

Relationship: Many-to-One (M:1) with the cities table.
Explanation: Many measurements can be associated with one city.
Pollutant Metrics Table:

Relationship: Many-to-One (M:1) with both the cities and measurements tables.
Explanation:
Many pollutant metrics can be associated with one city.
Many pollutant metrics can be associated with one measurement.
Meteorological Metrics Table:

Relationship: Many-to-One (M:1) with both the cities and measurements tables.
Explanation:
Many meteorological metrics can be associated with one city.
Many meteorological metrics can be associated with one measurement.



mysql -h 127.0.0.1 -P 3306 -uroot -p

------------------------------------------------

DW:

Fact Table:
FactTable (fact_id, measurement_id, city_id, pollutant_metric_id, meteorological_metric_id, value):
fact_id: Primary key for the fact table.
measurement_id: Foreign key referencing the measurements table.
city_id: Foreign key referencing the cities table.
pollutant_metric_id: Foreign key referencing the pollutant_metrics table.
meteorological_metric_id: Foreign key referencing the meteorological_metrics table.
value: The numerical value or metric.
Dimension Tables:
CitiesDimension (city_id, country_code, city_name):

city_id: Primary key for the cities dimension.
country_code: Country code for the city.
city_name: Name of the city.
MeasurementsDimension (measurement_id, date, specie, count, min_value, max_value, median, variance):

measurement_id: Primary key for the measurements dimension.
date: Date of the measurement.
specie: Specie measured.
count: Count of measurements.
min_value: Minimum measured value.
max_value: Maximum measured value.
median: Median of measurements.
variance: Variance of measurements.
PollutantMetricsDimension (pollutant_metric_id, pollutant_name, unit, measurement_value):

pollutant_metric_id: Primary key for the pollutant metrics dimension.
pollutant_name: Name of the pollutant.
unit: Unit of measurement.
measurement_value: Measurement value for the pollutant.
MeteorologicalMetricsDimension (meteorological_metric_id, metric_name, unit, measurement_value):

meteorological_metric_id: Primary key for the meteorological metrics dimension.
metric_name: Name of the meteorological metric.
unit: Unit of measurement.
measurement_value: Measurement value for the meteorological metric.