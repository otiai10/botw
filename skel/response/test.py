from system import *
from asset import Asset

class Echo:
  # {{{ TODO : DRY
  __serif_category = ''
  __serif_key      = ''
  def __init__(self):
    self.__serif_category = util.get_file_name(__file__)
    self.__serif_key      = self.__class__.__name__
  # }}}
    
  def generate(self, args):
    serif = Asset('serif').load(
      self.__serif_category,
      self.__serif_key
    ).apply(args).get_text()

    self.__msg_args = {
      'action' : 'update_status',
      'message': serif,
      'origin' : args['origin'],
    }
    return self.__msg_args

class Trigger:
  # {{{ TODO : DRY
  __serif_category = ''
  __serif_key      = ''
  def __init__(self):
    self.__serif_category = util.get_file_name(__file__)
    self.__serif_key      = self.__class__.__name__
  # }}}
    
  def generate(self, args):
    serif = Asset('serif').load(
      self.__serif_category,
      self.__serif_key
    ).apply(args).get_text()

    self.__msg_args = {
      'action' : 'update_status',
      'message': serif,
      'origin' : args['origin'],
    }
    return self.__msg_args
