import pathlib
current_file_path = pathlib.Path(__file__)


class Configs:
    JWT_SECRET_KEY = 'My-Name-Sundar'


class DatabaseConfigs:
    DATABASE_HOST = 'sql-database'
    DATABASE_USER = 'root'
    DATABASE_PASSWORD = 'sundar123'
    DATABASE_NAME = 'school'


class DDLandDMLConfigs:
    current_file_path = pathlib.Path(__file__)
    DDL_FILE_PATH = f"{current_file_path.parent}/sql/schema.sql"
    DML_FILE_PATH = f"{current_file_path.parent}/sql/data.sql"
