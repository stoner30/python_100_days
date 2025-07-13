"""
静态方法和类方法
静态方法和类方法在调用时，都是通过 类.method() 的语法进行调用，唯一的区别就是注解和参数的不同
"""


class Triangle(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a

    # @classmethod
    # def is_valid(cls, a, b, c):
    #     """
    #     类方法的定义
    #     因为要避免同名方法，所以在测试时可以注释掉同名静态方法
    #     """
    #     return a + b > c and a + c > b and b + c > a

    """
    @propery 注解，对于没有参数的方法，可以进行简化，在调用时通过 instance.property 即可。
    """

    @property
    def perimeter(self):
        """周长"""
        return self.a + self.b + self.c

    @property
    def area(self):
        """
        面积
        使用海伦公式
        p = (a + b + c) / 2，也就是半周长
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5，也就是半周长与三边差的乘积再进行开方操作
        """
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if Triangle.is_valid(a, b, c):
    triangle = Triangle(a, b, c)
    print(f'周长: {triangle.perimeter:.2f}')
    print(f'面积: {triangle.area:.2f}')
else:
    print('无法构成三角形')
