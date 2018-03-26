# -*-coding:utf-8 -*-
from wxpy import *
from wxpy import get_wechat_logger

from wxpy import *

bot = Bot()

group_receiver = ensure_one(bot.groups().search('XX业务-告警通知'))

logger = get_wechat_logger(group_receiver)

logger.error('打扰大家了，但这是一条重要的错误日志...')
