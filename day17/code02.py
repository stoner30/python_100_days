"""
递归
"""
import time
from functools import lru_cache


@lru_cache()
def fib1(num):
    """
    使用递归方式进行斐波那契数列的计算

    备注：
    - 未使用lru_cache引入缓存机制前，打印前50个斐波那契数列耗费了2596秒，合43分钟……
    - 使用lru_cache后，打印同样数量的斐波那契数列耗费了6.508827209472656e-05s，相差相当多……
    """
    if num in (1, 2):
        return 1
    return fib1(num - 1) + fib1(num - 2)


def fib2(num):
    """
    使用循环和交换变量的方式进行斐波那契数列的计算

    备注：
    使用循环及交换变量的方式计算前50个斐波那契数列，耗时8.082389831542969e-05s，与引入缓存机制
    的递归调用相差无几。
    """
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
    return a


start = time.time()
for i in range(1, 51):
    print(fib2(i))
print(f'执行时间: {time.time() - start}s')
