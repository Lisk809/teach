# dic = {'aaa': 1, 2: 2, 3.1: 3, (4, 5, 6): 4}
# dict({'aaa': 1, 2: 2, 3.1: 3, (4, 5, 6): 4})
# print(dic,type(dic))

# print(dict({'a': 1, 'b': 2}))

# print(dict(a=1, b=2, c=3))

# keys = ['name', 'gender', 'age']    #{'name':None,'gender':None,'age':None}
# dic = {}
# for key in keys:
#     dic[key] = None
# print(dic)
# a = {}.fromkeys(keys,None)
# print(a)

# l = [('name', '张大仙'), ['age', 18],['a','b']]
# print(dict(l))

# dic = {'a': 1, 'b': 2, 'c': 3,'c':4}
# dic['d'] = 4
# print(dic)


# dic = {'a': 1, 'b': 2, 'c': 3}
# print(dic.get('d'))
# dic['d']

# del dic['a']
# print(dic)
# print(dic.pop('a'))
# print(dic)
# print(dic.popitem())
# dic.clear()
# print(dic)
# print(len(dic))
# dic = {'a': 1, 'b': 2, 'c': 3}
# print(1 in dic)

# dic = {'a': 1, 'b': 2, 'c': 3}
# 字典的内置方法
# keys
# values
# items
# print(dic.keys())
# print(dic.values())
# print(dic.items())
# for key in dic.keys():
#     print(key)
# for value in dic.values():
#     print(value)
# msg = ('张大仙',18)
# name,age = msg
# print(name,age)

# for key,value in dic.items():
#     print(key, value)


# dic = {'a': 1, 'b': 2, 'c': 3}
# dic.update()
# hero = {'名字': '李白',
#         '职业': '刺客',
#         '移速': 550,
#         '攻速': 130}
# new = {'攻速': 120,
#        '技能1': '将进酒',
#        '技能2': '神来之笔',
#        '技能3': '青莲剑歌'}
# hero.update(new)
# print(hero)

# setdefault
# info = {'name': '张大仙', 'age': 18}
# info.setdefault('age')
# info.setdefault('gender','保密')
# print(info)

