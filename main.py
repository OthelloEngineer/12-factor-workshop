from flask import Flask, render_template
import numpy as np
from dotenv import load_dotenv
from os import getenv
import mysql.connector
from mysql.connector import Error
app = Flask(__name__)


@app.route('/')
def index():
    numpy_version = False
    env_correct = False
    db_connection_successful = False


    # Check for numpy
    numpy_version = check_if_numpy_version_is_correct()


    # Check for env
    if numpy_version == True:
        load_dotenv()
        if getenv('DEBUG').lower() == "true":
            env_correct = True


        # Check for database (docker compose)
        if env_correct == True:
            db_connection_successful = check_if_database_is_connected()

    # Returns the page:
    return render_template("index.html",
                           numpy_version=numpy_version,
                           env_correct=env_correct,
                           db_connection_successful=db_connection_successful)


def check_if_numpy_version_is_correct():
    try:
        _ = np.typeDict['float64']
        print("Numpt is the correct version.")
        return True
    except Exception as error:
        print(error)
        return False


def check_if_database_is_connected():
    MYSQL_DATABASE = getenv('MYSQL_DATABASE')
    MYSQL_PORT = 3306
    MYSQL_HOST = getenv('MYSQL_HOST')
    MYSQL_USER = getenv('MYSQL_USER')
    MYSQL_PASSWORD = getenv('MYSQL_PASSWORD')


    try:
        # Establish the connection to the MySQL database
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE,
            port=MYSQL_PORT
        )

        if connection.is_connected():
            # Execute a simple query to check the connection
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            db_name = cursor.fetchone()
            print(f"Connected to MySQL database: {db_name[0]}")

            return True

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()




if __name__ == '__main__':
    app.run(host='0.0.0.0')
