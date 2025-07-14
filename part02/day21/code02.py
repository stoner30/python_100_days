"""异常处理机制"""
file = None

try:
    file = open('./res/致橡树.txt', 'r', encoding='utf-8')
    print(file.read())
except FileNotFoundError:
    # 修改为错误的文件名
    print(f'无法打开文件')
except LookupError:
    # encoding指定为utf-88
    print('指定了未知的编码')
except UnicodeDecodeError:
    # encoding指定为gbk
    print('读取文件时解码错误')
finally:
    if file:
        file.close()
