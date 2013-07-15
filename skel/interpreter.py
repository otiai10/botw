from system import *

class Interpreter:

  __context = {
    'proc'   : {},
    'params' : {},
  }

  def __init__(self, tweet):
    self.tweet = tweet

  def execute(self):
    if self.tweet.in_reply_to_screen_name == conf.bot_name:
      if True:
        self.__context['proc']   = {'module':'test','class':'Echo'}
        self.__context['params'] = {
          'text_given' : self.tweet.text.replace(conf.at_bot_name,''),
          'user'       : self.tweet.user,
          'origin'     : self.tweet # TODO : remove unnecessary field
        }
    elif self.tweet.in_reply_to_screen_name is not None:
      print 'REPLY TO OTHER USER'
    #elif re.match(trigger_pattern,self.__tweet_text):
    #  pass
    else:
      self.__context['proc'] = None
    return self.__context
