"""
装饰器
"""
import random
import time

from functools import wraps


def record_time(func):
    """
    定义装饰器函数，实现记录函数执行时间的功能
    借助@wraps装饰器来保存原函数

    :param func: 实际要执行的函数
    :return: 被包装后的新函数
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__}执行时间: {end_time - start_time:.2f}秒')
        return result

    return wrapper


# 使用语法糖的形式调用装饰器函数

@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')


@record_time
def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')


# 调用装饰器函数，会记录函数执行时间
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')

# 如果想取消装饰器的功能，可以借助__wrapped__参数
download.__wrapped__('MySQL从删库到跑路.avi')
upload.__wrapped__('Python从入门到住院.pdf')
