#!/usr/bin/python #通常只在unix环境有效,作用是指定解释器路径,然后可以直接使用脚本名来执行,不需要在前面调用解释器

"""
模块的文档描述
"""

import time  # 导入模块

name = '小飞有点东西'  # 定义全局变量;如果不是必须,最好使用局部变量,这样可以提高代码的维护性,同时节省内存提高性能


class Test:  # 定义类
    """
    类的注释
    """
    pass


def func():  # 定义函数
    """
    函数注释
    """
    pass


if __name__ == '__main__':  # 主程序,在被当做脚本执行时,执行下面的代码
    func()
