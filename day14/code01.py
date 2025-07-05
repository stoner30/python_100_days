"""
输入m和n，计算组合数C(m,n)的值
"""


def fac(num):
    result = 1
    for n in range(2, num + 1):
        result *= n
    return result


m = int(input('m = '))
n = int(input('n = '))
print(fac(m) // fac(n) // fac(m - n))
