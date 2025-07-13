import time


class Clock:
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        """初始化方法"""
        self.hour = hour
        self.minute = minute
        self.second = second

    def run(self):
        """时钟走时"""
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        """显示时间"""
        return f'{self.hour:0>2d}:{self.minute:0>2d}:{self.second:0>2d}'


# 创建时钟对象
clock = Clock(23, 59, 15)
while True:
    print(clock.show())
    time.sleep(1)
    clock.run()
