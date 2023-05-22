# msg = ['张大仙', 84, 1.88, False]  # list(['张大仙', 84, 1.88, False])
# print(type(msg))

# print(list('hello'))
# print(list({'李白': '刺客', '武则天': '法师', '孙尚香': '射手'}))


# 内置方法
# 按索引取值
# print(l[0], l[-1])
# l[3] = '九天圣姬'
# print(l)
# 追加
# l.append(5)
# l.append(6)
# print(l)

# 插入
# l.insert(0,'李淳风')
# print(l)
# l = ['李星云', '姬如雪', '袁天罡']
# l2 = ['梵音天', '秒成天', '玄净天']
# l.append(l2)
# print(l)
# for i in l2:
#     l.append(i)
# print(l)

# extend    字符串、字典
# l.pop()
# print(l)
# print(l+l2)

# 删除
# 1、del
# names = ['美杜莎','云韵','熏儿','雅妃']
# del names[0]
# print(names)

# 2、pop
# names = ['美杜莎','云韵','熏儿','雅妃']
# res = names.pop(0)
# print(res)
# print(names)

# 3、remove
# names = ['美杜莎', '云韵', '熏儿', '雅妃','美杜莎']
# res = names.remove('美杜莎')
# print(res)
# print(names)

# 切片
# names = ['美杜莎', '云韵', '熏儿', '雅妃','美杜莎']
# print(names[0:2])

# len()统计长度
# len(names)

# 成员运算
# print('云韵' in names)

# 循环
# names = ['美杜莎', '云韵', '熏儿', '雅妃','美杜莎']
# for i in names:
#     names.pop(0)
#     print(names)

# 其他操作
# count
# names = ['美杜莎', '云韵', '熏儿', '雅妃','美杜莎','云韵','云韵']
# print(names.count('云韵'))

# index
# print(names.index('云韵'))

# clear
# names.clear()
# print(names)

# reverse
# names = ['美杜莎', '云韵', '熏儿', '雅妃','美杜莎']
# print(names[::-1])
# names.reverse()
# print(names)

# sort
# l = [55, 66, 33, 99,'aasa']
# l.sort(reverse=False)
# print(l)
# l = ['w', 's', 'a', 'd']
# l.sort()
# print(l)
# print('abcde' > 'abdg')


# 队列和堆栈
# 队列 FIFO 先进先出
# l = []
# # 入队操作
# l.append('张三')
# l.append('李四')
# l.append('王五')
# print(l)
#
# # 出队操作
# print(l.pop(0))
# print(l.pop(0))
# print(l.pop(0))


# 堆栈 LIFO 后进先出
l = []
# 入栈操作
l.append('张三')
l.append('李四')
l.append('王五')
print(l)

# 出栈操作
print(l.pop())
print(l.pop())
print(l.pop())
