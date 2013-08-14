from twitter import *
import sys,os,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.append(os.getcwd())

from system import conf

class CliToolBase:
  arg_list = {}
  def __init__(self):
    self.rest_api = Twitter(auth=OAuth(
      conf.access_token_key,
      conf.access_token_secret,
      conf.consumer_key,
      conf.consumer_secret
    ))
    self.parse_args()

  def parse_args(self):
    if '--help' in sys.argv:
      self.show_help()
      sys.exit()
    if 1 < len(sys.argv):
      _list = sys.argv[1:]
      for k_v in _list:
        (k,v) = k_v.split('=')
        self.arg_list[k] = v
