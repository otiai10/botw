import time, sys
import filters

import twitter

from system import *

api = twitter.Api(
  consumer_key        = conf.consumer_key,
  consumer_secret     = conf.consumer_secret,
  access_token_key    = conf.access_token_key,
  access_token_secret = conf.access_token_secret,
)

class Skel:

  __name = ''
  __filters = ['Retweet']

  def __init__(self, name):
    self.__name = name

  def listen(self):

    while True:
      timeline = api.GetUserTimeline(screen_name='hisyotan')
      for tweet in timeline:
        try:
          self.tweet_by_tweet(tweet)
        except:
          # log
          pass
      break
      #time.sleep(65)

  def tweet_by_tweet(self, tweet):
    if self.pass_this_tw(tweet):
      return None
    # do not pass
    print tweet

  def pass_this_tw(self, tweet):
    mod = __import__('filters',globals(),locals(), self.__filters, -1)
    for f in self.__filters:
      Fltr = getattr(mod, f)
      if Fltr.accept(tweet) is False:
        return True
    return False
