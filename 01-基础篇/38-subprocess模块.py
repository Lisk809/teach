# coding: utf-8
# @Author: 小飞有点东西


import subprocess

obj = subprocess.Popen('dir & ajfljl',
                       shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
#
# res = obj.stdout.read()
# print(res.decode('utf-8'))

error_res = obj.stderr.read()
print(error_res.decode('gbk'))
