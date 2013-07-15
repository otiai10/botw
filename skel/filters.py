#  tweet
#  tweet.created_at
#  tweet.favorited
#  tweet.id
#  tweet.in_reply_to_screen_name
#  tweet.in_reply_to_status_id
#  tweet.in_reply_to_user_id
#  tweet.text.encode('utf8')
#  tweet.retweeted
#  tweet.source.encode('utf8')
#  tweet.user
#  tweet.user_mentions
from system import *

class Retweet:
  @classmethod
  def accept(self, tweet):
    if tweet.retweeted is True or 0 < tweet.retweet_count:
      print "This is Retweeted entry!!!!!"
      return False
    return True

class Myself:
  @classmethod
  def accept(self, tweet):
    if tweet.user.screen_name == conf.bot_name:
      print "This is tweeted by My Self!!!!!"
      return False
    return True
