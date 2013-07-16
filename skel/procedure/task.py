from pymongo import MongoClient
from system import conf

client = MongoClient(conf.mongo['host'],conf.mongo['port'])
db = client.test
collection = db.masters

class List:
  __response = {
    'resp' : {},
    'args' : {},
  }
  @classmethod
  def perform(self, context):

    master = collection.find({'name':context['user']['screen_name']})
    # print dir(master)
    if master.count() is 1:
      m = master[0]
      tasks_str = ','.join(m['tasks']).encode('utf8')
      self.__response['resp']['module'] = 'task'
      self.__response['resp']['class']  = 'List'
      self.__response['args'] = {
        'user'      : context['user'],
        'origin'    : context['origin'],
        'tasks_str' : tasks_str,
        'command'   : context['command'],
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
