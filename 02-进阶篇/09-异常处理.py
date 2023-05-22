# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


# 异常处理
# print(name)
# print(111)
# l = [1,2,3]
# l[6]
# print(222)

# 语法上的错误
# print（）

# 逻辑上的错误
# l = None
# for i in l:
#     print(i)

# d = {'name': '张大仙'}
# d['age']

# int('abc')

# import bbb
# from time import bbb

# class Test:
#     pass
# # Test.xxx
# len(Test)


# 错误发生的条件可以预知
# while True:
#     num = input('请输入数字：').strip()
#     if not num.isdigit():
#         print('必须是数字！')
#         continue
#     num = int(num)
#     if num > 666:
#         print('猜大了')
#     elif num < 666:
#         print('猜小了')
#     else:
#         print('猜对了')
#         break


# 错误发生的条件不可预知
# S <========> C
# try:
#     子代码块1
#     子代码块2
#     子代码块3
#
# except 异常类型1 as e:
#     子代码块
# except 异常类型2 as e:
#     子代码块
# except 异常类型3 as e:
#     子代码块
# except 异常类型4 as e:
#     子代码块
# except Exception as e:
#     子代码块
# else:
#     子代码块：会在被检测代码（try下面的子代码块）没有异常的时候执行
# finally:
#     子代码块4
#
# xxx
# xxx


print('开始')
try:
    print('1'.center(20, '='))
    num = 'abc'
    # int(num)

    print('2'.center(20, '='))
    print(name)

    print('3'.center(20, '='))
    dic = {'name': '张大仙'}
    # dic['age']
# except (ValueError, NameError) as e:
#     print('异常信息：', e)
# except KeyError as e:
#     print('key不存在：', e)
# except Exception as e:
#     print('捕捉任意错误类型：', e)
# else:
#     print('没有异常')
finally:
    print('生前遗书')
print('结束')






