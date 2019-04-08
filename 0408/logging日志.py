import logging
# 创建日志模块
loginLogger = logging.getLogger('main')
# 设置等级
loginLogger.setLevel(logging.DEBUG)
# 创建日志输出类型
fileHandler = logging.FileHandler('logging.txt', encoding='utf-8')
# 设置文件日志等级
fileHandler.setLevel(logging.ERROR)
# 指定日志格式
fileFormater = logging.Formatter('%(name)s-%(levelno)s-%(lineno)d-%(asctime)s-%(message)s')
# 将文件绑定日志格式
fileHandler.setFormatter(fileFormater)

streamHanlder = logging.StreamHandler()
streamHanlder.setLevel(logging.DEBUG)
streamHanlder.setFormatter(fileFormater)

# 将日志处理方法台南佳到日志工具
loginLogger.addHandler(fileHandler)
loginLogger.addHandler(streamHanlder)

loginLogger.debug('debug')
loginLogger.info('info')
loginLogger.warning('warning')
loginLogger.error('error')

