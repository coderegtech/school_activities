import datetime

import mysql.connector

"""
CREATE DATABASE student_data;
USE student_data;

CREATE TABLE IF NOT EXISTS student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_number VARCHAR(20) NOT NULL UNIQUE,
    last_name VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    middle_initial CHAR(1),
    course VARCHAR(100) NOT NULL,
    cell_phone_no VARCHAR(15) NOT NULL,
    date_of_birth DATE NOT NULL,
    religion VARCHAR(50) NOT NULL,
    vaccination_status ENUM('Yes', 'No') NOT NULL,
    gmail_acc VARCHAR(100) NOT NULL UNIQUE
);

"""


class StudentDatabase:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="codereg25",
                database="student_data"
            )
            self.cursor = self.conn.cursor()
            print("Database connected successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.conn = None

    def insertEntry(self, student_number, last_name, first_name, middle_initial, course, cell_phone_no, date_of_birth, religion, vaccination_status, gmail_acc):
        if self.conn:
            query = """
            INSERT INTO student (student_number, last_name, first_name, middle_initial, course, cell_phone_no, date_of_birth, religion, vaccination_status, gmail_acc)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (student_number, last_name, first_name, middle_initial, course, cell_phone_no, date_of_birth, religion, vaccination_status, gmail_acc)
            try:
                self.cursor.execute(query, values)
                self.conn.commit()
                print("="*40)
                print("Student entry inserted successfully!")
            except mysql.connector.Error as err:
                print(f"Error: {err}")

    def fetchAllItems(self):
        if self.conn:
            query = """
            SELECT * FROM student
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
            DELETE FROM student WHERE id = %s
            """
            values = (id, )
            try:
                self.cursor.execute(query, values)
                self.conn.commit()
                print("="*40)
                print("Student record removed successfully!")
            except mysql.connector.Error as err:
                print(f"Error: {err}")

    def close_connection(self):
        """Close the database connection."""
        if self.conn:
            self.cursor.close()
            self.conn.close()


class StudentEnrollment(StudentDatabase):

    def validate_student_number(self, student_number):
        if student_number.isdigit():
            return True
        else:
            print("Invalid student number. Please enter a numeric value.")
            return False

    def validate_name(self, name):
        if all(x.isalpha() or x.isspace() for x in name):
            return True
        else:
            print("Invalid name. Only alphabetic characters and spaces are allowed.")
            return False

    def validate_middle_initial(self, initial):
        if len(initial) == 1 and initial.isalpha():
            return True
        else:
            print("Invalid middle initial. Please enter a single alphabetic character.")
            return False

    def validate_course(self, course):
        if len(course.strip()) > 0:
            return True
        else:
            print("Course cannot be empty.")
            return False

    def validate_contact_number(self, contact):
        if contact.isdigit() and 10 <= len(contact) <= 15:
            return True
        else:
            print("Invalid contact number. Please enter a 10 to 15 digit number.")
            return False

    def validate_date_of_birth(self, dob):
        try:
            datetime.datetime.strptime(dob, '%Y-%m-%d')
            return True
        except ValueError:
            print("Invalid date of birth. Please enter the date in YYYY-MM-DD format.")
            return False

    def validate_religion(self, religion):
        if len(religion.strip()) > 0:
            return True
        else:
            print("Religion cannot be empty.")
            return False

    def validate_vaccination(self, vaccination):
        if vaccination.lower() in ["yes", "no"]:
            return True
        else:
            print("Invalid vaccination status. Please enter 'Yes' or 'No'.")
            return False

    def validate_email(self, email):
        if "@" in email and "." in email and len(email) > 5:
            return True
        else:
            print("Invalid email. Please enter a valid email address.")
            return False

    def get_valid_input(self, prompt, validation_func):
        while True:
            user_input = input(prompt)
            if validation_func(user_input):
                return user_input

    def addStudent(self):
        print("="*40)
        student_number = self.get_valid_input("Enter Student Number: ", self.validate_student_number)
        last_name = self.get_valid_input("Enter Last Name: ", self.validate_name)
        first_name = self.get_valid_input("Enter First Name: ", self.validate_name)
        middle_initial = self.get_valid_input("Enter Middle Initial: ", self.validate_middle_initial)
        course = self.get_valid_input("Enter Course: ", self.validate_course)
        cell_phone_no = self.get_valid_input("Enter Contact Number: ", self.validate_contact_number)
        date_of_birth = self.get_valid_input("Enter Date of Birth (YYYY-MM-DD): ", self.validate_date_of_birth)
        religion = self.get_valid_input("Enter Religion: ", self.validate_religion)
        vaccination = self.get_valid_input("Vaccinated? (Yes/No): ", self.validate_vaccination)
        gmail_acc = self.get_valid_input("Enter Gmail Account: ", self.validate_email)

        # Insert the data into the database
        self.insertEntry(student_number, last_name, first_name, middle_initial, course, cell_phone_no, date_of_birth, religion, vaccination, gmail_acc)

    def displayStudents(self):
        print("="*40)
        print("===== All Student Entries ====")
        print("="*40)
        items = self.fetchAllItems()

        if items:
            for item in items:
                print(f"> Student Number: {item[0]}")
                print(f"> Last Name: {item[1]}")
                print(f"> First Name: {item[2]}")
                print(f"> Middle Initial: {item[3]}")
                print(f"> Course: {item[4]}")
                print(f"> Contact Number: {item[5]}")
                print(f"> Date of Birth: {item[6]}")
                print(f"> Religion: {item[7]}")
                print(f"> Vaccinated: {item[8]}")
                print(f"> Gmail Account: {item[9]}")
                print("="*40)

    def deleteStudent(self):
        print("="*40)
        try:
            id = int(input("Enter student ID to delete: "))
            self.removeItem(id)
        except ValueError:
            print("Invalid ID. Please enter a numeric value.")

    def main(self):
        while True:
            print("=" * 40)
            print(" Welcome to the Student Enrollment System ")
            print("=" * 40)
            print("[1] Display Students")
            print("[2] Add Student")
            print("[3] Delete Student")
            print("[0] Exit")
            print("=" * 40)

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue  

            if choice == 1:
                self.displayStudents()
            elif choice == 2:
                self.addStudent()
            elif choice == 3:
                self.deleteStudent()
            elif choice == 0:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

