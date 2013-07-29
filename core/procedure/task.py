from pymongo import MongoClient
from system import conf, util
from core.procedure.base import ProcedureBase

client = MongoClient(conf.mongo['host'],conf.mongo['port'])
db = client.test
collection = db.masters

class List(ProcedureBase):
  def perform(self, context):
    master = collection.find({'name':context['user']['screen_name']})
    if master.count() is 1:
      m = master[0]
      if len(m['tasks']) == 0:
        self._response['resp']['module'] = 'task'
        self._response['resp']['class']  = 'Empty'
        self._response['args'] = {
          'user'      : context['user'],
          'origin'    : context['origin'],
          'command'   : context['command'],
        }
      else: 
        tasks_str = ','.join(m['tasks'])
        self._response['resp']['module'] = 'task'
        self._response['resp']['class']  = 'List'
        self._response['args'] = {
          'user'      : context['user'],
          'origin'    : context['origin'],
          'tasks_str' : tasks_str,
          'command'   : context['command'],
        }
    else:
      return self.res_common_help()
    return self._response

class Add(ProcedureBase):
  def perform(self, context):
    master = collection.find({'name':context['user']['screen_name']})
    # """ print dir(master) """
    if master.count() is 1:
      m = master[0]
      old = m['tasks']
      added = util.split_by_delimiter(context['origin']['text'])
      added.remove(conf.at_bot_name)
      while True:
        if context['command'].strip(util.delimiter) in added:
          added.remove(context['command'].strip(util.delimiter))
        else:
          break

      cur = old + added

      m['tasks'] = cur
      collection.save(m)

      # TODO: DRY
      self._response['resp']['module'] = 'task'
      self._response['resp']['class']  = 'Add'
      self._response['args'] = {
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
      return self.res_common_help()
    return self._response

class Done(ProcedureBase):
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

      (done, notfound, new) = self.rebuild_tasks(m['tasks'], tasks_from_text)

      # update record
      m['tasks'] = new
      collection.save(m)

      self._response['resp']['module'] = 'task'
      self._response['resp']['class']  = 'Done'

      self._response['args'] = {
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
      return self.res_common_help()
    return self._response

class Clear(ProcedureBase):
  def perform(self, context):
    master = collection.find({'name':context['user']['screen_name']})
    if master.count() is 1:
      m = master[0]
      m['tasks'] = []
      collection.save(m)
      self._response['resp']['module'] = 'task'
      self._response['resp']['class']  = 'Clear'

      self._response['args'] = {
        'user'      : context['user'],
        'origin'    : context['origin'],
        'command'   : context['command'],
      }
    else:
      return self.res_common_help()
    return self._response
