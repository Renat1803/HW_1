class Person:
    def __init__(self, fullname, age, is_married):
        self.__fullname = fullname
        self.__age = age
        self.__is_married = is_married

    def introduce_myself(self, fullname, age, is_married):
        print(f'fullname: {fullname} \n age: {age} \n is_married: {is_married} \n')

class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self, fullname, age, is_married):
        print(f'fullname: {fullname} \n age: {age} \n is_married: {is_married} \n')

    def output(self):
        return f'fullname {self.fullname} \n age {self.age}\n is_married {self.is_married}\n'


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        Person.__init__(self, fullname, age, is_married)
        self.marks = marks

    def average_rating(self, ):
        print(sum(self.marks) / 5)


class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience=3):
        Person.__init__(self, fullname, age, is_married)
        self.experience = experience
        self.salary = 30000

    def Teacher_wage(self):
        if self.experience > 3:
            new_salary = self.salary + (self.salary / 100 * 5) * (self.experience - 3)
            return new_salary


Man = Teacher('Peter', 25, 'not married', 4)
print(f'{Man.fullname}, {Man.age} years old ,{Man.is_married}, '
      f'work experience {Man.experience} ')
print(Man.Teacher_wage())

def create_students():
    student_1 = Student(fullname="Fedor", age=16, is_married='not married', marks={
        "Русский язык": 5,
        "Алгебра": 4,
        "Химия": 5,
        "Физика": 2,
        "Английский язык": 3,
    })
    student_2 = Student(fullname="Manas", age=17, is_married='not married', marks={
        "Русский язык": 5,
        "Алгебра": 5,
        "Химия": 4,
        "Физика": 4,
        "Английский язык": 3,
    })
    student_3 = Student(fullname="Jack", age=17, is_married='not married', marks={
        "Русский язык": 4,
        "Алгебра": 4,
        "Химия": 3,
        "Физика": 4,
        "Английский язык": 4,
    })

    results = student_1, student_2, student_3
    return results

students = create_students()
for i in students:
    list = []
    for marks in i.marks.values():
        list.append(marks)
    print(f'Name: {i.fullname}\n age: {i.age}\n is_married: {i.is_married}\n'
          f'Average marks: {sum(list) / len(list)}\n')