from asset import Asset

class Yoruho:
  def __init__(self):
    self.__serif_category = 'monologue.jiho'
    self.__serif_key      = self.__class__.__name__
  def generate(self, args):
    serif = Asset('serif').load(
      self.__serif_category,
      self.__serif_key
    ).get_text()
    self.__msg_args = {
      'actions' : [
        'update_status',
      ],
      'message': serif,
    }
    return self.__msg_args

class Hiruho:
  def __init__(self):
    self.__serif_category = 'monologue.jiho'
    self.__serif_key      = self.__class__.__name__
  def generate(self, args):
    serif = Asset('serif').load(
      self.__serif_category,
      self.__serif_key
    ).get_text()
    self.__msg_args = {
      'actions' : [
        'update_status',
      ],
      'message': serif,
    }
    return self.__msg_args

class Jiho:
  def __init__(self):
    self.__serif_category = 'monologue.jiho'
    self.__serif_key      = self.__class__.__name__
  def generate(self, args):
    serif = Asset('serif').load(
      self.__serif_category,
      self.__serif_key
    ).apply(args).get_text()
    self.__msg_args = {
      'actions' : [
        'update_status',
      ],
      'message': serif,
    }
    return self.__msg_args
