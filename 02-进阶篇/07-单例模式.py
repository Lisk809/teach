# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


# 单例模式
# 1、模块
from settings import obj
from settings import obj
from settings import obj
from settings import obj

# 2、类装饰器
# def singleton_mode(cls):
#     obj = None
#     def wrapper(*args, **kwargs):
#         nonlocal obj
#         if not obj:
#             obj = cls(*args, **kwargs)
#         return obj
#     return wrapper
#
#
# # @singleton_mode # Human = singleton_mode(Human)
# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# obj = Human('张大仙', 73)
# obj2 = Human('张大仙', 75)
# print(obj)
# print(obj2)


# 3、类绑定方法
# class Human:
#     obj = None
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def get_obj(cls, *args, **kwargs):
#         if not cls.obj:
#             cls.obj = cls(*args, **kwargs)
#         return cls.obj
#
#
# obj = Human.get_obj('张大仙', 73)
# obj2 = Human.get_obj('张大仙', 75)
# print(obj)
# print(obj2)

# 4、__new__方法
# class Human:
#     obj = None
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.obj:
#             cls.obj = super().__new__(cls)
#         return cls.obj
#
#
# obj = Human('张大仙', 73)
# obj2 = Human('张大仙', 75)
# print(obj)
# print(obj2)


# 5、元类
class Mytype(type):
    obj = None
    def __call__(self, *args, **kwargs):
        if not self.obj:
            # self.obj = super().__call__(*args, **kwargs)
            self.obj = self.__new__(self)
        self.__init__(self.obj, *args, **kwargs)
        return self.obj


class Singleton(metaclass=Mytype):
    pass


class Human(Singleton):

    def __init__(self, name, age):
        self.name = name
        self.age = age


obj = Human('张大仙', 73)
print(obj, obj.__dict__)

obj2 = Human('张大仙', 75)
print(obj2, obj2.__dict__)

# xxx is None

# 6、并发
