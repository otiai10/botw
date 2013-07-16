
class List:
  @classmethod
  def process(self, resource, args):
    # {{{ replace ??? or any processing
    text = '@' + args['user']['screen_name'] + ' '#TODO : DRY? or It's needed?
    text += resource.replace('%{command}', args['command'])
    text = text.encode('utf8') + args['tasks_str']
    # }}}
    return text
