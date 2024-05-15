import mysql.connector
from mysql.connector import Error


class Database:
    @staticmethod
    def connect_to_db():
        try:
            return mysql.connector.connect(
                host='localhost',
                user='root',
                password='Harsh@8189',
                database='user'
            )
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return None

    @staticmethod
    def create_table(connection):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS Calculations (
            operation VARCHAR(10),
            result FLOAT
        )
        """
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()

    @staticmethod
    def insert_calculation(connection, operation, result):
        insert_query = """
        INSERT INTO calculations (operation, result)
        VALUES (%s, %s)
        """
        cursor = connection.cursor()
        cursor.execute(insert_query, (operation, result))
        connection.commit()


class Calculator:

    @staticmethod
    def add(x: float, y: float) -> float:
        return x + y

    @staticmethod
    def subtract(x: float, y: float) -> float:
        return x - y

    @staticmethod
    def multiplication(x: float, y: float) -> float:
        return x * y

    @staticmethod
    def division(x: float, y: float) -> float:
        if y == 0:
            raise ValueError("Cannot divide by error")
        return x // y

    @staticmethod
    def perform_calculations():
        connection = Database.connect_to_db()
        if connection is not None:
            Database.create_table(connection)

            calculations = [
                ('Add', Calculator.add(10, 12)),
                ('Subtract', Calculator.subtract(20, 12)),
                ('Multiply', Calculator.multiplication(5, 8)),
                ('Divide', Calculator.division(25, 5))
            ]

            for operation, result in calculations:
                Database.insert_calculation(connection, operation, result)
                print(f"The result of {operation} operation: {result}")

            connection.close()
        else:
            print("Failed to connect to the database")


Calculator.perform_calculations()
