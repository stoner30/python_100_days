"""
集合的方法
"""
set1 = {'Java', 'Python', 'C++', 'Kotlin'}
set2 = {'Kotlin', 'Swift', 'Java', 'Dart'}
set3 = {'HTML', 'CSS', 'JavaScript'}

# isdisjoint: 两个集合有相同元素返回False，否则返回True
print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))
