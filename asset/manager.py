from datetime import *
import time


class Asset:

  __resource_type   = ''
  __loaded_rsrc = ''

  def __init__(self, resource):
    self.__resource_type = resource
    pass

  def load(self, category, key):
    # {{{ load resource from json
    self.__loaded_rsrc = '(   *A*) < This is Basetext in Asset Class!!'
    # }}}
    return self

  def apply(self, params):
    if self.__resource_type == 'serif':
      mod = __import__('processor.serif.test',globals(),locals,['Echo'],-1)
      Prcsr = getattr(mod, 'Echo')
      self.__text = Prcsr.process(self.__loaded_rsrc, params)
    return self

  def get_text(self, opt=None):
    # {{{ for debug
    timestamp = time.mktime(datetime.now().timetuple())
    # }}}
    self.__text += ' and TS is ' + str(timestamp)
    return self.__text

#if __name__ == '__main__':
#  a = Asset('serif')
#  print a.load('test','Echo').apply({'text_given':'ggggggggggggggg'}).get_text()
