import twitter
import time

from interpreter import Interpreter
from system import *

api = twitter.Api(
  consumer_key        = conf.consumer_key,
  consumer_secret     = conf.consumer_secret,
  access_token_key    = conf.access_token_key,
  access_token_secret = conf.access_token_secret,
)

class Skel:

  __name = ''
  __filters = ['Retweet','Myself']

  def __init__(self, name):
    self.__name = name

  def listen(self):

    last_got_id = None
    itr_count = 0

    while True:
      print "\n\n\n\n============= %i TRY =============" % itr_count
      print 'last_got_id is ', last_got_id, '...'

      timeline = api.GetHomeTimeline(since_id=last_got_id)
      timeline.reverse()
      for tweet in timeline:
        #try:
        self.tweet_by_tweet(tweet)
        #except Exception as e:
        #  print 'EXCEPTION raised ->'
        #  print e.message
        #  pass # log
      itr_count += 1
      timeline.reverse()
      if 0 < len(timeline):
        last_got_id = timeline[0].id

      time.sleep(120)
      # if some trigger:
      #   break

  # core function
  def tweet_by_tweet(self, tweet):
    if self.pass_this_tw(tweet):
      # ignore this
      return None
    context = self.interpret_this_tw(tweet)
    if context['proc'] is None:
      # ignore this
      return None
    res = self.proc_this_context(context)
    if res['resp'] is None:
      # do not reply
      return None
    msg_args = self.generate_reply_message(res)
    if msg_args['action'] is None:
      # do nothing
      return None
    result = self.dispatch_action(msg_args)
    print result , __file__
    return None

  def pass_this_tw(self, tweet):
    mod = __import__('filters',globals(),locals(), self.__filters, -1)
    for f in self.__filters:
      Fltr = getattr(mod, f)
      if Fltr.accept(tweet) is False:
        return True
    return False

  def interpret_this_tw(self,tweet):
    return Interpreter(tweet).execute()

  def proc_this_context(self, context):
    mod_name = context['proc']['module']
    cls_name = context['proc']['class']
    mod = __import__('.'.join(['procedure',mod_name]),globals(),locals(),[cls_name], -1)
    Proc = getattr(mod, cls_name)
    return Proc.perform(context['params'])

  def generate_reply_message(self, res):
    mod_name = res['resp']['module']
    cls_name = res['resp']['class']
    mod = __import__('.'.join(['response',mod_name]),globals(),locals(),[cls_name], -1)
    Resp = getattr(mod, cls_name)
    return Resp().generate(res['args'])

  def dispatch_action(self, args):
    if args['action'] == 'update_status':
      api.PostUpdate(args['message'])
    else:
      pass
    return 'DISPATCHED SUCCESSFULLY'
