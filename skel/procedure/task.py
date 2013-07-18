from pymongo import MongoClient
from system import conf
import cgi

client = MongoClient(conf.mongo['host'],conf.mongo['port'])
db = client.test
collection = db.masters

def rebuild_tasks(cur, given):
  done_list     = []
  notfound_list = []
  for gv in given:
    gv = gv.decode('utf8')
    if gv in cur:
      done_list.append(gv)
      while cur.count(gv):
        cur.remove(gv)
    else:
      notfound_list.append(gv)
  return (done_list, notfound_list, cur)

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
      # TODO: DRY
      self.__response['resp']['module'] = 'task'
      self.__response['resp']['class']  = 'List'
      self.__response['args'] = {
        'user'      : context['user'],
        'origin'    : context['origin'],
        'tasks_str' : tasks_str,
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

class Add:
  __response = {
    'resp' : {},
    'args' : {},
  }
  @classmethod
  def perform(self, context):
    master = collection.find({'name':context['user']['screen_name']})
    # """ print dir(master) """
    if master.count() is 1:
      m = master[0]
      old = m['tasks']
      added = context['origin'].text.encode('utf8').split(' ')
      added.remove(conf.at_bot_name)
      added.remove(cgi.escape(context['command']))
      cur = old + added
      # TODO: DRY
      self.__response['resp']['module'] = 'task'
      self.__response['resp']['class']  = 'Add'
      self.__response['args'] = {
        'user'      : context['user'],
        'origin'    : context['origin'],
        'tasks'     : {
          'added'    : { 'list' : added, 'str' : ','.join(added) },
          'old'      : { 'list' : old,   'str' : ','.join(old).encode('utf8')  },
          'current'  : { 'list' : cur,   'str' : ','.join(cur)  },
        },
        'command'   : context['command'],
      }
      print(self.__response)
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

class Done:
  __response = {
    'resp' : {},
    'args' : {},
  }
  @classmethod
  def perform(self, context):
    master = collection.find({'name':context['user']['screen_name']})
    if master.count() is 1:
      m = master[0]
      tasks_from_text = context['origin'].text.encode('utf8').split(' ')
      tasks_from_text.remove(conf.at_bot_name)
      tasks_from_text.remove(context['command'])
      (done, notfound, new) = rebuild_tasks(m['tasks'], tasks_from_text)

      # update record
      m['tasks'] = new
      collection.save(m)

      self.__response['resp']['module'] = 'task'
      self.__response['resp']['class']  = 'Done'

      self.__response['args'] = {
        'user'      : context['user'],
        'origin'    : context['origin'],
        'tasks'     : {
          'done'     : { 'list' : done,     'str' : ','.join(done).encode('utf8')     },
          'notfound' : { 'list' : notfound, 'str' : ','.join(notfound).encode('utf8') },
          'new'      : { 'list' : new,      'str' : ','.join(new).encode('utf8')      },
        },
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
