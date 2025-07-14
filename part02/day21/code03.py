"""自定义异常"""
from functools import lru_cache


class InputError(ValueError):
    pass


@lru_cache
def fac(number):
    """求阶乘"""
    if number < 0:
        raise InputError('只能计算非负整数的阶乘')
    elif number in (0, 1):
        return 1
    return number * fac(number - 1)


flag = True
while flag:
    try:
        num = int(input('n = '))
        print(f'{num}! = {fac(num)}')
        flag = False
    except InputError as e:
        print(e)
