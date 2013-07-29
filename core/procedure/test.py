from core.procedure.base import ProcedureBase

class Echo(ProcedureBase):
  def perform(self, context):
    self._response['resp']['module'] = 'test'
    self._response['resp']['class']  = 'Echo'
    self._response['args'] = {
      'text_given' : context['text_given'],
      'user'       : context['user'],
      'origin'     : context['origin'],
    }
    return self._response

class Trigger(ProcedureBase):
  def perform(self, context):
    self._response['resp']['module'] = 'test'
    self._response['resp']['class']  = 'Trigger'
    self._response['args'] = {
      'trigger_word' : context['trigger_word'],
      'user'         : context['user'],
      'origin'       : context['origin'],
    }
    return self._response
