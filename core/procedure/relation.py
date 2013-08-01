from pymongo import MongoClient
from system import conf
from core.procedure.base import ProcedureBase

client = MongoClient(conf.mongo['host'],conf.mongo['port'])
db = client.test
collection = db.masters

class Create(ProcedureBase):
  def perform(self, context):
    master = collection.find({'name':context['user']['screen_name']})
    if master.count() is 0:
      m = {
        'name'     : context['user']['screen_name'],
        'tw_id'    : context['user']['tw_id'],
        'do_daily' : False,
        'daily'    : '',
        'do_weekly': True,
        'tasks'    : [],
      }
      collection.save(m)
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
    master = collection.find({'name':context['user']['screen_name']})
    if master.count() is 1:
      m = master[0]
      collection.remove(m)
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
