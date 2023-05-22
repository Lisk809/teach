l1 = ['张大仙', '徐凤年', ['李淳罡', '邓太阿']]
l2 = l1
# l1[0] = '张坦克'
# print(l1)
# print(l2)

# 浅拷贝
# l3 = l1.copy()
# print(l3)
# print(id(l1),id(l3))
# print(id(l1[0]), id(l1[1]), id(l1[2]))
# print(id(l3[0]), id(l3[1]), id(l3[2]))
# l3[0] = '张坦克'
# l3[1] = '徐骁'
# l3[2][0] = '剑九黄'
# l3[2][1] = '王仙芝'
# print(l1)
# print(l3)

# 深拷贝
l1 = ['张大仙', '徐凤年', ['李淳罡', '邓太阿']]
import copy

l3 = copy.deepcopy(l1)
# print(l3)
# print(id(l1))
# print(id(l3))
# print(id(l1[0]), id(l1[1]), id(l1[2]))
# print(id(l3[0]), id(l3[1]), id(l3[2]))
# print(id(l1[2][0]),id(l1[2][1]))
# print(id(l3[2][0]),id(l3[2][1]))
l3[0] = '张坦克'
l3[1] = '徐骁'
l3[2][0] = '剑九黄'
l3[2][1] = '王仙芝'
print(l1)
print(l3)
