"""文件读取和写入"""

# 一次读取全部文件
# file = open('./res/致橡树.txt', 'r', encoding='utf-8')
# print(file.read())
# file.close()

# 逐行读取文件
file = open('./res/致橡树.txt', 'r', encoding='utf-8')
for line in file:
    # 因为文件中已经包含了换行符，所以在使用print函数时，结束符指定为空字符串，否则行与行之间就会出现一个空行
    print(line, end='')
file.close()

file = open('./res/致橡树.txt', 'r', encoding='utf-8')
lines = file.readlines()
for line in lines:
    print(line, end='')
file.close()

# 向文件中追加内容
file = open('./res/致橡树.txt', 'a', encoding='utf-8')
file.write('\n标题：《致橡树》')
file.write('\n作者：舒婷')
file.write('\n时间：1977年3月')
file.close()
