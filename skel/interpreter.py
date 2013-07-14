from system import *

class Interpreter:

  __context = {
    'proc'   : {},
    'params' : {},
  }

  __user_name  = ''
  __tweet_text = ''
  __in_reply   = ''

  def __init__(self, tweet):
    self.__user_name = tweet.user.screen_name
    self.__tweet_text = tweet.text
    self.__in_reply  = tweet.in_reply_to_screen_name

  def execute(self):
    if self.__in_reply == conf.bot_name:
      if True:
        self.__context['proc']   = {'module':'test','class':'Echo'}
        self.__context['params'] = {
          'text_given' : self.__tweet_text.replace(conf.at_bot_name,''),
        }
    elif self.__in_reply is not None:
      print 'REPLY TO OTHER USER'
    #elif re.match(trigger_pattern,self.__tweet_text):
    #  pass
    else:
      self.__context['proc'] = None
    return self.__context
