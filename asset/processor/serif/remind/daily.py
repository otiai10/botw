
class Execute:
  @classmethod
  def process(self, resource, args):
    # {{{ replace ??? or any processing
    text = '@' + args['user']['name'] + ' '#TODO : DRY? or It's needed?
    text += resource
    # }}}
    return text
