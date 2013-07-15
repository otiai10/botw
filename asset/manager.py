from datetime import *
import time, json

from system import conf

class Asset:

  __resource_type   = ''
  __category = ''
  __key      = ''
  __loaded_rsrc = ''

  def __init__(self, resource):
    self.__resource_type = resource
    pass

  def load(self, category, key):
    pool = {}
    resource_file = conf.app_root + '/asset/resource/serif/' + category.lower() + '.json'
    with open(resource_file, 'r') as f:
      pool = json.load(f)
    self.__loaded_rsrc = pool[key]

    self.__category = category
    self.__key      = key

    return self

  def apply(self, params):
    if self.__resource_type == 'serif':
      mod = __import__('processor.serif.' + self.__category ,globals(),locals,[self.__key],-1)
      Prcsr = getattr(mod, self.__key)
      self.__text = Prcsr.process(self.__loaded_rsrc, params)
    return self

  def get_text(self, opt=None):
    # {{{ debug
    self.embed_debug_ts()
    # }}}
    return self.__text

  def embed_debug_ts(self):
    timestamp = time.mktime(datetime.now().timetuple())
    self.__text += ' and TS is ' + str(timestamp)

#if __name__ == '__main__':
#  a = Asset('serif')
#  print a.load('test','Echo').apply({'text_given':'ggggggggggggggg'}).get_text()