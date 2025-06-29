"""
计算三角形的周长和面积
"""
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

# 首先利用三角形定义判断是否为三角形
if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    print(f'周长: {perimeter:.2f}')

    # 这里用到了另一个三角形面积计算公式
    # 海伦公式:
    # 面积 = (周长 * (周长 - 边1) * (周长 - 边2) * (周长 - 边3)) 的平方根
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f'面积: {area:.2f}')

else:
    print('不能构成三角形')
