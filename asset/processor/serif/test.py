
class Echo:
  @classmethod
  def process(self, resource, params):
    # {{{ replace ??? or any processing
    text = resource + params['text_given'] + ' hoge---- '
    # }}}
    return text
