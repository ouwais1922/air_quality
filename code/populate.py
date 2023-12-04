from sqlalchemy import create_engine, select, insert, Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

# PostgreSQL connection parameters
postgres_params = {
    'host': '10.121.23.200',
    'port': '5432',
    'user': 'postgres',
    'password': 'postgres',
    'database': 'covid',
}

# MySQL connection parameters
mysql_params = {
    'host': '10.121.23.200',
    'port': '3306',
    'user': 'root',
    'password': 'password',
    'database': 'covid',
}

# PostgreSQL engine
postgres_engine = create_engine(
    f"postgresql+psycopg2://{postgres_params['user']}:{postgres_params['password']}@{postgres_params['host']}:{postgres_params['port']}/{postgres_params['database']}"
)

# MySQL engine
mysql_engine = create_engine(
    f"mysql+mysqlconnector://{mysql_params['user']}:{mysql_params['password']}@{mysql_params['host']}:{mysql_params['port']}/{mysql_params['database']}"
)

# Create sessions
SessionPostgres = sessionmaker(bind=postgres_engine)
SessionMySQL = sessionmaker(bind=mysql_engine)

# Define the table classes for the dimensions and fact table
Base = declarative_base()

class CitiesDimension(Base):
    __tablename__ = 'cities'

    city_id = Column(Integer, primary_key=True)
    country_code = Column(String(2))
    city_name = Column(String(255))

class MeasurementsDimension(Base):
    __tablename__ = 'measurements'

    measurement_id = Column(Integer, primary_key=True)
    date = Column(Date)
    specie = Column(String(255))
    count = Column(Integer)
    min_value = Column(Float)
    max_value = Column(Float)
    median = Column(Float)
    variance = Column(Float)

class PollutantMetricsDimension(Base):
    __tablename__ = 'pollutant_metrics'

    pollutant_metric_id = Column(Integer, primary_key=True)
    pollutant_name = Column(String(255))
    unit = Column(String(50))
    measurement_value = Column(Float)

class MeteorologicalMetricsDimension(Base):
    __tablename__ = 'meteorological_metrics'

    meteorological_metric_id = Column(Integer, primary_key=True)
    metric_name = Column(String(255))
    unit = Column(String(50))
    measurement_value = Column(Float)

class FactTable(Base):
    __tablename__ = 'fact_table'

    fact_id = Column(Integer, primary_key=True)
    measurement_id = Column(Integer, ForeignKey('measurements.measurement_id'))
    city_id = Column(Integer, ForeignKey('cities.city_id'))
    pollutant_metric_id = Column(Integer, ForeignKey('pollutant_metrics.pollutant_metric_id'))
    meteorological_metric_id = Column(Integer, ForeignKey('meteorological_metrics.meteorological_metric_id'))
    value = Column(Float)

# Create tables in MySQL
Base.metadata.create_all(bind=mysql_engine)

# Copy data from PostgreSQL to MySQL
# Copy data from PostgreSQL to MySQL
with SessionPostgres() as postgres_session, SessionMySQL() as mysql_session:
    # Copy data from CitiesDimension
    cities_data = postgres_session.execute(select(CitiesDimension))
    mysql_session.execute(insert(CitiesDimension).values(list(cities_data)))

    # Copy data from MeasurementsDimension
    measurements_data = postgres_session.execute(select(MeasurementsDimension))
    mysql_session.execute(insert(MeasurementsDimension).values(list(measurements_data)))

    # Copy data from PollutantMetricsDimension
    pollutant_metrics_data = postgres_session.execute(select(PollutantMetricsDimension))
    mysql_session.execute(insert(PollutantMetricsDimension).values(list(pollutant_metrics_data)))

    # Copy data from MeteorologicalMetricsDimension
    meteorological_metrics_data = postgres_session.execute(select(MeteorologicalMetricsDimension))
    mysql_session.execute(insert(MeteorologicalMetricsDimension).values(list(meteorological_metrics_data)))

    # Copy data from FactTable
    fact_table_data = postgres_session.execute(select(FactTable))
    mysql_session.execute(insert(FactTable).values(list(fact_table_data)))

