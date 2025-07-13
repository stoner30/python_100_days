from enum import Enum


class Suite(Enum):
    """花色，使用枚举进行定义"""
    SPADE, HEART, CLUB, DIAMOND = range(4)


for suite in Suite:
    print(f'{suite}: {suite.value}')
