# coding: utf-8
# @Author: 小飞有点东西
__all__ = ['name', 'get']
print('我是module')
name = '张大仙'


def func1():
    print('我是func1')
    print(name)


def func2():
    global name
    name = '周杰伦'
    print('我是func2')


def get():
    print(name)


# print('module.py的__name__属性：', __name__)
if __name__ == '__main__':
    print('module被执行')
    func1()
    func2()

