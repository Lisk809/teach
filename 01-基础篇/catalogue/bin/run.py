# coding: utf-8
# @Author: 小飞有点东西

# from ..core.core import main
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from core.core import main
from conf import settings
from db import db_handle


if __name__ == '__main__':
    main()
