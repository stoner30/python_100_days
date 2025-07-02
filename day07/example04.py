"""
百钱百鸡问题（穷举法）
"""
for x in range(0, 21):
    for y in range(0, 34):
        for z in range(0, 100, 3):
            if x + y + z == 100 and 5 * x + 3 * y + z // 3 == 100:
                print(f'公鸡: {x}, 母鸡: {y}, 小鸡: {z}')

# 另一种减少循环层数的写法
for x in range(0, 21):
    for y in range(0, 34):
        z = 100 - x - y
        if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
            print(f'公鸡: {x}, 母鸡: {y}, 小鸡: {z}')
