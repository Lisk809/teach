# coding: utf-8
# @Author: 小飞有点东西

# import sys
# print(sys.path)

# 绝对导入
# from game.chat import chat
# from game.kanpsack import kanpsack
# from game.map import map
# from game.gg.pay import brilliant


# from a.b.c.e import f


# 相对导入
# .：当前文件夹
# ..：上一层文件夹

from .chat import chat
from .kanpsack import kanpsack
from .map import map
from .gg.pay import brilliant
from .gg.pay import sell
