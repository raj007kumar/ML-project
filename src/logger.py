import logging
import os
from datetime import datetime

LOG_FILE=os.path.join(os.getcwd(),'logs',datetime.now().strftime('%Y-%m-%d')+'.log')
os.makedirs(os.path.dirname(LOG_FILE),exist_ok=True)


LOG_FILE_PATH=os.path.join(os.getcwd(),'logs')


logging.basicConfig(filename = LOG_FILE,level = logging.DEBUG ,format = '%(asctime)s %(message)s',datefmt = '%Y-%m-%d  %H:%M:%S')




