'''
while 条件:
    子代码1
    子代码2
    ...

'''

# num = 0
# while num < 10:  # 1,...,10
#     print(num)  # 0,1,....,9
#     # num = num + 1
#     # num += 1  # 1,2,10
# print('循环结束了')

# while True:
#     info = input('请输入内容：')
#     print(info)

# while 1:
#     10+10


# username = '1303544500'
# password = '123456'

# condition = True
# while True:
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


# while+continue
# num = 0
# while num < 10:
#     if num == 4:
#         num += 1
#         continue
#     print(num)
#     num += 1

# username = '1303544500'
# password = '123456'
# num = 0
# while True:
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
#         if num == 3:
#             print('账号密码已经连续输错了3次，账号已被锁定')
#             break


# while+else
'''
while True:
    ...
else:
    ...
'''

# num = 0
# while num < 10:
#     if num == 4:
#         num += 1
#         break
#     print(num)
#     num += 1
# else:
#     print('循环正常结束')


username = '1303544500'
password = '123456'
num = 0
while num<3:
    input_username = input('请输入你的账号：')
    input_password = input('请输入你的密码：')
    if input_username == username and input_password == password:
        print('登录成功')
        while True:
            action = input('请输入你的操作：')
            if action == 'Q':
                break
            print(f'正在{action}')
        break  # 立即结束本层循环
    else:
        print('用户名或密码错误')
        num += 1
else:
    print('账号密码输错3次，账号已被锁定')


