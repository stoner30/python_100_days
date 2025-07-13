"""
输入两个正整数求它们的最大公约数
"""
x = int(input('x = '))
y = int(input('y = '))

# for i in range(x, 0, -1):
#     if x % i == 0 and y % i == 0:
#         print(f'最大公约数: {i}')
#         break

# 上面的代码在执行效率上存在显著问题，比如x=99999998，y=99999999
# 下面代码采用了欧几里得算法来求最大公约数
while y % x != 0:
    x, y = y % x, x
    print(x, y)
print(f'最大公约数: {x}')
