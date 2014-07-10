from system import conf,util
import datetime,os

class Logger:
  executor = object
  def __init__(self, logtype):
    mod = __import__('system.logger.' + logtype ,globals(),locals, ['Exec'])
    self.executor = getattr(mod, 'Exec')

  def execute(self, value, opt=None):
    return self.executor().execute(value, opt)

class ExecBase:
  logfroot = conf.app_root + '/log/'
  header   = util.get_timestr()
  def __init__(self):
    pass

  def of_current_path(self):
    d = datetime.datetime.today()
    base = self.logfroot + self.location + '/'
    fdir = base + '{d.year}/{d.month:02}/{d.day:02}/'.format(d=d)
    if not os.path.exists(fdir):
      os.makedirs(fdir)
    return  fdir + '{d.hour:02}'.format(d=d) + '.log'

  def presentation(self,value):
    f = open(self.fpath, 'a', encoding='utf8')
    f.write(value + "\n")
    f.close()
