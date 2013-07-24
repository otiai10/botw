import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
from system import conf,util

class Alert:
  mail = {}
  def __init__(self, e=None, twtxt=None):
    self.mail = {
      'body'    : 'ALERT OCCURED',
      'to'      : conf.alert['mail_to'],
      'from'    : conf.alert['mail_from'],
    }
    if twtxt is not None:
      #self.mail['body'] = u"Cannot handle : " + twtxt
      self.mail['body'] = twtxt
    if e is not None:
      pass
      """
      base_str = ''
      base_str += "Type\t" + str(type(e)) + "\n"
      base_str += "Args\t" + str(e.args)  + "\n"
      base_str += "Mess\t" + e.message    + "\n\n"
      base_str += "Err\t"  + str(e) + "\n"
      self.mail['body'] = base_str
      """

  def send_mail(self):
    try:
      s = smtplib.SMTP('localhost')
      s.connect()
      s.sendmail(
        to_addrs=self.mail['to'],
        from_addr=self.mail['from'],
        msg=self.mail['body']
      )
      s.close()
    except:
      # sending mail errors itself
      # write stdout log
      print("An Error Occurred But Failed to Sending Mail...[%s]" % util.get_timestr())
      pass

  def set_params(self):
    pass

if __name__ == '__main__':
  Alert().send_mail()
