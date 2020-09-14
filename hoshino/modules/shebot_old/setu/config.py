import re

DEFAULT_ONLINE = True #是否默认在线涩图
WITH_URL = True #发图是是否附带链接
R18_PATH = 'C:/TomoriBot/res/setu/r18_setu' #r18 涩图保存路径,必须在酷Q图片路径下
NR_PATH = 'C:/TomoriBot/res/setu/nr18_setu'#非r18涩图保存路径，必须在酷Q图片路径下
SEARCH_PATH = 'C:/bot/res/setu/search_setu'#搜索结果保存路径，必须在酷Q图片路径下
COMMON_RE = re.compile('^来?([1-5])?[份点张]?[涩色瑟]图(.{0,10})$')#非r18匹配正则表达式
SECRET_RE = re.compile('^就这不够色([1-5])?$')#r18正则表达式



