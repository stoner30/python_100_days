"""
读写JSON

注：
作者更推荐ujson库，因其性能较标准库更好。
另外，同样具备对象序列化、反序列化功能的模块（标准库）还有pickle和shelve。
pickle：可以直接将文件保存为二进制文件，或者从二进制文件中还原对象
shelve：基于pickle，更像是简单数据库，不但可以持久化数据，还可以进行数据检索
"""
import json

my_dict = {
    'name': '张某',
    'age': 22,
    'friends': ['李某', '赵某某'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280},
    ]
}
# 将字典序列化为JSON字符串，如果不设置ensure_ascii参数为False，默认会讲中文转换为unicode码
print(json.dumps(my_dict, indent=4, ensure_ascii=False))

# 将字典序列化并保存到文件中
with open('./data.json', 'w', encoding='utf-8') as f:
    json.dump(my_dict, f, ensure_ascii=False, indent=4)

# 同样，从JSON字符串或文件读取为字段，需要用到loads和load
with open('./data.json', 'r', encoding='utf-8') as f:
    data_dict = json.load(f)
    print(type(data_dict))
    print(data_dict)
