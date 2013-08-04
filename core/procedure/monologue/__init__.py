from core.procedure.base import ProcedureBase

class Execute(ProcedureBase):
  def perform(self, context):
    # some dispatching here
    self._response['resp']['module'] = 'monologue'
    self._response['resp']['class']  = 'Test'
    self._response['args'] = {
    }
    return self._response
