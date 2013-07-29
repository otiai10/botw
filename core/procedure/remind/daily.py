from pymongo import MongoClient
from system import conf, util

client = MongoClient(conf.mongo['host'],conf.mongo['port'])
db = client.test
collection = db.masters

def pick_up_target_masters(masters):
  res = []
  for m in masters:
    res.append(m)
  return res

class Execute:
  __response = {
    'resp' : {},
    'args' : {},
  }
  @classmethod
  def perform(self, context):
    masters = collection.find({'do_daily':True})
    self.__response['resp']['module'] = 'remind.daily'
    self.__response['resp']['class']  = 'Execute'
    self.__response['args'] = {
      'masters' : pick_up_target_masters(masters),
    }
    return self.__response

class Enable:
  @classmethod
  def perform(self, context):
    pass

class Disable:
  @classmethod
  def perform(self, context):
    pass
