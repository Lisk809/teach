# name = '张大仙'
# print(type(name))
# str('张大仙')

# result = str(['aa', 'bb'])
# print(result, type(result))

# 索引取值
# info = 'good good study,day day up!'
# print(info[-1])
# info[0] = 'G'

# 切片
# print(info[0:20:3])
# print(info)
# info = 'good good study,day day up!'
# res = info[::-1]
# print(res)


# strip去除空格
# name = '-=(*!!!   张 大仙   !!!-=0*'
# res = name.strip('!-=(0* ')
# print(res)

# 登录案例
# input_username = input('请输入账号：').strip()
# input_password = input('请输入密码：').strip()
# if input_username == '1303544500' and input_password == '123456':
#     print('登录成功')
# else:
#     print('账号密码错误')

# split拆分
# names = '李白-韩信-露娜-孙悟空'
# res = names.split('-', 1)
# print(res, type(res))

# 循环

# 长度len
# info = 'good good study,day day up!'
# long = len(info)
# print(long, type(long))

# 成员运算in和not in
# print(not '张大仙' in '张大仙是个妖怪吧')


# 字符串的其他常见功能
# strip,lstrip,rstrip
# name = '  张大仙  '
# print(name.strip())
# print(name.lstrip())
# print(name.rstrip())

# split,rsplit
# names = '李白-杜甫-白居易-陶渊明'
# print(names.split('-', 1))
# print(names.rsplit('-', 1))

# format

# lower,upper
# msg = 'AbCd'
# print(msg.lower())
# print(msg.upper())

# startswith,endswith
# print('君不见，黄河之水天上来，奔流到海不复回'.startswith('君不见'))
# print('君不见，黄河之水天上来，奔流到海不复回'.endswith('不复回'))

# join
# l = ['李白', '杜甫', '白居易', '陶渊明', '1']
# l[0]+l[1].....
# f'{l[0]}-{l[1]}.......'
# print('-'.join(l))

# replace
# names = '李白-杜甫-白居易-陶渊明'
# print(names.replace('-', ':', 1))
# print(names.replace('李白', '诗仙', 1))

# isdigit
# print('84'.isdigit())
# print('8.a4'.isdigit())
#
# while 1:
#     num = input('请输入你猜的数字:').strip()
#     if num.isdigit():
#         num = int(num)
#     else:
#         print('别调皮，要输入纯数字！')
#         continue
#     if num >36:
#         print('猜大了')
#     elif num <36:
#         print('猜小了')
#     else:
#         print('猜中了')
#         break






# 字符串需要了解的操作
# 1	 capitalize()    将字符串的第一个字符转换为大写
# 2	 center(width, fillchar)    返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
# 3	 count(str, beg= 0,end=len(string))    返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
# 4  expandtabs(tabsize=8)  把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。
# 5	 find(str, beg=0, end=len(string))  检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
# 6  rfind(str, beg=0,end=len(string))   类似于 find()函数，不过是从右边开始查找.
# 7	 index(str, beg=0, end=len(string))  跟find()方法一样，只不过如果str不在字符串中会报一个异常。
# 8  rindex( str, beg=0, end=len(string))   类似于 index()，不过是从右边开始.
# 9	 isalnum()  如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True，否则返回 False
# 10  isalpha()  如果字符串至少有一个字符并且所有字符都是字母或中文字则返回 True, 否则返回 False
# 11  islower()   如果字符串中包含至少一个区分大小写的字符，并且所有这些字符都是小写，则返回 True，否则返回 False
# 12  isupper()  如果字符串中包含至少一个区分大小写的字符，并且所有这些字符都是大写，则返回 True，否则返回 False
# 13  isspace()   如果字符串中只包含空白，则返回 True，否则返回 False.
# 14  ljust(width,fillchar)  返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
# 15  rjust(width,fillchar)   返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
# 16  max(str)   返回字符串 str 中最大的字母。
# 17  min(str)   返回字符串 str 中最小的字母。
# 18  swapcase()   将字符串中大写转换为小写，小写转换为大写
# 19  title()   返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写
# 20  istitle()   如果字符串是标题化的，则返回 True，否则返回 False

