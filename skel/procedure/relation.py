from pymongo import MongoClient
from system import conf

client = MongoClient(conf.mongo['host'],conf.mongo['port'])
db = client.test
collection = db.masters

class Create:
  __response = {
    'resp' : {},
    'args' : {},
  }
  @classmethod
  def perform(self, context):

    master = collection.find({'name':context['user']['screen_name']})

    if master.count() is 0:

      m = {
        'name'     : context['user']['screen_name'],
        #'tw_id'    : context['user']['id_str'],
        'do_daily' : False,
        'daily'    : '',
        'tasks'    : [],
      }
      collection.save(m)

      self.__response['resp']['module'] = 'relation'
      self.__response['resp']['class']  = 'Create'
      self.__response['args'] = {
        'user'      : context['user'],
        'origin'    : context['origin'],
        'command'   : context['command'],
      }
    else:
      self.__response['resp']['module'] = 'relation'
      self.__response['resp']['class']  = 'AlreadyCreated'
      self.__response['args'] = {
        'user'    : context['user'],
        'origin'  : context['origin'],
        'command' : context['command'],
      }
    return self.__response

class Destroy:
  __response = {
    'resp' : {},
    'args' : {},
  }
  @classmethod
  def perform(self, context):

    master = collection.find({'name':context['user']['screen_name']})

    if master.count() is 1:

      m = master[0]

      collection.remove(m)

      # TODO: DRY
      self.__response['resp']['module'] = 'relation'
      self.__response['resp']['class']  = 'Destroy'
      self.__response['args'] = {
        'user'      : context['user'],
        'origin'    : context['origin'],
        'command'   : context['command'],
      }

    else:
      # TODO: DRY
      self.__response['resp']['module'] = 'common'
      self.__response['resp']['class']  = 'Help'
      self.__response['args'] = {
        'user'    : context['user'],
        'origin'  : context['origin'],
        'command' : context['command'],
      }
    return self.__response
