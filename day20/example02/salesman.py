from employee import Employee


class Salesman(Employee):
    """销售人员"""

    def __init__(self, name, sales=0):
        super().__init__(name)
        self.sales = sales

    def get_salary(self):
        """销售人员的薪资为底薪+提成的形式，底薪 1800 元，提成为加销售额的 5% """
        return 1800.0 + self.sales * 0.05
