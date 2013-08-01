class ProcedureBase:
  _response = {
    'resp' : {},
    'args' : {},
  }

  def res_common_help(self, context):
    self._response['resp']['module'] = 'common'
    self._response['resp']['class']  = 'Help'
    self._response['args'] = {
      'user'    : context['user'],
      'origin'  : context['origin'],
      'command' : context['command'],
    }
    return self._response

  def rebuild_tasks(self, cur, given):
    done_list     = []
    notfound_list = []
    for gv in given:
      if gv in cur:
        done_list.append(gv)
        while cur.count(gv):
          cur.remove(gv)
      else:
        notfound_list.append(gv)
    return (done_list, notfound_list, cur)
