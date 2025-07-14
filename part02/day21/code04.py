"""
上下文管理器

with:
可以自动处理文件关闭而无需在 finally 块中调用 file.close 方法
但要注意，只有实现了 __enter__ 和 __exit__ 协议的对象才能使用 with 语法并正确执行
"""

# try:
#     with open('./res/guido.png', 'rb') as file1:
#         data = file1.read()
#     with open('./res/吉多.jpg', 'wb') as file2:
#         file2.write(data)
# except FileNotFoundError:
#     print('指定的文件无法打开')
# except IOError:
#     print('读写文件时出错')
# print('程序结束')

# 如果文件过大，一次性读入内存可能导致内存开销过大，可以分批读取指定大小的字节来优化内存占用
try:
    with open('./res/guido.png', 'rb') as file1, open('./res/吉多.jpg', 'wb') as file2:
        """实验了一下，read(self, size)方法针对二进制和文本模式都生效"""
        buffer_size = 512
        data = file1.read(buffer_size)
        while data:
            file2.write(data)
            data = file1.read(buffer_size)
except FileNotFoundError:
    print('指定的文件无法打开')
except IOError:
    print('读写文件时出错')
print('程序结束')
