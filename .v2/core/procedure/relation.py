from core.procedure.base import ProcedureBase

class Create(ProcedureBase):
  def perform(self, context):
    master = self.mcollection.find({'name':context['user']['screen_name']})
    if master.count() is 0:
      m = {
        'name'     : context['user']['screen_name'],
        'tw_id'    : context['user']['tw_id'],
        'do_daily' : False,
        'daily'    : '',
        'do_weekly': True,
        'tasks'    : [],
      }
      self.mcollection.save(m)
      self._response['resp']['module'] = 'relation'
      self._response['resp']['class']  = 'Create'
      self._response['args'] = {
        'user'      : context['user'],
        'origin'    : context['origin'],
        'command'   : context['command'],
      }
    else:
      self._response['resp']['module'] = 'relation'
      self._response['resp']['class']  = 'AlreadyCreated'
      self._response['args'] = {
        'user'    : context['user'],
        'origin'  : context['origin'],
        'command' : context['command'],
      }
    return self._response

class Destroy(ProcedureBase):
  def perform(self, context):
    master = self.mcollection.find({'name':context['user']['screen_name']})
    if master.count() is 1:
      m = master[0]
      self.mcollection.remove(m)
      # TODO: DRY
      self._response['resp']['module'] = 'relation'
      self._response['resp']['class']  = 'Destroy'
      self._response['args'] = {
        'user'      : context['user'],
        'origin'    : context['origin'],
        'command'   : context['command'],
      }
    else:
      return self.res_common_help(context)
    return self._response
