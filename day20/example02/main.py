from manager import Manager
from programmer import Programmer
from salesman import Salesman

emps = [Manager('刘备'), Programmer('诸葛亮'), Manager('曹操'), Programmer('荀彧'), Salesman('张辽')]
for emp in emps:
    if isinstance(emp, Programmer):
        working_hours = int(input(f'请输入{emp.name}本月工作时间: '))
        emp.hours = working_hours
    elif isinstance(emp, Salesman):
        sales = float(input(f'请输入{emp.name}本月销售额: '))
        emp.sales = sales

    print(f'{emp.name}本月工资为: ¥{emp.get_salary():.2f}元')
