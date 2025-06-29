"""
变量的类型转换操作
"""
a = 100
b = 123.45
c = '123'
d = '100'
e = '123.45'
f = 'hello world'
g = True
print(float(a))
print(int(b))
print(int(c))
print(int(c, base=16))  # 把'123'当成16进制字符串并转换成10进制的整型
print(int(d, base=2))  # 把'100'当成2进制字符串并转换成10进制的整型
print(float(e))
print(bool(f))
print(int(g))
print(chr(a))
print(ord('d'))
