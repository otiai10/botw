from base import CliToolBase

class Main(CliToolBase):
  def __init__(self):

    super(Main, self).__init__()
    self.validate_args()

    statuses = self.rest_api.GetUserTimeline(
      screen_name= self.arg_list['screen_name'],
      count      = self.arg_list['count'],
      scince_id  = self.arg_list['scince_id']
    )

    for st in statuses:
      print("[%s] %s" % (st['created_at'], st))

  def validate_args(self):
    if 'screen_name' not in self.arg_list:
      self.arg_list['screen_name'] = 'otiai10'
    if 'count' not in self.arg_list:
      self.arg_list['count'] = 5
    if 'scince_id' not in self.arg_list:
      self.arg_list['scince_id'] = None

  def show_help(self):
    print('Usage:')
    print('\tpython cli/tools/tl_manager.py screen_name={screen_name} [options]')
    print('Options:')
    print('\tscreen_name=otiai10')
    print('\tcount=5')
    print('\tscince_id=365461677765967872')

if __name__ == '__main__':
  Main()
