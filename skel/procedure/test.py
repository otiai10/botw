
class Echo:
  __response = {
    'resp' : {},
    'args' : {},
  }
  @classmethod
  def perform(self, context):
    print __file__
    self.__response['resp']['module'] = 'test'
    self.__response['resp']['class']  = 'Echo'
    self.__response['args'] = {
      'text_given' : context['text_given'],
      'user'       : context['user'],
      'origin'     : context['origin'],
    }
    return self.__response
