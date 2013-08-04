from pymongo import MongoClient
from system import conf, util
from core.procedure.base import ProcedureBase

client = MongoClient(conf.mongo['host'],conf.mongo['port'])
db = client.test
collection = db.masters

def pick_up_target_masters(masters):
  res = []
  for m in masters:
    res.append(m)
  return res

class Execute(ProcedureBase):
  def perform(self, context):
    masters = collection.find({'do_weekly':True})
    self._response['resp']['module'] = 'remind.weekly'
    self._response['resp']['class']  = 'Execute'
    self._response['args'] = {
      'masters' : pick_up_target_masters(masters),
    }
    return self._response

class Enable(ProcedureBase):
  def perform(self, context):
    master = collection.find({'name':context['user']['screen_name']})
    if master.count() is 1:
      m = master[0]
      m['do_weekly'] = True
      collection.save(m)
      self._response['resp']['module'] = 'remind.weekly'
      self._response['resp']['class']  = 'Enable'
      self._response['args'] = {
        'user'    : context['user'],
        'origin'  : context['origin'],
        'command' : context['command'],
      }
    else:
      return self.res_common_help(context)
    return self._response

class Disable(ProcedureBase):
  def perform(self, context):
    master = collection.find({'name':context['user']['screen_name']})
    if master.count() is 1:
      m = master[0]
      m['do_weekly'] = False
      collection.save(m)
      self._response['resp']['module'] = 'remind.weekly'
      self._response['resp']['class']  = 'Disable'
      self._response['args'] = {
        'user'    : context['user'],
        'origin'  : context['origin'],
        'command' : context['command'],
      }
    else:
      return self.res_common_help(context)
    return self._response
