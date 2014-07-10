import smtplib, traceback, datetime
from email.mime.text import MIMEText
from email.utils import formatdate
from system import conf,util
from twitter import *

rest = Twitter(auth=OAuth(
  conf.access_token_key,
  conf.access_token_secret,
  conf.consumer_key,
  conf.consumer_secret
))

class Alert:
  mail = {}
  def __init__(self, info=None, twtxt=None):
    self.mail = {
      'body'    : "ALERT OCCURED\n\n",
      'to'      : conf.alert['mail_to'],
      'from'    : conf.alert['mail_from'],
    }
    if twtxt is not None:
      self.mail['body'] = "HANDLING \t: \"" + twtxt + "\":\n"
    if info is not None:
      (ex, msg, tb) = info
      base_str  = "MESSAGE  \t: " + str(msg) + "\n"
      base_str += "TRACEBACK\t: " + "\n".join(traceback.format_tb(tb)) + "\n"
      self.mail['body'] += base_str

  def send_mail(self):
    try:
      s = smtplib.SMTP('localhost')
      s.connect()
      s.sendmail(
        to_addrs=self.mail['to'],
        from_addr=self.mail['from'],
        msg = self.mail['body'].encode('utf8')
      )
      s.close()
    except:
      # sending mail errors itself
      # write stdout log
      print("An Error Occurred But Failed to Sending Mail...[%s]" % util.get_timestr())
      pass
    # status = conf.admin_name + conf.alert_tw_prefix + util.get_timestr() # + self.mail['body'].replace('@','@\\')
    status = conf.admin_name + ' ' + util.get_timestr() + self.mail['body'].replace('@','@\\')
    rest.statuses.update(status=status[:139])

  def set_params(self):
    pass

if __name__ == '__main__':
  Alert().send_mail()
