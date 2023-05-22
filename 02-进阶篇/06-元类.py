# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA

# 元类：实例化产生类的类
# 元类 --实例化--> 类(Human) --实例化--> 对象(obj)

# 用class这个关键字，定义的所有的类，以及内置的类
# 都是由内置的元类type，实例化产生的

# Human = 元类()

# 定义了一个类
# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print('name:', self.name, 'age:', self.age)
#
# print(Human.__dict__)
# # 基于类创建了一个对象
# obj = Human('张大仙', 73)
#
# print(type(obj))
# print(type(Human))
# print(type(str))

# # 1、类名
# class_name = 'Human'
#
# # 2、基类
# class_bases = (object,)
#
# # 3、执行类子代码，产生名称空间
# class_dic = {}
# class_body = '''
# def __init__(self, name, age):
#     self.name = name
#     self.age = age
# def info(self):
#     print('name:', self.name, 'age:', self.age)
# '''
# exec(class_body, {}, class_dic)
# # print(class_dic)
#
#
# # 4、调用元类
# Human = type(class_name, class_bases, class_dic)
# # print(Human)
# obj = Human('张大仙', 73)
# obj.info()
import abc


# # 自定义元类
# class Mytype(type):
#     def __init__(self, class_name, class_bases, class_dic):
#         # print('Mytype.init')
#         if '_' in class_name:
#             raise NameError('类名不能有下划线！')
#
#         # print(class_dic)
#         if not class_dic.get('__doc__'):
#             raise SyntaxError('定义类必须写注释！')
#
#         print(class_bases)
#         print(self.__bases__)
#
#     def __new__(cls, *args, **kwargs):
#         print('Mytype.__new__')
#         print(cls)
#         print(args)
#         print(kwargs)
#
#         return type.__new__(cls, *args, **kwargs)
#

# print(type(Mytype))
# # Human = Mytype(class_name, class_bases, class_dic)
# # 调用了内置元类type的__call__
#     # 1、调用Mytype的__new__方法，产生一个空对象Human
#     # 2、调用Mytype的init方法，初始化对象Human
#     # 3、返回初始化好的对象Human
#

'''

对象() --> 类内部的__call__
类() --> 自定义元类内部的__call__
自定义元类() ---> 内置元类的__call__

'''

# class Human(metaclass=Mytype):
#     '''
#     测试元类，嘿嘿嘿~
#     '''
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print('name:', self.name, 'age:', self.age)


# __call__
# class Test:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __call__(self, *args, **kwargs):
#         print('Test.__call__')
#         return 'abc'
#
#
# obj = Test('张大仙', 73)
# # print(obj)
# res = obj(1,2,3,x=4,y=5)   # obj.__call__()
# print(res)

# 如果想把一个对象，做成一个可以加括号调用的对象，
# 就在对象的类里面加一个__call__方法


# # 自定义元类
# class Mytype(type):
#     def __call__(self, *args, **kwargs):
#         human_obj = self.__new__(self)
#         self.__init__(human_obj, *args, **kwargs)
#         dic = {}
#         for key in human_obj.__dict__:
#             dic[f'H_{key}'] = human_obj.__dict__[key]
#
#         human_obj.__dict__ = dic
#         return human_obj
#
# class Human(metaclass=Mytype):
#     '''
#     测试元类，嘿嘿嘿~
#     '''
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print('name:', self.name, 'age:', self.age)
#
#     def __new__(cls, *args, **kwargs):
#         obj = object.__new__(cls)
#         return obj
#
#     # def __call__(self, *args, **kwargs):
#     #
#
# obj = Human('张大仙', 73)
# # 触发Mytype的__call__方法
# #     1、调用Human的__new__方法
# #     2、调用Human的__init__方法
# #     3、返回初始化好的对象
#
# print(obj.__dict__)


# 属性查找
# 对象=》类=》父类=》object
# class Mytype(type):
#     age = 18
#     def __call__(self, *args, **kwargs):
#         # print(object.__new__ is self.__new__)
#         obj = self.__new__(self)
#         self.__init__(obj, *args, **kwargs)
#         return obj
#
# class Animal(object):
#     # age = 17
#     pass
#
# class Human(Animal):
#     # age = 16
#     pass
#
# class Chinese(Human, metaclass=Mytype):
#     # age = 15
#     pass
#
# class ScPerson(Chinese):
#     # age = 14
#     pass
#
# obj = ScPerson()
# # print(obj.age)
# # print(ScPerson.age)
# print(type(Human))

