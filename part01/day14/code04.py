from random import randrange


def roll_dice(n=2):
    """
    投骰子的函数
    :param n: 投掷次数
    :return: 点数和
    """
    total = 0
    for _ in range(n):
        total += randrange(1, 7)
    return total


# 如果没有指定数字，那默认投2次骰子
print(roll_dice())
# 传入参数时则不使用默认值
print(roll_dice(3))
