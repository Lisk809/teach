# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA

# 反射机制

# def f1(obj):
#     if 'age' not in obj.__dict__:
#         return
#     obj.age
#
#
# f1(18)


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('name:', self.name, 'age:', self.age)


obj = Human('张大仙', 73)











# dir(obj)[-1]

# hasattr()
# getattr()
# setattr()
# delattr()

# print(hasattr(obj, 'x'))
# print(getattr(obj, 'name')) # obj.name
# setattr(obj, 'name', '李白')
# print(obj.name)
# delattr(obj, 'name')
# print(obj.__dict__)

# if hasattr(18, 'age'):
#     print(getattr(18, 'age'))
# else:
#     print('没有age')

# print(getattr(obj, 'age', None))


class Ftp:
    def put(self):
        print('正在上传数据。。。')

    def get(self):
        print('正在下载数据。。。')

    def interact(self):
        opt = input('>>>')
        getattr(self, opt, self.warning)()

    def warning(self):
        print('功能不存在！')


obj = Ftp()
obj.interact()










