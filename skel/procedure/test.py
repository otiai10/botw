
class Echo:
  __response = {
    'resp' : {},
    'args' : {},
  }
  @classmethod
  def perform(self, params):
    print __file__
    self.__response['resp']['module'] = 'test'
    self.__response['resp']['class']  = 'Echo'
    self.__response['args'] = {
      'text_given' : params['text_given'],
    }
    return self.__response
