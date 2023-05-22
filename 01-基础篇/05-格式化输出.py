# -------张大仙---------
# -------李白---------
# 格式化字符串

# 1、%
# info = 'my name is %s, I am from %s.' % ('广东','张大仙')
# print(info)
# info = 'my name is %s' % '张大仙'
# print(info)

# info = 'my name is %(name)s, I am from %(hometown)s.' % {'hometown':'广东', 'name':'张大仙'}
# print(info)

# info = 'my name is %s' % 18
# print(info)
# info = 'my name is %s' % ['a','b']
# print(info)
# info = 'my name is %s' % {'a':'aa','b':'bb'}
# print(info)

# %d
# info = 'my name is %d' % 'a'
# print(info)

# 2、format()
# info = 'my name is {0}{0}{0}, I am from {1}{1}{1}.'.format('张大仙', '广东')
# print(info)

# info = 'my name is {name}, I am from {hometown}.'.format(name=['a','b'], hometown='广东')
# print(info)


# 格式化填充
# ****开始****
# a = '{0:*<20}'.format('开始')
# print(a)
# b = '{num:.2f}'.format(num=3.1415936)
# print(b)

# 3、f
name = input('请输入你的名字：')
hometown = input('你来自哪里：')
info = f'我的名字是{name}，我来自于{hometown}'
print(info)

# 4、string-Template(需要导入）
