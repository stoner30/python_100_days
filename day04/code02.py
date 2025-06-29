"""
赋值运算符和复合赋值运算符
"""
a = 10
b = 3
a += b
a *= a + 2
print(a)

"""
海象运算符
"""
# 错误的实例: SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
# print((a = 10))
print((a := 10))
print(a)
