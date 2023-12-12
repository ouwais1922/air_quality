CREATE TABLE city (
    CityID INT PRIMARY KEY,
    CityName VARCHAR(255),
    Region VARCHAR(255),
    Country VARCHAR(255)
    -- Additional columns if necessary
);

CREATE TABLE station (
    StationID INT PRIMARY KEY,
    StationName VARCHAR(255),
    Location VARCHAR(255)
    -- Additional columns if necessary
);

CREATE TABLE time (
    TimeID INT PRIMARY KEY,
    Timestamp TIMESTAMP,
    Date DATE,
    Time TIME,
    Year INT,
    Month INT,
    Day INT,
    Hour INT
    -- Additional columns if necessary
);

CREATE TABLE pollutant_metrics (
    MetricID INT PRIMARY KEY,
    MetricName VARCHAR(255),
    Min DECIMAL,
    Max DECIMAL,
    Median DECIMAL,
    Standard_Deviation DECIMAL
    -- Additional columns if necessary
);

CREATE TABLE meteorological_metrics (
    MetricID INT PRIMARY KEY,
    MetricName VARCHAR(255),
    Min DECIMAL,
    Max DECIMAL,
    Median DECIMAL,
    Standard_Deviation DECIMAL
    -- Additional columns if necessary
);

CREATE TABLE data_entry (
    EntryID INT PRIMARY KEY,
    CityID INT,
    StationID INT,
    TimeID INT,
    WeatherCondition VARCHAR(255),
    Temperature DECIMAL,
    Humidity DECIMAL,
    WindSpeed DECIMAL,
    Visibility DECIMAL,
    AirPressure DECIMAL,
    DataQualityIndicator VARCHAR(255),
    Remarks TEXT,
    PollutionMetricID INT,
    MeteorologicalMetricID INT,
    FOREIGN KEY (CityID) REFERENCES city(CityID),
    FOREIGN KEY (StationID) REFERENCES station(StationID),
    FOREIGN KEY (TimeID) REFERENCES time(TimeID),
    FOREIGN KEY (PollutionMetricID) REFERENCES pollutant_metrics(MetricID),
    FOREIGN KEY (MeteorologicalMetricID) REFERENCES meteorological_metrics(MetricID)
    -- Additional columns if necessary
);
