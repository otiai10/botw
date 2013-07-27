from twitter import *
import time, smtplib, sys

from core.interpreter import Interpreter
from system import *

from asset import Asset

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

  with_init_tw = False
  __name    = ''
  __filters = ['Retweet','Myself']
  bot       = None

  def __init__(self, name):
    self.__name = name
    self.bot = dict(screen_name=name)

  def listen(self, with_init_tw=False):

    tl = strm.user(**self.bot)

    if with_init_tw:
      rest.statuses.update(status=Asset('serif').load('common','Initd').get_text())

    for t in tl:
      tw = util.convert_twitter_format(t)
      if tw['friends'] is not None:
        continue
      try:
        self.tweet_by_tweet(tw)
      except:
        info = sys.exc_info()
        Alert(info=info,twtxt=tw['text']).send_mail()

  def draw(self, opt={}):
    # TMP : ignore options
    count = 3
    tl = rest.statuses.home_timeline(count=count)
    print(type(tl))
    print(len(tl))
    for t in tl:
      tw = util.convert_twitter_format(t)
      self.tweet_by_tweet(tw)

  # core function
  def tweet_by_tweet(self, tweet):
    if self.pass_this_tw(tweet):
      return None
    context = self.interpret_this_tw(tweet)
    _executed = {}
    if context['proc'] is None:
      return None
    res = self.proc_this_context(context)
    _executed['Procedure'] = context['proc']
    if res['resp'] is None:
      return None
    msg_args = self.generate_reply_message(res)
    _executed['Response'] = res['resp']
    if msg_args['actions'] is None or len(msg_args['actions']) is 0:
      return None
    result = self.dispatch_action(msg_args)
    _executed['Actions'] = result
    print({'EXECUTED':_executed})
    return None

  def pass_this_tw(self, tweet):
    mod = __import__('core.filters',globals(),locals(), self.__filters)
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
    mod = __import__('.'.join(['core','procedure',mod_name]),globals(),locals(),[cls_name])
    Proc = getattr(mod, cls_name)
    return Proc.perform(context['params'])

  def generate_reply_message(self, res):
    mod_name = res['resp']['module']
    cls_name = res['resp']['class']
    mod = __import__('.'.join(['core','response',mod_name]),globals(),locals(),[cls_name])
    Resp = getattr(mod, cls_name)
    return Resp().generate(res['args'])

  def dispatch_action(self, args):
    _finally = []
    if 'update_status' in args['actions']     and args['message'] is not None:
      rest.statuses.update(status=args['message'], in_reply_to_status_id=args['origin']['id'])
      _finally.append('update_status')
    if 'friendships_create'  in args['actions'] and args['tw_id'] is not None:
      rest.friendships.create(id=args['tw_id'])
      _finally.append('friendships_create')
    if 'friendships_destroy' in args['actions'] and args['tw_id'] is not None:
      rest.friendships.destroy(id=args['tw_id'])
      _finally.append('friendships_destroy')
    return _finally
