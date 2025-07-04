"""
将一颗色子掷6000次，统计每种点数出现的次数
"""
import random

counters = [0] * 6
for _ in range(60000):
    face = random.randrange(1, 7)
    counters[face - 1] += 1

for face in range(1, 7):
    print(f'{face}出现了{counters[face - 1]}次')
