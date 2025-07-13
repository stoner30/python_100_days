"""继承和多态"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}正在吃饭')

    def sleep(self):
        print(f'{self.name}正在睡觉')


class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title

    def teach(self, course_name):
        print(f'{self.name}{self.title}正在教授{course_name}')


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def learn(self, course_name):
        print(f'{self.name}正在学习{course_name}')


teacher = Teacher('安西', 70, '教练')
student = Student('樱木花道', 16)

teacher.sleep()
student.sleep()
teacher.eat()
student.eat()
teacher.teach('定点跳投')
student.learn('定点跳投')
