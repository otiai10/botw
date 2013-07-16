from datetime import *
import time, json, random

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
    self.__loaded_rsrc = random.choice(pool[key])

    self.__category = category
    self.__key      = key

    return self

  def apply(self, params):
    #if self.__resource_type == 'serif':
    mod = __import__('processor.serif.' + self.__category ,globals(),locals,[self.__key],-1)
    Prcsr = getattr(mod, self.__key)
    self._text = Prcsr.process(self.__loaded_rsrc, params)
    return self

  def get_text(self, opt=None):
    if not hasattr(self, '_text'):
      self._text = self.__loaded_rsrc
    # {{{ debug
    self.embed_debug_ts()
    # }}}
    return self._text

  def get_dict(self, opt=None):
    resource_file = conf.app_root + '/asset/resource/' + self.__resource_type + '.json'
    with open(resource_file, 'r') as f:
      return json.load(f)
 
  def embed_debug_ts(self):
    timestamp = time.mktime(datetime.now().timetuple())
    self._text += ' and TS is ' + str(timestamp)
