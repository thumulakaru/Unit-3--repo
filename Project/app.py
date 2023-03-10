from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
import sqlite3
from library import encrypt_password
from library import check_password
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class database_handler:
    # Initialize the database
    def __init__(self, namedb: str):
        self.connection = sqlite3.connect(namedb)
        self.cursor = self.connection.cursor()

    # The default query function
    def run_query(self, query: str):
        self.cursor.execute(query)
        self.connection.commit()

    # Searching items in the database
    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    # Close the database connection
    def close(self):
        self.connection.close()

    # Table for user data
    def create_table_1(self):
        query = f"""CREATE TABLE if not exists users(
            id integer primary key,
            email text NOT NULL unique,
            password text NOT NULL,
            username text NOT NULL 
            )"""
        self.cursor.execute(query)
        self.connection.commit()

    # Table for entry data
    def create_table_2(self, namedb: str):
        query = f"""CREATE TABLE if not exists entries(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id integer NOT NULL,
            title text NOT NULL,
            question text NOT NULL,
            answer text,
            memo text
            )"""
        self.cursor.execute(query)
        self.connection.commit()

    # The function to add a new user to the database
    def enter_data_1(self, id, email, password, username):
        query = f"""INSERT INTO users(email, password, username) VALUES('{email}', '{password}', '{username}')"""
        self.run_query(query)

    # The function to add a new entry to the database
    def enter_data_2(self, user_id: int, title: str, question: str, answer: str, memo: str):
        query = f"INSERT INTO entries(user_id, title, question, answer, memo) VALUES('{user_id}', '{title}', '{question}', '{answer}', '{memo}')"
        self.cursor.execute(query)
        self.connection.commit()

    # The function to edit an existing entry in the database
    def update_data(self, entry_id: int, title: str, question: str, answer: str, memo: str):
        query = f"UPDATE entries SET title='{title}', question='{question}', answer='{answer}', memo = '{memo}' WHERE id = '{entry_id}'"
        self.cursor.execute(query)
        self.connection.commit()

    # The function to check if a user exists in the database and verify the password
    def test_login(self, email: str, password: str):
        db = database_handler("user_database.db")
        query = f'SELECT * FROM users WHERE email = "{email}"'
        result = self.cursor.execute(query).fetchall()
        id = 0
        username = None
        db.close()
        print(result)
        # Checking if the user exists
        if len(result) == 1:
            uname_check = True
            # Assigning all the values from the row to the variables
            id, email, hashed, username = result[0]
            # hashed = result[0][2]
            pass_check = check_password(password, hashed)

        else:
            uname_check = False
            pass_check = False

        print(result)
        return pass_check, uname_check, id, username


class LoginScreen(MDScreen):

    # User presses the login button
    def try_login(self):
        # Changing the state of the fields
        self.ids.passwd.error = False
        self.ids.uname.error = False
        print("User tried to login")
        self.user_id = 0
        username = ""
        # Get the input email and password
        email = self.ids.uname.text
        passwd = self.ids.passwd.text
        db = database_handler("user_database.db")
        # Get the necessary data from the try_login function
        pass_check, uname_check, user_id, username = db.test_login(email, passwd)

        if pass_check and uname_check:
            # Assigning the values to objects in other classes
            print(username)
            SelectionScreen.user = username
            EntryScreen.user_id = user_id
            DisplayScreen.username = username
            self.parent.current = "SelectionScreen"
            # Resetting the values
            self.ids.uname.text = ""
            self.ids.passwd.text = ""

        elif uname_check and not pass_check:
            # Making the error visible
            self.ids.passwd.error = True

        else:
            # Making the error visible
            self.ids.passwd.error = True
            self.ids.uname.error = True
            RegistrationScreen.show_popup(self, "Email error", "Email not found")
        print(self.user_id)


class RegistrationScreen(MDScreen):
    # Defining the variables
    uname = None
    passwd1 = None
    email = None
    passwd2 = None

    # User presses the register button
    def try_register(self):
        db = database_handler("user_database.db")
        print("User tried to register")
        # Get the registration details
        query = f"SELECT email FROM users"
        temp = db.search(query)
        email_list = []
        for i in temp:
            # Creating a list of emails
            email_list.append(i[0])
        # Getting the data from the fields
        self.uname = self.ids.uname.text
        self.email = self.ids.email.text
        self.passwd1 = self.ids.passwd1.text
        self.passwd2 = self.ids.passwd2.text

        # Code for not letting the same email enter twice
        if self.email not in email_list:
            # Validating user input
            if (self.passwd1 != self.passwd2) or (self.passwd1 == "") or (self.uname.strip() == "") or (self.email.strip() == ""):
                print("Failed")
                if self.uname.strip() == "":
                    # Username is empty
                    self.ids.uname.error = True
                    self.show_popup("Username error", "Username cannot be empty")
                    print("Username error")

                elif self.email.strip() == "":
                    # Email is empty
                    self.ids.email.error = True
                    self.show_popup("Email error", "Email cannot be empty")
                    print("Email error")

                elif self.passwd1 == "":
                    # Password is empty
                    self.ids.passwd2.error = True
                    self.ids.passwd1.error = True
                    self.show_popup("Password error", "Password cannot be empty")
                    print("Empty password")

                else:
                    # Passwords do not match
                    self.ids.passwd2.error = True
                    self.ids.passwd1.error = True
                    self.show_popup("Password error", "Passwords do not match")
                    print("Passwords do not match")

            else:
                print("Passed")
                hash = encrypt_password(self.passwd1)
                # Inserting the data to the database
                query = f"""INSERT INTO users(email, password, username) VALUES('{self.email}','{hash}', '{self.uname}')"""

                db.run_query(query)

                print("User registered successfully")

                # Resetting the fields
                self.ids.uname.text = ""
                self.ids.email.text = ""
                self.ids.passwd1.text = ""
                self.ids.passwd2.text = ""

                # Getting the id of the newly created user
                query = f"SELECT id FROM users WHERE email = '{self.email}'"
                temp_list = db.search(query)
                id = temp_list[0][0]
                EntryScreen.user_id = id
                print(id)
                db.close()

                # Assigning the username to the variables that will be used later
                SelectionScreen.user = self.uname
                DisplayScreen.username = self.uname
                self.parent.current = "SelectionScreen"


        # Error for existing user from the same email
        else:
            self.show_popup("Email error", "A user from this email already exists")

    def show_popup(self, title, message):
        # Create a dialog with the desired content
        dialog = MDDialog(
            title=title,
            text=message,
            size_hint=(0.7, 0.3),
            buttons=[
                MDFlatButton(
                    text="Close", on_release=lambda *args: dialog.dismiss()
                )
            ],
        )

        # Open the dialog
        dialog.open()


class EntryScreen(MDScreen):
    # Defining the variable
    user_id = None

    # Entering a new entry into the database
    def insert_data_to_function(self):
        # Getting the data from the fields
        title = self.ids.title.text
        question = self.ids.question.text
        answer = self.ids.answer.text
        memo = self.ids.memo.text

        if title.strip() == "" and question.strip() != "":
            # Only the title is empty
            self.ids.title.error = True
            RegistrationScreen.show_popup(self, "Title error", "Title cannot be empty")

        elif question.strip() == "" and title.strip() != "":
            # Only the question is empty
            self.ids.question.error = True
            RegistrationScreen.show_popup(self, "Question Error", "Question cannot be empty")

        elif title.strip() == "" and question.strip() == "":
            # Both title and question are empty
            self.ids.title.error = True
            self.ids.question.error = True
            RegistrationScreen.show_popup(self, "Error", "Title and Question cannot be empty")

        else:
            # Input is valid
            out_list = (title, question, answer, memo)
            user_id = self.user_id
            db = database_handler("user_database.db")
            # Sending the data to the database
            db.enter_data_2(user_id, title, question, answer, memo)
            # Resetting the fields
            self.ids.title.text = ""
            self.ids.question.text = ""
            self.ids.answer.text = ""
            self.ids.memo.text = ""
            # Visual Output for the user
            RegistrationScreen.show_popup(self, "Success", "Data inserted successfully")
            # Change the screen
            self.parent.current = "SelectionScreen"


class SelectionScreen(MDScreen):
    # Defining the variables
    user = None

    # Welcome message for the user
    def on_pre_enter(self, *args):
        self.ids.select_user_label.text = f"Welcome {self.user}!"
        print(self.user)

    pass


class TableScreen(MDScreen):
    pass
    data_table = None
    checked_rows = None

    # Inserting the table
    def on_pre_enter(self, *args):
        # Number of entries in the table
        db = database_handler("user_database.db")
        query = f"SELECT count(*) FROM entries WHERE user_id = {EntryScreen.user_id}"
        entrie_num = db.search(query)
        print(entrie_num)

        # before the screen is created, this code is run to create the MDDataTable
        self.data_table = MDDataTable(
            size_hint=(.8, .5),
            pos_hint={'center_x': .5, 'center_y': .5},
            use_pagination=False,
            check=True,
            # Defining how long the table is going to be
            rows_num = entrie_num[0][0],
            # Title of the columns
            column_data=[("id", 40),
                         ("user_id", 30),
                         ("Title", 33),
                         ("Question", 40),
                         ("Answer", 40),
                         ("Memo", 40)
                         ]
        )

        # Add the functions for events of the mouse
        self.data_table.bind(on_row_press=self.row_pressed)
        self.data_table.bind(on_check_press=self.check_pressed)
        self.add_widget(self.data_table)  # Add table to the GUI
        self.update()

    # Function for check pressed
    def check_pressed(self, table, current_row):
        print("A check was pressed", current_row)
        # Assigning the values for the DisplayScreen
        DisplayScreen.entry_id = current_row[0]
        DisplayScreen.title = current_row[2]
        DisplayScreen.question = current_row[3]
        DisplayScreen.answer = current_row[4]
        DisplayScreen.memo = current_row[5]

        self.checked_row = self.data_table.get_row_checks()
        self.parent.current = "DisplayScreen"

    # Function for an element pressed in the table
    def row_pressed(self, table, row):
        print("a row was pressed", row)
        # Changes the colour of the element in the table
        row.md_bg_color = "#ff0000"

    # Used for update the table
    def update(self):
        # Read database and update file
        db = database_handler("user_database.db")
        # Getting data that is unique to the user
        query = f"SELECT * FROM entries WHERE user_id = {EntryScreen.user_id}"
        data = db.search(query)
        db.close()
        self.data_table.update_row_data(None, data)


class DisplayScreen(MDScreen):
    entry_id = None  # class attribute
    title = None  # class attribute
    question = None  # class attribute
    answer = None  # class attribute
    memo = None  # class attribute
    username = None  # class attribute

    # Filling the fields of the DisplayScreen
    def on_pre_enter(self, *args):
        print(DisplayScreen.entry_id)
        # Changing the empty labels to previously user inputted data
        self.ids.display_main_label.text = f"{self.username}'s entry"
        self.ids.display_label_title.text = f"{DisplayScreen.title}"
        self.ids.display_label_question.text = f"{DisplayScreen.question}"
        self.ids.display_label_answer.text = f"{DisplayScreen.answer}"
        self.ids.display_label_memo.text = f"{DisplayScreen.memo}"

    # Delete the current record
    def delete_one(self):
        query = f"DELETE from entries where id = {DisplayScreen.entry_id}"
        db = database_handler("user_database.db")
        db.run_query(query)
        db.close()
        print(DisplayScreen.entry_id)
        self.parent.current = "TableScreen"

    # Edit the current record
    def edit_record(self):
        query = f"SELECT * FROM entries WHERE id = {DisplayScreen.entry_id}"
        db = database_handler("user_database.db")
        value_list = db.search(query)
        temp_list = []
        # Create a list that contains only "title, question, answer, memo"
        for i in range(2, 6):
            temp_list.append(value_list[0][i])
        # Assigning title, question, answer, memo
        title, question, answer, memo = temp_list
        db.close()

        # Assigning the previously found values to EntryEditScreen fields
        EntryEditScreen.title = title
        EntryEditScreen.question = question
        EntryEditScreen.answer = answer
        EntryEditScreen.memo = memo

        self.parent.current = "EntryEditScreen"


class EntryEditScreen(MDScreen):
    title = None
    question = None
    answer = None
    memo = None
    user_id_for_edit = EntryScreen.user_id
    print(memo)

    # Inserting data into the text fields before the screen is created
    def on_pre_enter(self, *args):
        self.ids.titleedit.text = f"{self.title}"
        self.ids.questionedit.text = f"{self.question}"
        self.ids.answeredit.text = f"{self.answer}"
        self.ids.memoedit.text = f"{self.memo}"

    # When the user presses the submit button
    def update(self):
        # Getting the data from the text fields
        title = self.ids.titleedit.text
        question = self.ids.questionedit.text
        answer = self.ids.answeredit.text
        memo = self.ids.memoedit.text

        if title == "" and question != "":
            # Only the title is empty
            self.ids.titleedit.error = True
            RegistrationScreen.show_popup(self, "Title error", "Title cannot be empty")

        elif question == "" and title != "":
            # Only the question is empty
            self.ids.questionedit.error = True
            RegistrationScreen.show_popup(self, "Question Error", "Question cannot be empty")

        elif title == "" and question == "":
            # Both title and question are empty
            self.ids.titleedit.error = True
            self.ids.questionedit.error = True
            RegistrationScreen.show_popup(self, "Error", "Title and Question cannot be empty")

        else:
            # No errors, data gets updated
            db = database_handler("user_database.db")
            db.update_data(DisplayScreen.entry_id, title, question, answer, memo)
            RegistrationScreen.show_popup(self, "Success", "Data updated successfully")
            self.parent.current = "TableScreen"

    pass


class app(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return


# Create tables
# db = database_handler("user_database.db")
# db.create_table_2(reg"entries")
# db.close()

x = app()
x.run()
