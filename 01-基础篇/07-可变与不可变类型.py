# 整型、浮点型、字符串类型、列表类型、字典类型、布尔值类型

# 可变类型：值改变的情况下，id不变，说明改的是原值

# 不可变类型：值改变的情况下，id变了
# 整型、浮点型、字符串类型、布尔值类型
# name = '张大仙'
# print(id(name))
# name = '李白'
# print(id(name))

# 可变类型：列表，字典
# l = ['张大仙', '李白', '韩信']
# print(id(l))
# l[1] = '露娜'
# print(l)
# print(id(l))

# {key:value,key:value}

dic = {10: 'a', 3.14: 'b', 'x': 'c', True: 'd'}
print(dic[10],dic[3.14],dic[True])
