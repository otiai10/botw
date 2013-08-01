class Default:
  @classmethod
  def process(self, resource, args):
    # {{{ replace ??? or any processing
    text = '@' + args['user']['screen_name'] + ' '#TODO : DRY? or It's needed?
    text += resource.replace('%{trigger_word}', args['trigger_word'])
    # }}}
    return text
