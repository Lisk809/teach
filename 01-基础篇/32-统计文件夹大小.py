# coding: utf-8
# @Author: 小飞有点东西

import os


def stat_size(path):
    size = 0
    for item in os.listdir(path):
        next_path = os.path.join(path, item)
        if os.path.isdir(next_path):
            size += stat_size(next_path)
        else:
            size += os.path.getsize(next_path)
    return size


if __name__ == '__main__':
    res = stat_size(r'D:\teach')
    print(res)

