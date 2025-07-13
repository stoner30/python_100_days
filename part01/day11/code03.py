"""
编码和解码
"""
a = '小绿'
b = a.encode('utf-8')
c = a.encode('gbk')
print(b)
print(c)

e = b.decode('utf-8')
f = c.decode('gbk')
print(e)
print(f)
