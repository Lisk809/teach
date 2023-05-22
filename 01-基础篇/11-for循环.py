# 循环取值（遍历）
# 列表、字典、字符串、元组、集合
"""
for 变量名 in 可迭代对象:
    子代码块
    。。。
"""

# l = ['张大仙', '张宏发', '张冰心', '张坦克']
# for a in l:
#     print(a)
# i = 0
# while i < 4:
#     print(l[i])
#     i += 1

# dic = {'name': '张大仙', 'age': 84, 'height': 200}
# for i in dic:
#     print(dic[i])
#
# s = 'hello world!'
# for i in s:
#     print(i)


# for x in [1,2,3,4,5]:
#     print('aaa')

# range()
# for i in range(10):
#     print('张大仙')


# username = '1303544500'
# password = '123456'
# num = 0
# for i in range(3):
#     input_username = input('请输入你的账号：')
#     input_password = input('请输入你的密码：')
#     if input_username == username and input_password == password:
#         print('登录成功')
#         while True:
#             action = input('请输入你的操作：')
#             if action == 'Q':
#                 break
#             print(f'正在{action}')
#         break  # 立即结束本层循环
#     else:
#         print('用户名或密码错误')
#         num += 1
# else:
#     print('账号密码输错3次，账号已被锁定')


for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j}x{i}={i * j}', end='\t')
    print('')

# print('张大仙是个妖怪吧', end='')
# print('张大仙是个妖怪吧')
