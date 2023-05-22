# coding: utf-8
# @Author: 小飞有点东西

# 序列化和反序列化
# 序列化:把内存中的数据类型转成一种特定格式,这种特定格式可以用于存储,
# 或者传输给其他平台使用

# 内存中的数据类型 ----> 序列化 ----> 特定格式(json/pickle)
# 内存中的数据类型 <---- 反序列化 <---- 特定格式(json/pickle)


# 用途:
# 1、存档
# 2、跨平台数据交互（只能用json，pickle是Python专用的格式）

# java                python
# 数组       json     列表


# json模块
import json

# 序列化
# dic = {'name': '张大仙', 'age': 18, 'salary': 3.5, 'married': False, 'hobbies': ['可乐', '厕所', '烫头']}
# json_res = json.dumps(dic, ensure_ascii=False)
# with open('data/test.json', mode='wt', encoding='utf-8')as f:
#     f.write(json_res)

# with open('data/test1.json', mode='wt', encoding='utf-8')as f:
#     json.dump(dic, f, ensure_ascii=False)

# 反序列化
# with open('data/test.json', mode='rt', encoding='utf-8')as f:
#     json_res = f.read()
# dic = json.loads(json_res)
# print(dic, type(dic))

# with open('data/test1.json', mode='rt', encoding='utf-8')as f:
#     json_res = json.load(f)
#     print(json_res)


# with open('data/test.json', mode='rb')as f:
# #     json_res = f.read()
# # dic = json.loads(json_res)
#     dic = json.load(f)
# print(dic, type(dic))


# json.dumps({1,2,3,4})


dic = {
    'name': '张大仙',
    'age': 18,
    'salary': 3.5,
    'married': False,
    'hobbies': ['可乐', '厕所', '烫头'],
    's': {1, 2, 3, 4}
}


# pickle模块
import pickle

# pickle_res = pickle.dumps(dic, protocol=0)
with open('data/test2.pickle', mode='wb')as f:
    pickle.dump(dic, f, protocol=0)


# xml
import xml










'''
<?xml version="1.0" encoding="utf-8" standalone="no"?>
<students>
    <student number="1001">
        <name>张三</name>
        <age>23</age>
        <gender>male</gender>
    </student>
    <student number="1002">
        <name>李四</name>
        <age>32</age>
        <gender>female</gender>
    </student>
    <student number="1003">
        <name>王五</name>
        <age>55</age>
        <gender>male</gender>
    </student>
</students>
'''
