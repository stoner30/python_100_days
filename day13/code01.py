"""
字典方法
"""
person = {
    'name': '王大锤',
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': '成都市武侯区科华北路62号1栋101'
}

print(person['name'])
print(len(person))
person['signature'] = '你的男朋友是一个盖世垃圾，他会踏着五彩祥云去赢取你的闺蜜'
print(person)

print(person.keys())
print(person.values())
print(person.items())

for key, value in person.items():
    print(f'{key}: \t{value}')

print(person.get('not_exist'))
print(person.get('not_exist', 'Not Found'))

# 合并两个字典
person2 = {
    'mobile': '13800138000'
}
person.update(person2)
print(person)

# Python3.9后也支持|运算符，等价于update方法
person3 = {
    'job': '无业游民'
}
person |= person3
print(person)
