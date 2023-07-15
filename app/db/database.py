import mysql.connector
from app.configs import DatabaseConfigs


class DatabaseManager:
    def __init__(self):
        self.host = DatabaseConfigs.DATABASE_HOST
        self.user = DatabaseConfigs.DATABASE_USER
        self.password = DatabaseConfigs.DATABASE_PASSWORD
        self.database = DatabaseConfigs.DATABASE_NAME
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Connected to the database.")

        except mysql.connector.Error as error:
            print("Error connecting to the database:", error)

    def execute_ddl(self, ddl_file):
        try:
            with open(ddl_file, 'r') as f:
                ddl_statements = f.read().split(';')

            cursor = self.connection.cursor()
            for statement in ddl_statements:
                if statement:
                    try:
                        cursor.execute(statement)
                        self.connection.commit()
                        print("DDL statement executed successfully")
                    except Exception as e:
                        print(f"Error executing DDL statement: {e}")
            cursor.close()
        except mysql.connector.Error as error:
            print("Error executing DDL statement:", error)

    def execute_dml(self, dml_file):
        try:
            with open(dml_file, 'r') as f:
                dml_statements = f.read().split(';')

            cursor = self.connection.cursor()
            for statement in dml_statements:
                if statement:
                    try:
                        cursor.execute(statement)
                        self.connection.commit()
                        print("DML statement executed successfully")
                    except Exception as e:
                        print(f"Error executing DML statement: {e}")
            cursor.close()
            print("DML executed successfully.")

        except mysql.connector.Error as error:
            print("Error executing DML statement:", error)

    def execute_select_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            return results
        except mysql.connector.Error as error:
            print("Error executing query:", error)
            return None

    def execute_insert_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            cursor.close()
            return f"{query} executed"
        except mysql.connector.Error as error:
            print("Error executing query:", error)
            return None

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")
