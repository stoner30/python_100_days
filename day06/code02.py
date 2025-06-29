"""
从1到100的整数求和
"""
total = 0
for i in range(1, 101):
    total += i
print(f'{total}')

"""
从1到100的偶数求和
"""
total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print(f'{total}')

# 另一种使用控制起始数值和步长的写法
total = 0
for i in range(2, 101, 2):
    total += i
print(f'{total}')
