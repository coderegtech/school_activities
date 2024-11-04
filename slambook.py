import datetime

import pyinputplus as pyip

from database import Database


class Slambook(Database):

    def validate_name(self, name):
        if all(x.isalpha() or x.isspace() for x in name):
            return True
        else:
            print("Invalid name. Only alphabetic characters and spaces are allowed.")
            return False

    def validate_age(self, age):
        if age.isdigit() and 0 < int(age) < 120:
            return True
        else:
            print("Invalid age. Please enter a number between 1 and 120.")
            return False

    def validate_email(self, email):
        if "@" in email and "." in email and len(email) > 5:
            return True
        else:
            print("Invalid email. Please enter a valid email address.")
            return False

    def validate_favorite_number(self, number):
        if number.isdigit():
            return True
        else:
            print("Invalid number. Please enter a valid number.")
            return False

    def validate_contact_number(self, contact):
        if contact.isdigit() and 10 <= len(contact) <= 15:
            return True
        else:
            print("Invalid contact number. Please enter a 10 to 15 digit number.")
            return False

    def validate_birthday(self, birthday):
        try:
            datetime.datetime.strptime(birthday, '%Y-%m-%d')
            return True
        except ValueError:
            print("Invalid birthday. Please enter the date in YYYY-MM-DD format.")
            return False

    def validate_dream(self, dream):
        if len(dream.strip()) > 0:
            return True
        else:
            print("Dream cannot be empty.")
            return False

    def validate_hobby(self, hobby):
        if len(hobby.strip()) > 0:
            return True
        else:
            print("Hobby cannot be empty.")
            return False

    def validate_address(self, address):
        if len(address.strip()) > 0:
            return True
        else:
            print("Address cannot be empty.")
            return False

    def get_valid_input(self, prompt, validation_func):
        while True:
            user_input = input(prompt)
            if validation_func(user_input):
                return user_input

    def addEntry(self):
        print("="*40)
        name = self.get_valid_input("Enter Name: ", self.validate_name)
        age = self.get_valid_input("Enter Age: ", self.validate_age)
        email = self.get_valid_input("Enter Email: ", self.validate_email)
        favorite_number = self.get_valid_input("Enter Favorite Number: ", self.validate_favorite_number)
        contact_number = self.get_valid_input("Enter Contact Number: ", self.validate_contact_number)
        birthday = self.get_valid_input("Enter Birthday (YYYY-MM-DD):", self.validate_birthday)
        address = self.get_valid_input("Enter Address: ", self.validate_address)
        dream = self.get_valid_input("Enter Your Dream: ", self.validate_dream)
        hobby = self.get_valid_input("Enter Your Hobby: ", self.validate_hobby)

        # Insert the data into the database
        self.insertEntry(name, age, email, favorite_number, contact_number, birthday, address, dream, hobby)

    def displayInfo(self):
        print("="*40)
        print("===== All Slambook Entries ====")
        print("="*40)
        items = self.fetchAllItems()

        if items:
            for item in items:
                print(f"> ID: {item[0]}")
                print(f"> Name: {item[1]}")
                print(f"> Age: {item[2]}")
                print(f"> Email: {item[3]}")
                print(f"> Favorite Number: {item[4]}")
                print(f"> Contact Number: {item[5]}")
                print(f"> Birthday: {item[6]}")
                print(f"> Address: {item[7]}")
                print(f"> Dream: {item[8]}")
                print(f"> Hobby: {item[9]}")
                print("="*40)
    
    def deleteItem(self):
        print("="*40)
        id = int(input("Enter item ID: "))
        # remove item from the list
        self.removeItem(id)


    def main(self):
        while True:
            print("=" * 40)
            print(" Welcome to the Autograph/Slambook Program ")
            print("=" * 40)
            print("[1] Display Entries")
            print("[2] Insert Entries")
            print("[3] Delete Entry")
            print("[0] Exit")
            print("=" * 40)

            try:
                choose = int(input("Enter your choice: "))
            except ValueError:
                print("=" * 40)
                print("Invalid input. Please enter a number.")
                continue  

            if choose == 1:
                self.displayInfo()
            elif choose == 2:
                self.addEntry()
            elif choose == 3:
                self.deleteItem()
            elif choose == 0:
                print("=" * 40)
                print("Exiting the program. Goodbye!")
                break 
            else:
                print("Invalid choice. Please select a valid option.")

        

        
                
        


"""
    def validate_name(self, name):
        if all(x.isalpha() or x.isspace() for x in name):
            return True
        else:
            print("Invalid name. Only alphabetic characters and spaces are allowed.")
            return False

    def validate_age(self, age):
        if age.isdigit() and 0 < int(age) < 120:
            return True
        else:
            print("Invalid age. Please enter a number between 1 and 120.")
            return False

    def validate_email(self, email):
        if "@" in email and "." in email and len(email) > 5:
            return True
        else:
            print("Invalid email. Please enter a valid email address.")
            return False

    def validate_favorite_number(self, number):
        if number.isdigit():
            return True
        else:
            print("Invalid number. Please enter a valid number.")
            return False

    def validate_contact_number(self, contact):
        if contact.isdigit() and 10 <= len(contact) <= 15:
            return True
        else:
            print("Invalid contact number. Please enter a 10 to 15 digit number.")
            return False

    def validate_birthday(self, birthday):
        try:
            datetime.datetime.strptime(birthday, '%Y-%m-%d')
            return True
        except ValueError:
            print("Invalid birthday. Please enter the date in YYYY-MM-DD format.")
            return False

    def validate_dream(self, dream):
        if len(dream.strip()) > 0:
            return True
        else:
            print("Dream cannot be empty.")
            return False

    def validate_hobby(self, hobby):
        if len(hobby.strip()) > 0:
            return True
        else:
            print("Hobby cannot be empty.")
            return False

    def validate_address(self, address):
        if len(address.strip()) > 0:
            return True
        else:
            print("Address cannot be empty.")
            return False
"""