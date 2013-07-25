from pymongo import MongoClient
from system import conf, util

client = MongoClient(conf.mongo['host'],conf.mongo['port'])
db = client.test
collection = db.masters

def rebuild_tasks(cur, given):
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

class List:
  __response = {
    'resp' : {},
    'args' : {},
  }
  @classmethod
  def perform(self, context):

    master = collection.find({'name':context['user']['screen_name']})
    if master.count() is 1:
      m = master[0]
      if len(m['tasks']) == 0:
        self.__response['resp']['module'] = 'task'
        self.__response['resp']['class']  = 'Empty'
        self.__response['args'] = {
          'user'      : context['user'],
          'origin'    : context['origin'],
          'command'   : context['command'],
        }
      else: 
        tasks_str = ','.join(m['tasks'])
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
      added = util.split_by_delimiter(context['origin']['text'])
      added.remove(conf.at_bot_name)
      added.remove(context['command'].strip())
      cur = old + added

      m['tasks'] = cur
      collection.save(m)

      # TODO: DRY
      self.__response['resp']['module'] = 'task'
      self.__response['resp']['class']  = 'Add'
      self.__response['args'] = {
        'user'      : context['user'],
        'origin'    : context['origin'],
        'tasks'     : {
          'added'    : { 'list' : added, 'str' : ','.join(added) },
          'old'      : { 'list' : old,   'str' : ','.join(old)  },
          'current'  : { 'list' : cur,   'str' : ','.join(cur)  },
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
      tasks_from_text = util.split_by_delimiter(context['origin']['text'])
      tasks_from_text.remove(conf.at_bot_name)
      while True:
        if context['command'].strip(util.delimiter) in tasks_from_text:
          tasks_from_text.remove(context['command'].strip(util.delimiter))
        else:
          break

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
          'done'     : { 'list' : done,     'str' : ','.join(done)     },
          'notfound' : { 'list' : notfound, 'str' : ','.join(notfound) },
          'new'      : { 'list' : new,      'str' : ','.join(new)      },
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
