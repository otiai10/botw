# basic
from datetime import *
import time
# this topic
import twitter
# my
from system import conf

api = twitter.Api(
  consumer_key        = conf.consumer_key,
  consumer_secret     = conf.consumer_secret,
  access_token_key    = conf.access_token_key,
  access_token_secret = conf.access_token_secret,
)
# This is confirmation of App Verification
# print api.VerifyCredentials()

def tweet_test():
  timestamp = time.mktime(datetime.now().timetuple())
  status = api.PostUpdate("Hi, This is test tweet using python-twitter!! and TS = %s" % str(timestamp))
  print "Tweet Post result :\t%s" % status.text

def timeline_test():
  statuses = api.GetUserTimeline(
    screen_name='hisyotan'
  )
  print '>>> TimeLine >>>'
  for s in statuses:
    print s.text.encode('utf8')

if __name__ == '__main__':
  tweet_test()
  timeline_test()

# tl = rest.statuses.mentions_timeline
# tl = rest.statuses.user_timeline
# tl = rest.statuses.home_timeline(**self.bot)
