# coding: utf-8
# @Author: 小飞有点东西


# 列表生成式：[结果 for item in 可迭代对象 if 条件]
# l = ['康师傅_老坛酸菜', '统一_老坛酸菜', '大今野_老坛酸菜', '白象']
# new_l = []
# for name in l:
#     if name.endswith('老坛酸菜'):
#         new_l.append(name)
# print(new_l)
#
#
# # new_l = [name for name in l if name.endswith('老坛酸菜')]
# # new_l = [name for name in l if True]
# # new_l = [name.replace('老坛酸菜', '小鸡炖蘑菇') for name in l]
# new_l = [[i for i in range(10) if i > 6] for name in l]
# print(new_l)


# # 集合生成式
# l = ['康师傅_老坛酸菜', '统一_老坛酸菜', '大今野_老坛酸菜', '白象']
# res = {name for name in l}
# print(res, type(res))


# 字典生成式
# l = ['康师傅_老坛酸菜', '统一_老坛酸菜', '大今野_老坛酸菜', '白象']
# res = {name: 5 for name in l}
# print(res, type(res))


# l = [('康师傅_老坛酸菜', 5), ('统一_老坛酸菜', 6), ('大今野_老坛酸菜', 7), ('白象', 8)]
# res = {k: v for k, v in l if not k.startswith('康师傅')}
# print(res, type(res))


# 生成器表达式
# l = ['康师傅_老坛酸菜', '统一_老坛酸菜', '大今野_老坛酸菜', '白象']
# res = (name for name in l)
# # print(res, type(res))
# print(next(res))
# print(res.send(None))
# print(res.send(10))
# print(res.send('张大仙'))
# print(res.send('张大仙'))


with open('data/user.log', mode='rt', encoding='utf-8')as f:
    # size = 0
    # for line in f:
    #     size += len(line)
    # print(size)
    # print([len(line) for line in f])
    size = sum(len(line) for line in f)
    print(size)
















