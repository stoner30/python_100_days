"""
动态属性
"""


class Person:
    """
    如果不希望从外部设置动态属性，可以使用__slots__定义有效属性
    """

    # __slots__ = ('name', 'age', )

    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("John", 18)
# 禁用动态属性设置时，设置属性的话则会提示 AttributeError: 'Person' object has no attribute 'sex'
person.sex = '男'
print(person.sex)
