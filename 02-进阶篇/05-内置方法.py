# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


# 内置方法：会在满足条件的时候自动执行
# __init__

# l = [1,2,3]
# len(l)
# print(l)


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'<{self.name}: {self.age}>'

    def __del__(self):
        self.f.close()


obj = Human('张大仙', 73)
# print(obj.__str__())
# print(obj)  # <张大仙:73>

# __del__
# 在删除对象的时候，先执行
# del obj
# print('='*50)



