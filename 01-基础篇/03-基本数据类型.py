# 数字类型
#   整型int
#     -0、1、2、3、100、1000
age = 73
# print(type(age))

#   浮点型float
price = 3.5
# print(type(price))


level = 1
level = level + 1
# print(level)

# print(10 - 1)
# print(10 * 2)
# print(10 / 2)

a = 3
b = 1.5
c = a + b
# print(c, type(c))

age = 16
# print(age > 18)

# 字符串类型str
'xxx'
"xxx"
a = """xxx"""
quotes = """人的差别在于业余时间，而一个人的命运
决定在晚上8点到10点之间。因为一开始大家都在同一高度，
做的工作一样，拿的薪水一样，大部分人下班后想休息，然
后一直刷视频、打游戏，这样得到了即时满足，很爽，但你
最终就什么都没有得到。但是如果你能每天把握住这两个小
时好好学习，能够习惯延迟满足，每天进步1%，那么一年后
你将比现在的自己优秀3倍。"""
# print(type(quotes))

name = '张大仙'
# print(type(name))
a = 73
# print(type(a))
b = '73'
# 'name' = '张大仙'

a = 'my name is \'张大仙\''
# print(a)

a = 'my name is '
b = '张大仙'
# print(a + b)

# print('-'*50)
# print('我喜欢你')
# print('-'*50)


name = '张大仙'
age = 73
price = 3.5

hobbies = '可乐，厕所，烫头'

# 列表
#     0    1      2         3
l = [73, 3.5, '张大仙', ['aaa', 'bbb'], 1, 3, 'aa', 'bbb', 'ccc', 'ddd']
# print(l[3][1])

hobbies = ['可乐', '厕所', '烫头']
# print(hobbies[1])

person = [
    ['张大仙', 73, 100, ['可乐', '厕所', '烫头']],
    ['韩信', 84, 200, ['打仗']],
    ['李白', 95, 0.5, ['喝酒', '写诗', '练剑']]
]
# print(type(person))

# print(person[1][2])
# print(person[2][3][1])

# 名字、年龄、身高、体重、薪资、三围
person = ['张大仙', 73, 150, 84, 180, 60, 80, 99]

# 字典类型dict
dic = {
    'name': '张大仙',
    'age': 73,
    'height': 150,
    'salary': 180
}

# print(type(dic))

# print(dic['name'])
# print(dic['salary'])

person = [
    {'name': '张大仙', 'age': 73, 'saraly': 100, 'hobbies': ['可乐', '厕所', '烫头']},
    {'name': '韩信', 'age': 84, 'saraly': 200, 'hobbies': ['打仗']},
    {'name': '李白', 'age': 95, 'saraly': 0.5, 'hobbies': ['喝酒', '写诗', '练剑']}
]

# print(person[0]['hobbies'][2])
# print(person[1]['hobbies'][0])

# 布尔类型bool
a = True
b = False
# print(type(a))
a = 1
b = 0

c = None
# print(type(c))

# 0 None '' [] {}都代表False


name = '张大仙'
l = ['a', 'b', name]
# print(l[2])
# print(id(name))
# print(id(l[2]))


a = 100
b = a
c = a

# 引用计数
# 标记清除
# 分代回收


name = '张大仙'
l = ['a', 'b', name]
name = '李白'
# print(l[2])
# print(name)


l1 = ['a', 'b']
l2 = ['x', 'y']
l1.append(l2)
# print(l1)
# print(id(l2), id(l1[2]))
l2.append(l1)
# print(l2)
# print(id(l1),id(l2[2]))
del l1
del l2


name = '张大仙'









