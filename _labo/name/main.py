from os.path import *
from system import conf

class Echo:

  def __init__(self, key):
    print key

    print "__file__ %s" % __file__
    #print "__module__ %s" % __module__
    print "__name__ %s" % __name__
    print self.__class__.__name__

    print __file__.split('/')[-1].split('.')[0]

    print dirname(dirname(__file__))

    print 'app_root ', conf.app_root

if __name__ == '__main__':
  c = Echo('hoge')
