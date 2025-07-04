"""
双色球随机选号程序
"""
import random

red_balls = list(range(1, 34))
selected_balls = []

# 添加6个红色球到选中列表
for _ in range(6):
    index = random.randrange(len(red_balls))
    # 使用pop将index索引处的红球取出，并放入已选号码中
    selected_balls.append(red_balls.pop(index))

# 对选中的红球进行排序
selected_balls.sort()

for ball in selected_balls:
    print(f'\033[031m{ball:0>2d}\033[0m', end=' ')

# 随机选择一个蓝色球
blue_ball = random.randrange(1, 17)
print(f'\033[034m{blue_ball:0>2d}\033[0m')
