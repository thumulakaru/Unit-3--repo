# Quiz 36
## Code
```.py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        if not isinstance(self.name, str):
            raise ValueError("Name must be a string")
        return self.name

    def get_age(self):
        if not isinstance(self.age, int):
            raise ValueError("Age must be and integer")
        return self.age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student:Student):
        self.students.append(student)

    def remove_student(self, student:Student):
        if student not in self.students:
            raise ValueError("Student is not in the classroom")
        self.students.remove(student)

    def get_average_score(self):
        if len(self.students) == 0:
            raise ValueError("Classroom is empty")
        total = 0
        for student in self.students:
            total += student.get_grade()
            average = total / len(self.students)
        return average
```

## Evidence
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Quizzes/Quiz_036_result.png)

**Fig.1** Results of the test file

## UML Diagram
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Quizzes/Quiz_036_UML_diagram.png)

**Fig.2** UML diagram for the class
