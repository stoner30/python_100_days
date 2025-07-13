from employee import Employee


class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        """部门经理为固定薪资 15000"""
        return 15000.0
