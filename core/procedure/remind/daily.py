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

class Execute:
  def perform(self, context):
    masters = collection.find({'do_daily':True})
    self._response['resp']['module'] = 'remind.daily'
    self._response['resp']['class']  = 'Execute'
    self._response['args'] = {
      'masters' : pick_up_target_masters(masters),
    }
    return self._response

class Enable:
  def perform(self, context):
    pass

class Disable:
  def perform(self, context):
    pass
