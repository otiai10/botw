from system import *
from asset import Asset

class List:
  # """ TODO : DRY
  __serif_category = ''
  __serif_key      = ''
  def __init__(self):
    self.__serif_category = util.get_file_name(__file__)
    self.__serif_key      = self.__class__.__name__
  # """
    
  def generate(self, args):
    serif = Asset('serif').load(
      self.__serif_category,
      self.__serif_key
    ).apply(args).get_text()

    self.__msg_args = {
      'actions' : ['update_status'],
      'message' : serif,
      'origin'  : args['origin'],
    }

    return self.__msg_args

class Empty:
  # """ TODO : DRY
  __serif_category = ''
  __serif_key      = ''
  def __init__(self):
    self.__serif_category = util.get_file_name(__file__)
    self.__serif_key      = self.__class__.__name__
  # """
    
  def generate(self, args):
    serif = Asset('serif').load(
      self.__serif_category,
      self.__serif_key
    ).apply(args).get_text()

    self.__msg_args = {
      'actions' : ['update_status'],
      'message' : serif,
      'origin'  : args['origin'],
    }

    return self.__msg_args

class Add:
  # """ TODO : DRY
  __serif_category = ''
  __serif_key      = ''
  def __init__(self):
    self.__serif_category = util.get_file_name(__file__)
    self.__serif_key      = self.__class__.__name__
  # """
    
  def generate(self, args):
    serif = Asset('serif').load(
      self.__serif_category,
      self.__serif_key
    ).apply(args).get_text()
    self.__msg_args = {
      'actions' : ['update_status'],
      'message' : serif,
      'origin'  : args['origin'],
    }
    return self.__msg_args

class Done:
  # """ TODO : DRY
  __serif_category = ''
  __serif_key      = ''
  __msg_args       = {}
  def __init__(self):
    self.__serif_category = util.get_file_name(__file__)
    self.__serif_key      = self.__class__.__name__
  # """
    
  def generate(self, args):

    # """ nothing """
    if len(args['tasks']['done']['list']) is 0 and len(args['tasks']['notfound']['list']) is 0:
      self.__msg_args['actions'] = []
      self.__msg_args['origin'] = args['origin']
      return self.__msg_args

    # """ without done """
    if len(args['tasks']['done']['list']) is 0:
      serif = Asset('serif').load(
        self.__serif_category,
        'Notfound_Without_Done'
      ).apply(args).get_text()
      self.__msg_args = {
        'actions' : ['update_status'],
        'message' : serif,
        'origin'  : args['origin'],
      }
      return self.__msg_args

    # """ COMPLETE! """
    if len(args['tasks']['new']['list']) is 0:
      serif = Asset('serif').load(
        self.__serif_category,
        'Complete'
      ).apply(args).get_text()
      self.__msg_args = {
        'actions' : ['update_status'],
        'message' : serif,
        'origin'  : args['origin'],
      }
      return self.__msg_args

    # """ DONE and new tasklist """
    if len(args['tasks']['notfound']['list']) is 0:
      serif = Asset('serif').load(
        self.__serif_category,
        'Done'
      ).apply(args).get_text()
      self.__msg_args = {
        'actions' : ['update_status'],
        'message' : serif,
        'origin'  : args['origin'],
      }
      return self.__msg_args

    # """ DONE and Notfound
    serif = Asset('serif').load(
      self.__serif_category,
      'Done_With_Notfound'
    ).apply(args).get_text()
    self.__msg_args = {
      'actions' : ['update_status'],
      'message' : serif,
      'origin'  : args['origin'],
    }
    return self.__msg_args
