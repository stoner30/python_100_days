"""
输入年份，闰年输出True，平年输出False
闰年的判断规则为：
1. 年份是4的倍数但不是100的倍数
2. 年份是400的倍数
"""
year = int(input('请输入年份: '))
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print('%d年为%s' % (year, '闰年' if is_leap else '平年'))
