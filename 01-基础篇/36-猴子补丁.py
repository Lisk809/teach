# coding: utf-8
# @Author: 小飞有点东西

# 猴子补丁：用自己的代码替换你所用模块的源代码
import json
import ujson


def monkey_patch_json():
    json.__name__ = 'ujson'
    json.dumps = ujson.dumps
    json.loads = ujson.loads


monkey_patch_json()








json.dumps()
json.loads()
json.dumps()

import json
json.loads()
json.dumps()
json.loads()
json.dumps()
json.loads()
json.dumps()
json.loads()
json.dumps()
json.loads()

import json
json.dumps()
json.loads()







import json