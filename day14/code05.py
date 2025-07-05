def add(*args):
    """
    可变参数的函数定义

    用*表达式来表示args可以接受0个或任意多个参数
    调用函数时，传入的n个参数被封装成一个tuple并赋值给args
    如果没传入任何参数，args则为空元组
    """
    total = 0
    for val in args:
        if type(val) in (int, float):
            total += val
    return total


print(add())
print(add(1, 2, 3))
print(add(1, 2, 'hello', 4, 5.34))


def foo(*args, **kwargs):
    """
    关键字参数的函数定义

    **kwargs接收0或任意多个关键字参数，并将这些参数封装到字典中赋值给kwargs
    如果一个关键字参数都没被指定，则kwargs为空字典
    """
    print(args)
    print(kwargs)


foo(1, 2, 3, name='小李', age=43, married=False)
foo(name='小王')
