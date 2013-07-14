
class Echo:
  __msg_args = {
    'action' : '',
    'message': '',
  }
  @classmethod
  def generate(self, args):
    self.__msg_args = {
      'action' : 'update_status',
      'message': args['text_given'],
    }
    return self.__msg_args
