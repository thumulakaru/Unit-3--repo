# Unit 3: A journal for math Questions

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
7. There should be pop up screens for the user registration.


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

## Record of Tasks
| Task No | Planned Action                        | Planned Outcome                                          | Time estimate | Target completion date | Criterion |
|---------|---------------------------------------|----------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Meet the client                       | Have an idea about what the client wants                 | 10 mins       | 2023 Feb 1             | A         |
| 2       | Write the problem definition          | Have a clear idea of what the client wants               | 10 mins       | 2023 Feb 4             | A         |
| 3       | Write the success criteria            | Have a clear conclusion of what the client wants         | 5 mins        | 2023 Feb 10            | A         |
| 4       | Write the proposed solution           | Write how the program is going to be built               | 10 mins       | 2023 Feb 19            | A         |
| 5       | Meet the client                       | Confirm on the final solution                            | 10 mins       | 2023 Feb 20            | A         |
| 6       | Write the proposed solution           | Explain what I'm going to be working on                  | 8 mins        | 2023 Feb 23            | A         |
| 7       | Draw System Diagram                   | To have a better understanding about the system          | 10 mins       | 2023 Feb 28            | B         |
| 8       | Draw ER Diagram                       | Understand the database clearly                          | 20 mins       | 2023 Feb 28            | B         |
| 9       | Draw UML Diagram                      | Understand classes in the program                        | 30 mins       | 2023 Feb 28            | B         |
| 10      | Draw Wireframe Diagram                | Understand the screens in the GUI                        | 45 mins       | 2023 Feb 28            | B         |
| 11      | Draw Flow Diagram for login           | Understand the process of login                          | 30 mins       | 2023 Feb 28            | B         |
| 12      | Draw Flow Diagram for inserting data  | Understand the process of inserting data into  the table | 20 mins       | 2023 Feb 28            | B         |
| 13      | Draw the Flow Diagram for x           | Understand the process of x                              | 20 mins       | 2023 Feb 28            | B         |
| 14      | Coding the main program. 1st  half    | Finish atleast half the program                          | 3 hrs         | 2023 Mar 2             | C         |
| 15      | Coding the main program. 2nd hald     | Finish the entire program                                | 2 hrs         | 2023 Mar 3             | C         |
| 16      | Minor bug fixes and small validations | Get rid of minor bugs                                    | 1 hr          | 2023 Mar 4             | C         |
| 17      | Adding colours to the GUI             | Have a pleasant and clear user interface                 | 3 hrs         | 2023 Mar 5             | C         |

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

## Development


# Criteria D: Functionality
