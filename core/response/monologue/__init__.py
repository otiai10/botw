from asset import Asset

class Default:
  # monologue Test class
  __serif_category = ''
  __serif_key      = ''
  def __init__(self):
    self.__serif_category = 'monologue.default'
    self.__serif_key      = self.__class__.__name__

  def generate(self, args):
    #  apply is not necessary here (so far)
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
