# 1 导入模块
import logging
# 2 创建日志模块
loginLogger = logging.getLogger("main")
# 2.1 设置等级
loginLogger.setLevel(logging.DEBUG)

# 3 创建日志输出类型
fileHandler = logging.FileHandler('loginregist.txt',encoding='utf-8')
# 3.1 文件日志等级
fileHandler.setLevel(logging.DEBUG)
# 4 指定日志格式
fileformater = logging.Formatter('%(name)s-%(levelno)s-%(lineno)d-%(asctime)s-%(message)s')
# 5 将文件绑定日志格式
fileHandler.setFormatter(fileformater)

streamHanlder = logging.StreamHandler()
streamHanlder.setLevel(logging.DEBUG)
streamHanlder.setFormatter(fileformater)



# 6 将日志处理方法添加到日志工具
loginLogger.addHandler(fileHandler)
loginLogger.addHandler(streamHanlder)

loginLogger.debug("debug000")
loginLogger.info("info000")
loginLogger.warning("warning000")
loginLogger.error("error000")
