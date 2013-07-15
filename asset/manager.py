from datetime import *
import time


class Asset:

  __text = '(   *A*) < This is Basetext in Asset Class!!'

  def __init__(self, resource):
    pass

  def load(self, category, key):
    return self

  def apply(self, params):
    # {{{ tmp
    self.__text += params['text_given']
    return self
    # }}}

  def get_text(self, opt=None):
    # {{{ for debug
    timestamp = time.mktime(datetime.now().timetuple())
    # }}}
    self.__text += ' and TS is ' + str(timestamp)
    return self.__text
