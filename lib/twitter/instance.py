class TwitterBot:
  conf = {}
  def __init__(self, conf):
    self.conf = conf
    pass

  def say_hello(self):
    print 'hello;'

def get(conf):
  return TwitterBot(conf)
