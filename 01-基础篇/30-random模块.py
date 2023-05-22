# coding: utf-8
# @Author: 小飞有点东西


# random
import random

# print(random.random())
# print(random.uniform(1, 10))
# print(random.randint(-100, 100))
# print(random.randrange(1, 3))
# print(random.choice(['张大仙', 18, ('可乐', '厕所', '烫头')]))
# print(random.sample(['张大仙', 18, ('可乐', '厕所', '烫头')], 1))
# li = [1, 3, 5, 7, 9]
# random.shuffle(li)
# print(li)


# 随机生成一个16位密码
# 必须包含大写字母,小写字母,数字和符号,如:vC3D-kf26c+70(Z4
def pwd_generator(length=16):
    pwd = ''
    char_list = [[97,122],[65,90],[48,57],[33,47]]
    for _ in range(length):
        random_list = random.choice(char_list)
        random_char = chr(random.randint(*random_list))
        pwd += random_char
    return pwd


# print(pwd_generator(6))








def pwd_generator(length=16):
    if length < 4:
        return ''
    while True:
        pwd = ''
        for _ in range(length):
            char_list = [[97, 122], [65, 90], [48, 57], [33, 47]]
            random_list = random.choice(char_list)
            random_char = chr(random.randint(*random_list))
            pwd += random_char
        l = [False for i in range(4)]   # 创建4个值都为False的列表
        # 遍历前面生成的密码,判断密码是否包含四种类型的字符,
        # 因为可能16次循环完了,碰巧缺少某一种或多种字符
        for word in pwd:
            if 97 <= ord(word) <= 122:
                l[0] = True
            if 65 <= ord(word) <= 90:
                l[1] = True
            if 48 <= ord(word) <= 57:
                l[2] = True
            if 33 <= ord(word) <= 47:
                l[3] = True
        if l[0] and l[1] and l[2] and l[3]:  # 如果四个值都为True,则返回密码
            return pwd
        print('密码不合法:', pwd)    # 如果密码没有包含4种字符,则重新生成


# pwd = pwd_generator(6)
# print(pwd)


def pwd_generator(length=16):
    pwd = []
    for _ in range(length//4+1):
        char_list = [chr(random.randint(97, 122)),
                     chr(random.randint(65, 90)),
                     chr(random.randint(48, 57)),
                     chr(random.randint(33, 47))]
        pwd.extend(char_list)
    pwd = pwd[:length]
    random.shuffle(pwd)
    return ''.join(pwd)


print(pwd_generator(8))

