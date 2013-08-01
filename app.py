import sys
from core import Bot

hisyotan = Bot(name='hisyotan')

if 1 < len(sys.argv):
  if sys.argv[1] == 'd':
    hisyotan.listen(with_init_tw=True)
  elif sys.argv[1] == 'o':
    opt={}
    if 2 < len(sys.argv) and sys.argv[2].isdigit():
      opt = {'count':int(sys.argv[2])}
    hisyotan.draw(opt=opt)
else:
  hisyotan.listen(with_init_tw=False)
