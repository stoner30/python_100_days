"""
输入半径计算圆的周长和面积
"""
import math

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * (radius ** 2)

print(f'圆的周长为: {perimeter: .4f}, 面积为: {area: .4f}')
