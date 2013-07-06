import skel
from lib.twitter.bot import TwitterBot

class Hisyo(TwitterBot):

  def __init__(self,conf):
    self.conf = conf

  def listen(self):
    # entry = self.listen_user_stream()
    print 'Start listening...'
    self.tweet_hello()

def get(conf):
  return Hisyo(conf)
