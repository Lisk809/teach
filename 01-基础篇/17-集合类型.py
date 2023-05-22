# 集合（去重、做关系运算）
# s = {1, 2, 3, 1, 1, 1}
# print(list(s))
# a = set()
# b = {}
# print(type(a), type(b))

# 关系运算
# hobbies1 = ['吃饭','睡觉','看书','钢琴','跳舞','游泳','旅行']
# hobbies2 = ['吃饭','睡觉','追剧','打游戏']
# both_like = []
# for i in hobbies1:
#     if i in hobbies2:
#         both_like.append(i)
# print(both_like)

# hobbies1 = {'吃饭', '睡觉', '看书', '钢琴', '跳舞', '游泳', '旅行'}
# hobbies2 = {'吃饭', '睡觉', '追剧', '打游戏'}

# 取交集
# res = hobbies1 & hobbies2
# print(res)

# 取并集
# print(hobbies1 | hobbies2)

# 取差集
# print(hobbies1 - hobbies2)
# print(hobbies2 - hobbies1)

# 对称差集
# print((hobbies1 - hobbies2) | (hobbies2 - hobbies1))
# print(hobbies1 ^ hobbies2)

# 父子集
# s1 = {1, 2, 3}
# s2 = {1, 2, 4}
# print(s1>s2)
# print(s1<s2)
# print(s1==s2)


# 内置方法
# 取交集：s1.intersection(s2)
# 取并集：s1.union(s2)
# 取差集：s1.difference(s2)
# 取对称差集：s1.symmetric_difference(s2)
# 父子集(如果两者相等，则互为父子，结果都是True）
# 父集：s1.issuperset(s2)
# 子集：s1.issubset(s2)

# 去重
# l = ['a', 'd', 'a', 'b', 'z', 'b']
# print(set(l))
# info = [
#     ['张三', 18],
#     ['李四', 19],
#     ['王五', 18],
#     ['张三', 18],
#     ['王五', 18]
# ]
# set(info)
# new_info = []
# for i in info:
#     if i not in new_info:
#         new_info.append(i)
# print(new_info)
# len()
# in not in
# 循环

# s = {1, 2, 3, 4}
# s2 = {3, 4, 5}
# s.update([4,5,6])
# print(s)
# s.intersection_update(s2)
# s = s.intersection(s2)
# print(s)
# print(s3)

# s = {1, 2, 3, 4}
# s2 = {3, 4, 5}
# s.remove(5)
# s.discard(5)
# s.add(6)
# s1 = {1, 2, 3, 4}
# s2 = {4, 5, 6}
#
# res = s1.isdisjoint(s2)
# print(res)


a = set([1,2,3])
print(a)



