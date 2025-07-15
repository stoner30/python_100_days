"""CSV文件的读写"""
import csv
import random

with open('./scores.csv', 'w') as f:
    """
    CSV文件写入
    csv.writer(file)可以指定附加参数，来设置分隔符、包围符和包围范围
    """
    writer = csv.writer(f, delimiter='|', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(['姓名', '语文', '数学', '英语'])
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    for name in names:
        scores = [random.randrange(50, 101) for _ in range(3)]
        scores.insert(0, name)
        writer.writerow(scores)

with open('./scores.csv', 'r') as f:
    """CSV文件读取"""
    reader = csv.reader(f, delimiter='|', quotechar='"', quoting=csv.QUOTE_ALL)
    for row in reader:
        print(reader.line_num, end='\t')
        for element in row:
            print(element, end='\t')
        print()
