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
    masters = collection.find({'do_weekly':True})
    self.__response['resp']['module'] = 'remind.weekly'
    self.__response['resp']['class']  = 'Execute'
    self.__response['args'] = {
      #'masters' : pick_up_target_masters(masters),
      'masters' : collection.find({'name':'otiai10'}),
    }
    return self.__response

class Enable:
  __response = {
    'resp' : {},
    'args' : {},
  }
  @classmethod
  def perform(self, context):
    master = collection.find({'name':context['user']['screen_name']})
    if master.count() is 1:
      m = master[0]
      m['do_weekly'] = True
      collection.save(m)
      self.__response['resp']['module'] = 'remind.weekly'
      self.__response['resp']['class']  = 'Enable'
      self.__response['args'] = {
        'user'    : context['user'],
        'origin'  : context['origin'],
        'command' : context['command'],
      }
    else:
      self.__response['resp']['module'] = 'common'
      self.__response['resp']['class']  = 'Help'
      self.__response['args'] = {
        'user'    : context['user'],
        'origin'  : context['origin'],
        'command' : context['command'],
      }
    return self.__response

class Disable:
  __response = {
    'resp' : {},
    'args' : {},
  }
  @classmethod
  def perform(self, context):
    master = collection.find({'name':context['user']['screen_name']})
    if master.count() is 1:
      m = master[0]
      m['do_weekly'] = False
      collection.save(m)
      self.__response['resp']['module'] = 'remind.weekly'
      self.__response['resp']['class']  = 'Disable'
      self.__response['args'] = {
        'user'    : context['user'],
        'origin'  : context['origin'],
        'command' : context['command'],
      }
    else:
      self.__response['resp']['module'] = 'common'
      self.__response['resp']['class']  = 'Help'
      self.__response['args'] = {
        'user'    : context['user'],
        'origin'  : context['origin'],
        'command' : context['command'],
      }
    return self.__response
