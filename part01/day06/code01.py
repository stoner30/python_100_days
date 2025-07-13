"""
每隔1秒输出一次“hello, world”，持续1小时
"""
import time

for _ in range(3600):
    print('hello world')
    time.sleep(1)  # 进程暂停1s
