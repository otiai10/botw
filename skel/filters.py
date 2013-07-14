# print tweet
# print tweet.created_at
# print tweet.favorited
# print tweet.id
# print tweet.in_reply_to_screen_name
# print tweet.in_reply_to_status_id
# print tweet.in_reply_to_user_id
# print tweet.text.encode('utf8')
# print tweet.retweeted
# print tweet.source.encode('utf8')
# print tweet.user
# print tweet.user_mentions
from system import *

class Retweet:
  @classmethod
  def accept(self, tweet):
    if tweet.retweeted is True or 0 < tweet.retweet_count:
      print "\nThis is Retweeted entry!!!!!\n"
      return False
    return True

class Myself:
  @classmethod
  def accept(self, tweet):
    if tweet.user.screen_name == conf.bot_name:
      print "\nThis is tweeted by My Self!!!!!\n"
      return False
    return True
