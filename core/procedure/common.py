
class Help:
  __response = {
    'resp' : {},
    'args' : {},
  }
  @classmethod
  def perform(self, context):
    self.__response['resp']['module'] = 'common'
    self.__response['resp']['class']  = 'Help'
    self.__response['args'] = {
      'user'       : context['user'],
      'origin'     : context['origin'],
      'command'    : context['command'],
    }
    return self.__response
