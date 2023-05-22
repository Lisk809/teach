# coding: utf-8
# @Author: 小飞有点东西

# import logging
# from logging import config
import logging.config
import settings

logging.config.dictConfig(settings.LOGGING_DIC)
logger3 = logging.getLogger('用户充值')
logger3.info('xxx充值了5毛钱')

logger4 = logging.getLogger('用户操作')
logger4.info('xxx登录了')


logger5 = logging.getLogger('用户转账')
logger5.info('xxx给yyy转了5毛钱')

logger6 = logging.getLogger('用户提现')
logger6.info('xxx提现了5毛钱')

# 日志轮转


# 日志配置字典

# logging.debug('调试日志')
# logging.info('消息日志')
# logging.warning('硬盘空间不足')
# logging.error('错误日志')
# logging.critical('严重错误日志')












