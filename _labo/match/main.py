# -*- coding: utf-8 -*-
import re
from system import *

enstr = 'abcidefg hijklmn opqrstu hoge vwixyz hoge'
jastr = '@hisyotan 　たーげっと　うんこ　おしっこ たーげっと'

def en(regex):
  print('--en--')
  pat = re.compile(regex)
  if pat.search(enstr) is not None:
    print(pat.search(enstr).group(0))
  else:
    print(None)
  if pat.match(enstr) is not None:
    print(pat.match(enstr).group(0))
  else:
    print(None)

def search(regex,src=jastr):
  print('--search--')
  pat = re.compile(regex)
  if pat.search(src) is not None:
    print('search res Exist')
  else:
    print(None)

arr = util.split_by_delimiter(jastr)
print(len(arr))
for i,v in enumerate(arr):
  print(i)
  try:
    print(v)
  except:
    pass
