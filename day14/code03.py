def make_judgement(a, b, c):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and a + c > b and b + c > a


print(make_judgement(1, 2, 3))
print(make_judgement(4, 5, 6))

print(make_judgement(a=1, b=2, c=3))

"""
可以使用/强制位置参数
def make_judgement(a, b, c, /):
    pass
    
但是如下这样调用就会提示错误
make_judgement(a=1, b=2, c=3)
> TypeError: make_judgement() got some positional-only arguments passed as keyword arguments: 'a, b, c'
"""

"""
可以使用*来强制使用命名参数
def make_judgement(*, a, b, c):
    pass

如下方式调用也会提示错误
make_judgement(1, 2, 3)
> TypeError: make_judgement() takes 0 positional arguments but 3 were given
"""
