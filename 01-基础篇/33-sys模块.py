# coding: utf-8
# @Author: 小飞有点东西

import sys

# sys.path
from_path = sys.argv[1]
new_path = sys.argv[2]

with open(from_path, 'rb')as f1, open(new_path, 'wb')as f2:
    f2.write(f1.read())


