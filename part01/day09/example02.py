"""
双色球随机选号程序（代码优化+生成N注）
"""
import random

red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]

n = int(input('生成几注号码: '))
for _ in range(n):
    # 使用random.sample进行无回放随机采样
    selected_balls = random.sample(red_balls, 6)
    selected_balls.sort()
    for ball in selected_balls:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')

    # 使用random.choice随机抽取一个元素
    blue_ball = random.choice(blue_balls)
    print(f'\033[034m{blue_ball:0>2d}\033[0m')
