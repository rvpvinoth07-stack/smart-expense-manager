import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vino9626@7868",
        database="expense_db"
    )

print("Connection Successful...!")