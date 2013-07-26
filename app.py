import sys
from core import *

with_init_tw = False
if 1 < len(sys.argv) and sys.argv[1] == 'd':
  with_init_tw = True

hisyotan = Skel(name='hisyotan',with_init_tw=with_init_tw)
hisyotan.listen()
