from _datetime import datetime
from datetime import datetime
DATE_NOW = datetime.today()
print (f'Start: {DATE_NOW}')
# CODE
print (f'Now: {datetime.today()}')
print (f'Duration: {datetime.today() - DATE_NOW}')

import time
start = time.time()
# CODE
finish = time.time()
dur=datetime(finish-start)
print (f'Duration: {dur}')
