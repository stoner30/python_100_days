"""
集合的二元运算
"""
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}

# 交集
print(set1 & set2)
print(set1.intersection(set2))

# 并集
print(set1 | set2)
print(set1.union(set2))

# 差集
print(set1 - set2)
print(set1.difference(set2))
print(set2 - set1)

# 对称差
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

"""
还可以使用复合赋值运算

|= 等价于 set1.update(set2)
&= 等价于 set1.intersection_update(set2)
-= 等价于 set1.difference_update(set2)
^= 等价于 set1.symmetric_difference_update(set2)
"""
set1 ^= set2
print(set1)
