# Unit 3: A journal for math Questions
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Project/Client.gif)

**Fig.1** My client being frustrated with manual journals

## Criteria A: Planning

## Problem definition
The client wants a journal to write down math questions that he find. He wants to edit them later if he thinks there's an addition to the question. He wants a login system for the journal and wants to change the details that he enters when he registers for the first time. Also he want to add the answers of the questions once he find them.

## Proposed Solution
Considering the clients requirements a GUI application seems to be the best option. For this I decided to use Python as a programming language since it is able to run on multiple platforms[^1].For GUI development kivymd would be very suitable as this GUI framework is structured in object-oriented format which makes the development easy[^2]. SQLite is used to manage user inputted data as it is an embedded, serverless relational database which means the program and the database can be both localized.[^3]

[^1]: Python Geeks. “Advantages of Python: Disadvantages of Python.” Python Geeks, 26 June 2021, https://pythongeeks.org/advantages-disadvantages-of-python/.
[^2]: Gupta, Kaustubh. “What Is KivyMD: Creating Android Machine Learning Apps Using KivyMD.” *Analytics Vidhya*, 6 July 2021, https://www.analyticsvidhya.com/blog/2021/06/creating-android-ml-app-kivymd/#:~:text=KivyMD%20is%20built%20on%20the.
[^3]: S, Ravikiran A. “What Is Sqlite? and When to Use It?” *Simplilearn.com*, Simplilearn, 16 Feb. 2023, https://www.simplilearn.com/tutorials/sql-tutorial/what-is-sqlite.

## Success Criteria
1. The journal should have a login/registration system.
2. The journal should be able to record math questions with a title, an answer and a memo.
3. The user should be able to view and edit journal entries later.
4. The journal entries will be displayed separately to each user.
5. The GUI should have a dark theme.
6. All the inputting data has to go through validation inorder to stop the user from entering a blank entry.
7. There should be pop up screens.


# Criteria B: Design

## System Diagram
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Project/Sys_diagram.drawio.png)

**Fig.2** System Diagram 

## ER Diagram
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Project/ER_diag.png)

**Fig.3** ER Diagram 

## UML Diagram
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Project/UML_diag.png.png)

**Fig.4** UML Diagram

## Wireframe Diagram
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Project/Wireframe_diag.png.png)

**Fig.5** Wireframe Diagram

## Flow Diagrams
### Login Function
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Project/login_function_flow_diag.png.png)

**Fig.6** Flow diagram for the login function 

### Registration Function
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Project/_Registration_flow_diag.drawio.png)

**Fig.7** Flow diagram for the registration function

### Insert data
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Project/Insert_data_to_flow_diag.drawio.png)

**Fig.8** Flow diagram for entering a new entry into the table

## Record of Tasks
| Task No | Planned Action                                 | Planned Outcome                                         | Time estimate | Target completion date | Criterion |
|---------|------------------------------------------------|---------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Meet the client                                | Have an idea about what the client wants                | 10 mins       | 2023 Feb 1             | A         |
| 2       | Write the problem definition                   | Have a clear idea of what the client wants              | 10 mins       | 2023 Feb 4             | A         |
| 3       | Write the success criteria                     | Have a clear conclusion of what the client wants        | 5 mins        | 2023 Feb 10            | A         |
| 4       | Write the proposed solution                    | Write how the program is going to be built              | 10 mins       | 2023 Feb 19            | A         |
| 5       | Meet the client                                | Confirm on the final solution                           | 10 mins       | 2023 Feb 20            | A         |
| 6       | Write the proposed solution                    | Explain what I'm going to be working on                 | 8 mins        | 2023 Feb 23            | A         |
| 7       | Draw System Diagram                            | To have a better understanding about the system         | 10 mins       | 2023 Feb 28            | B         |
| 8       | Draw ER Diagram                                | Understand the database clearly                         | 20 mins       | 2023 Feb 28            | B         |
| 9       | Draw UML Diagram                               | Understand classes in the program                       | 30 mins       | 2023 Feb 28            | B         |
| 10      | Draw Wireframe Diagram                         | Understand the screens in the GUI                       | 45 mins       | 2023 Feb 28            | B         |
| 11      | Draw Flow Diagram for login                    | Understand the process of login                         | 30 mins       | 2023 Feb 28            | B         |
| 12      | Draw Flow Diagram for inserting data           | Understand the process of inserting data into the table | 20 mins       | 2023 Feb 28            | B         |
| 13      | Draw the Flow Diagram for a user registration  | Understand the process of registering a user            | 20 mins       | 2023 Feb 28            | B         |
| 14      | Coding LoginScreen                             | Finish coding the LoginScreen                           | 15 mins       | 2023 Mar 2             | C         |
| 15      | Alligning elements in the kivyscreen           | Finish allignments in LoginScreen                       | 30 mins       | 2023 Mar 2             | C         |
| 16      | Coding RegistrationScreen                      | Finish coding the RegistrationScreen                    | 20 mins       | 2023 Mar 2             | C         |
| 17      | Alligning elements in the kivyscreen           | Finish allignments in RegistrationScreen                | 20 mins       | 2023 Mar 2             | C         |
| 18      | Coding SelectionScreen                         | Finish coding the SelectionScreen                       | 15 mins       | 2023 Mar 2             | C         |
| 19      | Alligning elements in the kivyscreen           | Finish allignments in SelectionScreen                   | 10 mins       | 2023 Mar 2             | C         |
| 20      | Coding the EntryScreen                         | Finish coding the EntryScreen                           | 20 mins       | 2023 Mar 2             | C         |
| 21      | Alligning elements in the kivyscreen           | Finish allignments in EntryScreen                       | 60 mins       | 2023 Mar 2             | C         |
| 22      | Coding the pre_enter of TableScreen            | Finish the pre_enter function                           | 60 mins       | 2023 Mar 3             | C         |
| 23      | Coding the rest of TableScreen                 | Finish coding the rest of TableScreen                   | 20 mins       | 2023 Mar 3             | C         |
| 24      | Allignments for the TableScreen                | Finish the allignments for the TableScreen              | 15 mins       | 2023 Mar 3             | C         |
| 25      | Coding the DisplayScreen                       | Finish coding the DisplayScreen                         | 30 mins       | 2023 Mar 3             | C         |
| 26      | Alligning elements in the kivyscreen           | Finish the allignments of DisplayScreen                 | 20 mins       | 2023 Mar 3             | C         |
| 27      | Coding the EntryEditScreen                     | Finish coding the EntryEditScreen                       | 30 mins       | 2023 Mar 3             | C         |
| 28      | Alligning the elements in the  kivyscreen      | Finish the allignments of EntryEditScreen               | 45 mins       | 2023 Mar 3             | C         |
| 29      | Coding the popup dialogs                       | Finish the dialogs                                      | 60 mins       | 2023 Mar 3             | C         |
| 30      | Finalise the program                           | Finish coding the program                               | 1 hr          | 2023 Mar 4             | C         |
| 31      | Adding colours to the GUI                      | Have a pleasant and clear user interface                | 3 hrs         | 2023 Mar 5             | C         |
| 32      | Record and upload the video                    | Finish the entire project                               | 1 hr          | 2023 Mar 10            | C         |

## Test Plan
| Type                | Description                               | Process                                                                                                                                                                                                                                                                                                          | Anticipated Outcome                                                                                                                                              |
|---------------------|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unit Testing        | User Registration                         | 1. Run app.py file<br>2. Click the Register button on the application screen<br>3. Input the appropriate information in each textfield following the hint text<br>4. Click Register                                                                                                                              | After clicking register the user will be directed to a screen with a welcome <br>message                                                                         |
| Unit Testing        | User Login                                | 1. Run app.py file<br>2. Input the appropriate information in each textfield following the hint text<br>3. Click Login                                                                                                                                                                                           | If the information is correct the user will be greeted with a welcome message.<br>If the information are incorrect the relevant fields will be displayed in red. |
| Unit Testing        | Logout                                    | 1. Run app.py file<br>2. Login to an existing user<br>3. Click the Logout button                                                                                                                                                                                                                                 | The user will be displayed the login screen with empty text fields and hint <br>texts.                                                                           |
| Integration Testing | Login and Registration                    | 1. Run app.py file<br>2. Click the Register button on the application screen<br>3. Enter the data as guided by the hint text<br>4. Click Register<br>5. Click logout in the new screen<br>6. Try login with the same credentials registered                                                                      | If the user entered correct data according to the instructions shown in the GUI <br>they should be able to login without a problem                               |
| Unit Testing        | Adding New Entry                          | 1. Run app.py file<br>2. Login with previously registered credentials<br>3. Click "New Entry" on the selection screen<br>4. Input data into the appropriate fields                                                                                                                                               | If the data were inputted correctly according to the hint texts the user should<br>be directed to the home screen again                                          |
| Unit Testing        | Viewing Entries                           | 1. Run app.py file.<br>2. Login with previously registered credentials.<br>3. Click view all entries in the selection screen.<br>4. Click the checkbox that the user wants to see.<br>5. Click the "Delete" button.                                                                                              | The selected entry should be removed from the table                                                                                                              |
| Unit Testing        | Editing Entries                           | 1. Run app.py file.<br>2. Login with previously registered credentials.<br>3. Click view all entries in the selection screen.<br>4. Click the checkbox that the user wants to see.<br>5. Click the "Edit" button.<br>6. Enter the data according to the hint text.<br>7. Click "submit".                         | If the data is entered properly according to the hint texts the user should be<br>able to see the modified entries.                                              |
| Integration Testing | Editing a present<br>entry and viewing it | 1. Run app.py file.<br>2. Login with previously registered credentials.<br>3. Click view all entries in the selection screen.<br>4. Click the checkbox that the user wants to see.<br>5. Click the "Edit" button.<br>6. Enter the data according to the hint text.<br>7. In the new screen click the same entry. | The user should be able to view the newly editted entry with the new data.                                                                                       |
| Code Review         | Reviewing Code                            | Reading the entire code and removing unused variables and renaming some <br>variables and adding comments to parts when necessary.                                                                                                                                                                               | Easy to understand and easy to debug code for future development.                                                                                                |

# Criteria C: Development

## Existing tools
| Software/Development Tools | Coding Structure Tools       | Libraries  |
|----------------------------|------------------------------|------------|
| PyCharm                    | OOP Structures(Classes)      | kivymd.app |
| Python                     | SQL requests                 | Passlib    |
| SQLite                     | Databases                    | sqlite     |
| KivyMD                     | Encryption                   | kivymd.uix |
| Tabnine AI code completion | For Loops                    |            |
|                            | If-then-else statements      |            |
|                            | ORM(Object Relation Mapping) |            |

## List of techniques used
1. Object Oriented Programming(OOP)
2. KivyMD.app Library
3. KivyMD.uix Library
4. For loops
5. if statements
6. Password Hashing
7. Interacting with Databases
8. Lists


## Development
### Computational Thinking
#### Decomposition
Decomposition in Computational Thinking refers to breaking a complex problem or system into parts that are easier to conceive, understand, program, and maintain. In this project one of the key things was to display user entries uniquely to each user. As this was a complex process I first focused on making the table in the database easier to access for the developer by having a one to one relationship with the users table. After that I wrote a query to get data from the table while sorting them through the user id. Finally since the row numbers have a limit I decided to get the count of data that the user has entered.

##### Create the table
```.py
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
```

##### Get the data for the table
```.py
    def update(self):
        # Read database and update file
        db = database_handler("user_database.db")
        # Getting data that is unique to the user
        query = f"SELECT * FROM entries WHERE user_id = {EntryScreen.user_id}"
        data = db.search(query)
        db.close()
        self.data_table.update_row_data(None, data)
```

##### Number of rows

```.py
db = database_handler("user_database.db")
        query = f"SELECT count(*) FROM entries WHERE user_id = {EntryScreen.user_id}"
        entrie_num = db.search(query)
```

```.py
# Defining how long the table is going to be
            rows_num = entrie_num[0][0],
```

#### Pattern Recognition
Pattern recognition is the process of identifying patterns or regularities in data, while generalization is the ability to infer relationships between different patterns based on observed similarities. Abstraction involves distilling essential features or characteristics from a set of data so that it can be used to represent a more general concept. In computer science, these concepts are used in various technologies such as machine learning, natural language processing, and image recognition.

In this program I identified how the popup messages are repititive which had a pattern from which I was able to write a general function for all the popup messages which helped me to reduce the length of my code.

##### Popup messages

##### Before
```.py
class RegistrationScreen(MDScreen):
    def show_popup_uname_error(self):
        # Create a dialog with the desired content
        dialog = MDDialog(
            title="Username error",
            text="Username cannot be empty",
            size_hint=(0.7, 0.3),
            buttons=[
                MDFlatButton(
                    text="Close", on_release=lambda *args: dialog.dismiss()
                )
            ],
        )
      
    def show_popup_email_error(self):
        # Create a dialog with the desired content
        dialog = MDDialog(
            title="Email error",
            text="Email cannot be empty",
            size_hint=(0.7, 0.3),
            buttons=[
                MDFlatButton(
                    text="Close", on_release=lambda *args: dialog.dismiss()
                )
            ],
        )
    def show_popup_pwd_empty(self):
        # Create a dialog with the desired content
        dialog = MDDialog(
            title="Password error",
            text="Password cannot be empty",
            size_hint=(0.7, 0.3),
            buttons=[
                MDFlatButton(
                    text="Close", on_release=lambda *args: dialog.dismiss()
                )
            ],
        )
    def show_popup_pwd_error(self):
        # Create a dialog with the desired content
        dialog = MDDialog(
            title="Password error",
            text="Passwords do not match",
            size_hint=(0.7, 0.3),
            buttons=[
                MDFlatButton(
                    text="Close", on_release=lambda *args: dialog.dismiss()
                )
            ],
        )
```

###### After
```.py
class RegistrationScreen(MDScreen):    
    def show_popup(self, title, messaI fge):
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
    # The code has been reduced for demonstration purposes    
    self.show_popup("Username error", "Username cannot be empty")
    self.show_popup("Email error", "Email cannot be empty")
    self.show_popup("Password error", "Password cannot be empty")
    self.show_popup("Password error", "Passwords do not match")
```
### Developing
#### OOP
OOP stands for Object-Oriented Programming. It is a programming paradigm that emphasizes the use of objects and classes to represent and manipulate data. In OOP, objects are instances of classes, which are defined as a blueprint or template for creating objects. OOP offeres many benefits such as modularity(reusable code for easy management) and Encapsuation(hiding implementation details for better security), Inheritance(for reduced duplication). Following is an example of OOP in my program.
```.py
class database_handler():
  def __init__(self, namedb: str):
  # code omitted for display of OOP structures

  def run_query(self, query: str):
  # code omitted for display of OOP structures

  def search(self, query):
  # code omitted for display of OOP structures

  def close(self):
  # code omitted for display of OOP structures

  def create_table_1(self):
  # code omitted for display of OOP structures

  def create_table_2(self, namedb: str):
  # code omitted for display of OOP structures

  def enter_data_1(self, id, email, password, username):
  # code omitted for display of OOP structures

  def enter_data_2(self, user_id: int, title: str, question: str, answer: str, memo: str):
  # code omitted for display of OOP structures

  def update_data(self, entry_id: int, title: str, question: str, answer: str, memo: str):
  # code omitted for display of OOP structures

  def test_login(self, email: str, password: str):
  # code omitted for display of OOP structures
```

Some of this code is used throughout the program to query data from the tables which made my program efficient as I was not using the same code over and over again.

#### Key KivyMD elements used
##### MDScreen
MDScreen is used to create a different screens within the application.The different screens can be managed by the ScreenManager in kivy md. The examples of MDScreens and MDScreen manager is shown below:
```.kv
ScreenManager:
    LoginScreen:
        name:"LoginScreen"

    RegistrationScreen:
        name:"RegistrationScreen"

    EntryScreen:
        name:"EntryScreen"

    SelectionScreen:
        name:"SelectionScreen"

    TableScreen:
        name:"TableScreen"

    DisplayScreen:
        name:"DisplayScreen"

    EntryEditScreen:
        name:"EntryEditScreen"
        
<DisplayScreen>:
```

##### MDBoxLayout, MDCard and MDRaisedButton
MDBoxLayout is a versatile layout function that enables developers to position widgets in a specific arrangement, either vertically or horizontally. And MDCard is also really similar to MDBoxLayout. Both are commonly used to organize multiple widgets, such as buttons, labels, and images, into a cohesive layout. MDBoxLayout,MDCard is highly customizable, making it easy to tailor the layout to specific design needs. On the other hand, "MDRaisedButton"s are specialized button widgets that facilitate user interaction with the application. Here are some examples of MDBoxLayout, MDCard and MDButtons in my code.

##### MDCard

```.kv
MDCard:
        size_hint:.6, .8
        pos_hint: {"center_x":.5, "center_y":.5}
        orientation:"vertical"
```

##### MDBoxLayout

```.kv
MDBoxLayout:
    size_hint:1, .2
```

##### MDButtons

```.kv
MDRaisedButton:
    id:login
    text:"Login"
    on_press: root.try_login()
    md_bg_color: "#b24403"
    size_hint: .5, .25
```

##### MDDataTable
MDDataTable can be used to display data in a table. I used this to display all entries that belonged to a certain user.
```.kv
db = database_handler("user_database.db")
        query = f"SELECT count(*) FROM entries WHERE user_id = {EntryScreen.user_id}"
        entrie_num = db.search(query)
        # print(entrie_num)

        # before the screen is created, this code is run
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
```

##### MDDialog
This opens a popup dialog which has a title and a message. I used to this to give out output on several screens. Here is an example in my code.
```.py
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
        
self.show_popup("Email error", "A user from this email already exists")
```

#### Key functions within the app
##### Login function
This code is used to verify the password of an existing user. And if the details do not match with the details in the database errors are shown. If only the password is wrong the text field will be displayed in red. If the email is wrong a popup screen will show and state the error. If the entered data is correct username and user_id are queried and assigned to objects in different classes. The code for the function is displayed below.
```.py
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
```

##### Insert data into the table
This code is used to enter a new entry into the table. This code validates the title and question to not to be empty and if the user were not to enter the data properly popup screens will showup explaining the error to the user. Also the object user_id is inherited from the class LoginScreen or RegistrationScreen.
```.py
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
```

##### Edit entered data
This is one of the important parts of the code as it reads data from the database, displays them for the user and let the user edit them and validated by the code to avoid errors. Most of the objects in this code are inherited from another class which also shows how effective using classes are. In this code by using the pre_enter function I display the previously entered data by the user to enable editting them. And when the user decides to submit the data all the data is validated and the errors are displayed through popup screens.
```.py
class EntryEditScreen(MDScreen)
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
            RegistrationScreen.show_popup("Success", "Data updated successfully")
            self.parent.current = "TableScreen"
```

A special thanks to Olivia Leung, class of 2025 for the design of the GUI.
# Criteria D: Functionality

## Project Demonstration
[Link for the video](https://drive.google.com/file/d/1VSOciE6K-yTsEfyFTkOiwJUjVxxM9YoE/view?usp=share_link)

## Appendix
### Client agreement
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Project/Client_agreenment.jpg)

**Fig.9** An image of the client agreement

