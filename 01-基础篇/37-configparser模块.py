# coding: utf-8
# @Author: 小飞有点东西


# configparser模块
import configparser

config = configparser.ConfigParser()
config.read('data/test.ini', encoding='utf-8')

# print(config.sections())
# print(config.options('db'))
# print(config.items('db'))
# delay = config.getint('default', 'delay')
# print(delay, type(delay))
# delay = config.getfloat('default', 'salary')
# print(delay, type(delay))
# delay = config.getboolean('default', 'compression')
# print(delay, type(delay))









'''

# 这是注释
; 这也是注释

[default]
delay = 45
compression = true
compression_Level = 9
language_code = en-us
time_zone = UTC

[db]
db_type = mysql
database_name = catalogue_data
user = root
password = root
host = 127.0.0.1
port = 3306
charset = utf8

'''
