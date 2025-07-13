from employee import Employee


class Programmer(Employee):
    """程序员"""

    def __init__(self, name, hours=0):
        super().__init__(name)
        self.hours = hours

    def get_salary(self):
        """程序员以工时计算薪资，每小时 200 元"""
        return 200.0 * self.hours
