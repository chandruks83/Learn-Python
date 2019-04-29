#! python3
import os
import sys
import logging
import time

logFile = os.path.basename(sys.argv[0])[:-3]
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename=logFile + '.txt', filemode='w', level=logging.DEBUG)

time.sleep(2)
a = 5
print('a = %s' %(a))
logging.debug('value of a is %d' %(a))
time.sleep(2)
b = 10
print('b = %s' %(b))
logging.debug('value of b is %d' %(b))
time.sleep(2)
sum = a + b
print('a + b = %s' %(sum))
logging.debug('sum of a and b is %d' %(sum))
