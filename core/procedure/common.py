from core.procedure.base import ProcedureBase

class Help:
  def perform(self, context):
    self._response['resp']['module'] = 'common'
    self._response['resp']['class']  = 'Help'
    self._response['args'] = {
      'user'       : context['user'],
      'origin'     : context['origin'],
      'command'    : context['command'],
    }
    return self._response
