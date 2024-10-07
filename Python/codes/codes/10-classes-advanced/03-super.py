# super 사용 전
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email


class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        self.student_id = student_id



# super 사용 예시 - 단일 상속
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

class Student(Person):
    def __init__(self, name, age, number, email, student_id, gpa):
        super().__init__(name, age, number, email)
        self.student_id = student_id
        self.gpa = gpa
        


# super 사용 예시 - 다중 상속
class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')


class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')


class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__()
        self.value_c = 'CHild'


child1 = Child()
print(child1.value_a)
print(child1.value_c)
print(child1.value_b)  # AttributeError: 'Child' object has no attribute 'value_b'
