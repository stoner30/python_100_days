"""
比较创建list和tuple的性能
"""
import timeit

print('%.3f秒' % timeit.timeit('[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))
print('%.3f秒' % timeit.timeit('(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))
