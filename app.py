import sys
from core import Bot

hisyotan = Bot(name='hisyotan')

if 1 < len(sys.argv):
  if sys.argv[1] == 'd':
    hisyotan.listen(with_init_tw=True)
  elif sys.argv[1] == 'o':
    hisyotan.draw(opt={'key':sys.argv[2],'console':True})
else:
  hisyotan.listen(with_init_tw=False)
