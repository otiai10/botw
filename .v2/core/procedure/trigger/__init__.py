from core.procedure.base import ProcedureBase

class Default(ProcedureBase):
  def perform(self, context):
    self._response['resp']['module'] = 'trigger'
    self._response['resp']['class']  = 'Default'
    self._response['args'] = {
      'trigger_word' : context['trigger_word'],
      'user'       : context['user'],
      'origin'     : context['origin'],
    }
    return self._response
