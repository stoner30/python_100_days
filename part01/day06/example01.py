"""
输入一个大于1的正整数判断它是不是素数
"""
num = int(input('请输入一个正整数: '))
# 不需要一直循环到num，只需要循环到num的平方根即可，因为因数都是成对出现，如36的因数
# 1、36
# 2、18
# 3、12
# 4、9
# 6、6
end = int(num ** 0.5)

is_prime = True
for i in range(2, end + 1):
    if num % i == 0:
        is_prime = False
        break

print('%d%s素数' % (num, '是' if is_prime else '不是'))
