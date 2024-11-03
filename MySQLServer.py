import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL Server
        connection = mysql.connector.connect(
            host="localhost",
            user="AaronAyitey",   # Replace with your MySQL username
            password="**********" # Replace with your MySQL password
        )
        
        # Create a cursor object
        cursor = connection.cursor()

        # Try creating the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        # Handle errors for connection issues or permissions
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Please check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        print("Database connection closed.")

if __name__ == "__main__":
    create_database()
