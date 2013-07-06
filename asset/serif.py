import lib.util

serif = {
  'test' : {
    'unko' : [
      'unko1',
      'unko2',
      'unko3',
    ]
  }
}

class Serif:

  def __init__(self,key):
    if serif.has_key(key):
      self.res_str = util.random_choice(serif[key])

  def apply(self,params):
    return self.res_str
