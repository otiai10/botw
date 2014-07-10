import datetime, random
from system import conf
from core.procedure.base import ProcedureBase

class Execute(ProcedureBase):
  def perform(self, context):
    if conf.monologue_rate < random.random():
      return None
    d = datetime.datetime.today()
    self._response['resp']['module'] = 'monologue'
    self._response['resp']['class']  = 'Default'
    if d.minute == 0:
      self._response['resp']['module'] = 'monologue.jiho'
      if d.hour == 0:
        self._response['resp']['class'] = 'Yoruho'
      elif d.hour == 12:
        self._response['resp']['class'] = 'Hiruho'
      else:
        self._response['resp']['class'] = 'Jiho'
        self._response['args']['hour'] = d.hour
    return self._response
