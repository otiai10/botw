# -*- coding: utf-8 -*-
import sys,io

print(sys.stdout.encoding)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print(sys.stdout.encoding)

s = 'りっちゃんぺろぺろ'
print(s)
