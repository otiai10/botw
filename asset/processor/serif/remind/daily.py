
class Execute:
  @classmethod
  def process(self, resource, args):
    # {{{ replace ??? or any processing
    text = '@' + args['user']['name'] + ' '#TODO : DRY? or It's needed?
    text += resource
    text = text.replace('%{tasks_str}', args['tasks_str'])
    # }}}
    return text

class Enable:
  @classmethod
  def process(self, resource, args):
    # {{{ replace ??? or any processing
    text = '@' + args['user']['screen_name'] + ' '#TODO : DRY? or It's needed?
    text += resource
    # }}}
    return text

class Disable:
  @classmethod
  def process(self, resource, args):
    # {{{ replace ??? or any processing
    text = '@' + args['user']['screen_name'] + ' '#TODO : DRY? or It's needed?
    text += resource
    # }}}
    return text
