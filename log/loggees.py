import time, os, logging
from loguru import logger
# from settings import LOG_DIR # 日志保存路径

# 新增如下三行代码
class PropogateHandler(logging.Handler):
    def emit(self, record):
        logging.getLogger(record.name).handle(record)
        
class Log:
    """输出日志到文件和控制台"""
    def __init__(self):
        # 文件的命名
        log_name = f"test_{time.strftime('%Y-%m-%d', time.localtime()).replace('-','_')}.log"
        log_path = os.path.join(os.getcwd()+"\\logs\\111.log")
        # log_path = os.path.join(LOG_DIR, log_name)
        # 判断日志文件夹是否存在，不存则创建
        # if not os.path.exists(LOG_DIR): 
        #     os.mkdir(LOG_DIR)
        # 日志输出格式
        formatter = "{time:YYYY-MM-DD HH:mm:ss} | {level}: {message}"
        # 日志写入文件
        logger.add(log_path,   # 写入目录指定文件
               format=formatter,
               encoding='utf-8',   
               retention='10 days',  # 设置历史保留时长
               backtrace=True,  # 回溯
               diagnose=True,   # 诊断
               enqueue=True,   # 异步写入
               # rotation="5kb",  # 切割，设置文件大小，rotation="12:00"，rotation="1 week"
               # filter="my_module"  # 过滤模块
               # compression="zip"   # 文件压缩
              ) 
        # 新增代码
        logger.add(PropogateHandler(), format=formatter)

    def debug(self, msg):
        logger.debug(msg)

    def info(self, msg):
        logger.info(msg)

    def warning(self, msg):
        logger.warning(msg)

    def error(self, msg):
        logger.error(msg) 

log = Log()
