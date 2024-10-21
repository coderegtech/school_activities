import mysql.connector

"""
CREATE DATABASE slambook_db;
USE slambook_db;

CREATE TABLE IF NOT EXISTS slambook (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(100) NOT NULL,
    favorite_number INT NOT NULL,
    contact_number VARCHAR(15) NOT NULL,
    birthday DATE NOT NULL,
    address VARCHAR(255) NOT NULL,
    dream VARCHAR(255) NOT NULL,
    hobby VARCHAR(255) NOT NULL
);
"""

class Database:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="codereg25",
                database="slambook_db"
            )
            self.cursor = self.conn.cursor()
            print("Database connected successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.conn = None

    def insertEntry(self, name, age, email, favorite_number, contact_number, birthday, address, dream, hobby):
        if self.conn:
            query = """
            INSERT INTO slambook (name, age, email, favorite_number, contact_number, birthday, address, dream, hobby)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (name, age, email, favorite_number, contact_number, birthday, address, dream, hobby)
            try:
                self.cursor.execute(query, values)
                self.conn.commit()
                print("="*40)
                print("Slambook entry inserted successfully!")
            except mysql.connector.Error as err:
                print(f"Error: {err}")

    def fetchAllItems(self):
        if self.conn:
            query = """
            SELECT * FROM slambook
            """
            try:
                self.cursor.execute(query)
                data = self.cursor.fetchall()
                return data
            except mysql.connector.Error as err:
                print(f"Error: {err}")

    def removeItem(self, id):
        if self.conn:
            query = """
            DELETE FROM slambook WHERE id = %s
            """
            values = (id, )
            try:
                self.cursor.execute(query, values)
                self.conn.commit()
                print("="*40)
                print("Item removed successfully!")
            except mysql.connector.Error as err:
                print(f"Error: {err}")


    def close_connection(self):
        """Close the database connection."""
        if self.conn:
            self.cursor.close()
            self.conn.close()