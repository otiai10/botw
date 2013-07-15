

class Echo:
  __response = {
    'resp' : {},
    'args' : {},
  }
  @classmethod
  def perform(self, context):
    self.__response['resp']['module'] = 'test'
    self.__response['resp']['class']  = 'Echo'
    self.__response['args'] = {
      'text_given' : context['text_given'],
      'user'       : context['user'],
      'origin'     : context['origin'],
    }
    return self.__response

class Trigger:
  __response = {
    'resp' : {},
    'args' : {},
  }
  @classmethod
  def perform(self, context):
    self.__response['resp']['module'] = 'test'
    self.__response['resp']['class']  = 'Trigger'
    self.__response['args'] = {
      'trigger_word' : context['trigger_word'],
      'user'         : context['user'],
      'origin'       : context['origin'],
    }
    return self.__response
