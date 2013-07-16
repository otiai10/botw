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
    for m in master:
      print m

    # {{{ tmp
    self.__response['resp']['module'] = 'common'
    self.__response['resp']['class']  = 'Help'
    self.__response['args'] = {
      'user'       : context['user'],
      'origin'     : context['origin'],
      'command'    : context['command'],
    }
    # }}}
    return self.__response
