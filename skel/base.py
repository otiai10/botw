from twitter import *
import time, smtplib

from skel.interpreter import Interpreter
from system import *

rest = Twitter(auth=OAuth(
  conf.access_token_key,
  conf.access_token_secret,
  conf.consumer_key,
  conf.consumer_secret
))
strm = TwitterStream(auth=OAuth(
  conf.access_token_key,
  conf.access_token_secret,
  conf.consumer_key,
  conf.consumer_secret
))

class Skel:

  __name = ''
  __filters = ['Retweet','Myself']

  def __init__(self, name):
    self.__name = name

  def listen(self):

    last_got_id = None
    itr_count = 0

    bot = dict(screen_name=conf.bot_name)
    tl = strm.user(**bot)
    for t in tl:
      tw = util.convert_twitter_format(t)
      if tw['friends'] is not None:
        continue
      try:
        self.tweet_by_tweet(tw)
      except Exception as err:
        Alert(e=err,twtxt=tw['text']).send_mail()

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
    print(result)
    return None

  def pass_this_tw(self, tweet):
    mod = __import__('skel.filters',globals(),locals(), self.__filters)
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
    mod = __import__('.'.join(['skel','procedure',mod_name]),globals(),locals(),[cls_name])
    Proc = getattr(mod, cls_name)
    return Proc.perform(context['params'])

  def generate_reply_message(self, res):
    mod_name = res['resp']['module']
    cls_name = res['resp']['class']
    mod = __import__('.'.join(['skel','response',mod_name]),globals(),locals(),[cls_name])
    Resp = getattr(mod, cls_name)
    return Resp().generate(res['args'])

  def dispatch_action(self, args):
    if args['action'] == 'update_status':
      # rest.statuses.update(args['message'], in_reply_to_status_id=args['origin'].id)
      rest.statuses.update(status=args['message'], in_reply_to_status_id=args['origin']['id'])
    else:
      pass
    return 'DISPATCHED SUCCESSFULLY'
