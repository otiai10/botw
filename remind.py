import sys
from core import Bot

hisyotan = Bot(name='hisyotan')

if 1 < len(sys.argv):
  if sys.argv[1] == '--daily':
    hisyotan.remind(mode='daily')
  elif sys.argv[1] == '--weekly':
    hisyotan.remind(mode='weekly')
  else:
    pass
