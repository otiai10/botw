import json, random

from system import conf,util

class Asset:

  path   = ''
  __category = ''
  __key      = ''
  __loaded_rsrc = ''

  def __init__(self, resource):
    self.path = '/asset/resource/' + resource
    pass

  def load(self, category, key):
    pool = {}
    resource_file = conf.app_root + self.path + '/' + '/'.join(category.lower().split('.')) + '.json'
    with open(resource_file, 'r', encoding='utf8') as f:
      pool = json.load(f)
    self.__loaded_rsrc = random.choice(pool[key])

    self.__category = category
    self.__key      = key

    return self

  def apply(self, params):
    mod = __import__('asset.processor.serif.' + self.__category ,globals(),locals,[self.__key])
    Prcsr = getattr(mod, self.__key)
    self._text = Prcsr.process(self.__loaded_rsrc, params)
    return self

  def get_text(self, time_footer=False):
    if not hasattr(self, '_text'):
      self._text = self.__loaded_rsrc
    if time_footer:
      self.embed_debug_ts()
    return self._text

  def get_dict(self, opt=None):
    resource_file = conf.app_root + self.path + '.json'
    with open(resource_file, 'r', encoding='utf8') as f:
      return json.load(f)
 
  def embed_debug_ts(self):
    self._text += ' %s' % util.get_timestr(space=False)
