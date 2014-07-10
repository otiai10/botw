from system.logger import ExecBase

class Exec(ExecBase):

  location = 'error'
  fpath    = ''

  def __init__(self):
    self.fpath = self.of_current_path()
    pass

  def execute(self, value, opt=None):
    self.presentation(self._build(value))
    return True

  def _build(self, value):
    return self.header + str(value)
