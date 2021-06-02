import logging
import time
import datetime
from logging.handlers import RotatingFileHandler

log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')

logFile = '/home/pi/Desktop/log/relative.log'

my_handler = RotatingFileHandler(logFile, mode='a', maxBytes=5*1024*1024, backupCount=999, encoding=None, delay=0)
my_handler.setFormatter(log_formatter)
my_handler.setLevel(logging.INFO)

app_log = logging.getLogger('root')
app_log.setLevel(logging.INFO)

app_log.addHandler(my_handler)

app_log.info("data" + str(datetime.datetime.now()))
# while True:
#     time.sleep(1)
#     print(datetime.datetime.now())
#     app_log.info("data" + str(datetime.datetime.now()))