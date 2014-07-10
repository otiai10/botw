import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from core import Bot

hisyotan = Bot(name='hisyotan')

if 1 < len(sys.argv):
  arg1 = sys.argv[1]
  if arg1 == 'd' or arg1 == '--daemon':
    # app.py d
    hisyotan.listen(with_init_tw=True)
  elif arg1 == 'o' or arg1 == '--once':
    # app.py o all
    # app.py o Conv.Echo
    hisyotan.draw(key=sys.argv[2],console=True)
  elif arg1 ==  'm' or arg1 == '--monologue':
    # app.py m
    if 2 < len(sys.argv):
      hisyotan.monologue(console=True)
    else:
      hisyotan.monologue(console=False)
  elif arg1 ==  'r' or arg1 == '--remind':
    # app.py r daily
    # app.py r weekly
    hisyotan.remind(mode=sys.argv[2])
else:
  hisyotan.listen(with_init_tw=False)
