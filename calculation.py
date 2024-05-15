import mysql.connector
from mysql.connector import Error


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


def insert_calculation(connection, operation, result):
    insert_query = """
    INSERT INTO calculations (operation, result)
    VALUES (%s, %s)
    """
    cursor = connection.cursor()
    cursor.execute(insert_query, (operation, result))
    connection.commit()


def add(x: float, y: float) -> float:
    return x + y


def subtract(x: float, y: float) -> float:
    return x - y


def multiplication(x: float, y: float) -> float:
    return x * y


def division(x: float, y: float) -> float:
    if y == 0:
        raise ValueError("Cannot divide by error")
    return x // y


def perform_calculations():
    connection = connect_to_db()
    if connection is not None:
        create_table(connection)

        calculations = [
            ('Add', add(10, 12)),
            ('Subtract', subtract(20, 12)),
            ('Multiply', multiplication(5, 8)),
            ('Divide', division(25, 5))
        ]

        for operation, result in calculations:
            insert_calculation(connection, operation, result)
            print(f"The result of {operation} operation: {result}")

        connection.close()
    else:
        print("Failed to connect to the database")


perform_calculations()
