import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password"
    )

    if db.is_connected():
        mycursor = db.cursor()

        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

        mycursor.close()
        db.close()

except mysql.connector.Error as e:
    print(f"Error: {e}")
