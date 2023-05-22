# 明天是周六，你就不用上班
# 你年龄大于18岁，你就可以进网吧

# 显式布尔值
# 明天==’周六’  -> True
# 年龄>18   -> True
# True
# False

# 隐式布尔值
# 0、None、空（空字符串、空列表、空字典）->False
# 其他所有的值都是True
# 10  -> True
# 0   -> False
# None  -> False
# '张大仙'   -> True
# ''   -> False
# '    '   -> True
# []、{}   -> False


# if True:
#     代码


# 逻辑运算
girl_friend = 'human'
gender = 'male'
age = 18

# print(girl_friend == 'human')
# print(gender == 'female')
# print(16 < age < 84)

# 逻辑运算符:
# and 逻辑与
# print(girl_friend == 'human' and gender == 'female' and 16 < age < 84)
#

# not 逻辑非
# print(not True)
# print(not 16 < age < 84)
# print(not 0)
# print(not 100)
# print(not None, not '', not [], not {})


# or 逻辑或

# 优先级
# not>and>or
#          True                            False                       False
# (84 != 73 and (not 22 > 22)) or (37 == 27 and '张大仙' == '李白') or 18 > 20

# print(84 != 73 and (not 22 > 22 or 31 == 27) and '张大仙' == '李白' or 18 > 20)


# 成员运算符
# print('仙' in '张大仙你是个妖怪吧')

l = [1, 2, 3]
# print(4 in l)

dic = {'name': '张大仙', 'age': 84}
# print('name' in dic)

# print('张大仙' not in '张大仙你是个妖怪吧')
# print(not '张大仙' in '张大仙你是个妖怪吧')


# if判断
'''
if 条件:
    代码1
    代码2
    ...
else:
    代码1
    代码2
    ...
'''

# print(1)
# print(2)
# if 条件:
#     子代码块
# print(3)
# print(4)

# is_human = input('你是不是个人，请输入是或者不是：')
# gender = input('请输入你的性别：')
# age = int(input('请输入你的年龄：'))
# if is_human == '是' and gender == '女' and 16 < age < 84:
#     print('我喜欢你，我们一起生猴子吧！')
# else:
#     print('你是个好人')
# print('你这个渣男')


# elif
# if 条件：
#     子代码块
# elif 条件2：
#     子代码块
# elif 条件2：
#     子代码块
# elif 条件2：
#     子代码块
# else：
#     子代码块
# xxx

grade = 59
if grade == 100:
    print('去海洋公园')
elif 80 <= grade:
    print('吃肯德基')
elif grade >= 60:
    print('喝西北风')
else:
    print('裤子脱掉，皮鞭伺候')
