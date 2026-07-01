import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mite",
        database="apartment_rental1"
    )
    return conn
