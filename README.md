# clog
彩色日志，文件夹下自动生成log日志目录，根据运行的文件命名log名称,生成json日志，exception log

安装方法：
pip install plogs

demo:

import plogs

log = plogs.logger

log_json = plogs.logger_json


log.debug('这是一条debug日志')
log.info('这是一条info日志')
log.warning('这是一条warning日志')
log.error('这是一条error日志')

try:
   b = 1 + a 
exception Exception as e:
    log.exception(e)


log_json('这是一条json日志格式')

log.debug('所有日志内容输出在了屏幕，和你执行目录下面的log 文件夹。 文件名是你的程序名')
