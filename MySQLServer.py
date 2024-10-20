import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        mydb = mysql.connector.connect(
            user = 'root',
            password = 'KRMVNS2024.$mysql',
            host = 'localhost'
        )
        cursor = mydb.cursor()
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.errors as err:
            print(F"Failed creating database: {err}")
        cursor.close()
        mydb.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
if __name__ == "__main__":
    create_database()