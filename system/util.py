# -*- coding: utf-8 -*-
from datetime import *
import time,re

delimiter = '[ 　]*'
knot = ','

def get_file_name(file__, contain_file_extension=False):
  if contain_file_extension:
    return file__.split('/')[-1]
  return file__.split('/')[-1].split('.')[0]

def convert_twitter_format(tw):
  return _convert_v1(tw)

def _convert_v1(tw):
  result = {
    'user' : {},
    'text' : '',
    'friends' : None,
    'retweeted' : False,
    'retweet_count' : 0,
    'in_reply_to_screen_name' : '',
    'id' : '',
  }

  # implementation
  for k,v in result.items():
    if (k in tw.keys()):
      result[k] = tw[k]
  return result

def get_timestamp(is_float=False):
  timestamp = time.mktime(datetime.now().timetuple())
  if is_float:
    return timestamp
  return str(timestamp)

def get_timestr(opt=None, space=True):
  res = ''
  if opt is None:
    res = '[{d.year}/{d.month:02}/{d.day:02}/ {d.hour:02}:{d.minute:02}:{d.second:02}]'.format(d=datetime.today())
  else:
    res = datetime.today().isoformat()
  if space:
    return res + ' '
  return res

def split_by_delimiter(string):
  return re.split(delimiter, string)

def join_with_knot(_list):
  return knot.join(_list)

def join_(knot, _list):
  _list = map(lambda x: str(x), _list)
  return knot.join(_list)
