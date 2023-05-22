# coding: utf-8
# @Author: 小飞有点东西


# time
import time
# 1、时间戳
# print(time.time())

# 2、格式化的字符串形式：2030-11-11 11:11:11
# print(time.strftime('%Y-%m-%d %H:%M:%S %A'))
# print(time.strftime('%Y-%m-%d %X %A'))
# print(time.strftime('%x %X %A'))
# print(time.strftime('%Y'))

# 3、结构化时间
# res = time.localtime()
# print(res)
# print(res.tm_year)
# print(res.tm_mon)
# print(res.tm_yday)

# datetime
import datetime

# res = datetime.datetime.now() + datetime.timedelta(days=365*5)
# print(res.replace(microsecond=0))

# 时间戳 --localtime/gmtime--> 结构化时间 --strftime--> 格式化的字符串时间
# 时间戳 <--mktime-- 结构化时间 <--strptime-- 格式化的字符串时间
# res = time.time()
# print(time.localtime(111111111))
# print(time.gmtime(111111111))
# print(time.gmtime())
# res = time.localtime(111111111)
# print(time.strftime('%Y-%m-%d %X', res))

# t = '1983-12-07 01:02:02'
# # print(time.strptime(t, '%Y-%m-%d %X'))
# res = time.strptime(t, '%Y-%m-%d %X')
# print(time.mktime(res)+30*24*60*60)

# time.sleep()
# print(time.asctime())
# print(time.ctime(time.time()))

# print(datetime.datetime.now())
# print(datetime.datetime.utcnow())

# print(datetime.datetime.fromtimestamp(111111111))

