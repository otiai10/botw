from system import *
from asset import Asset
import re

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
        }
    elif self.tweet.in_reply_to_screen_name is not None:
      # print 'REPLY TO OTHER USER'
      # ignore
      pass
    elif self.contain_trigger_word():
      pass
    else:
      self.__context['proc'] = None

    self.__context['params']['user'] = {
      'screen_name' : self.tweet.user.screen_name,
      # add another attributes if needed
    }
    self.__context['params']['origin'] = self.tweet # TODO : remove unnecessary field

    return self.__context

  def contain_trigger_word(self):
    triggers = Asset('trigger').get_dict()
    for k,proc in triggers.items():
      if re.match(k, self.tweet.text):
        self.__context['proc'] = triggers[k]
        self.__context['params'] = {
          'trigger_word' : k,
        }
        return True
      else:
        self.__context['proc'] = None
    return False
