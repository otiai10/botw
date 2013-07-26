class List:
  @classmethod
  def process(self, resource, args):
    text = '@' + args['user']['screen_name'] + ' '#TODO : DRY? or It's needed?
    text += resource.replace('%{command}', args['command'])
    text = text.replace('%{tasks_str}', args['tasks_str'])
    return text

class Empty:
  @classmethod
  def process(self, resource, args):
    text = '@' + args['user']['screen_name'] + ' '#TODO : DRY? or It's needed?
    text += resource.replace('%{command}', args['command'])
    return text

class Add:
  @classmethod
  def process(self, resource, args):
    text = '@' + args['user']['screen_name'] + ' '
    text += resource.replace('%{command}', args['command'])
    text = text.replace('%{added}', args['tasks']['added']['str'])
    text = text.replace('%{old}', args['tasks']['old']['str'])
    text = text.replace('%{total}', str(len(args['tasks']['current']['list'])))
    return text

class Complete:
  @classmethod
  def process(self, resource, args):
    text = '@' + args['user']['screen_name'] + ' '
    text += resource.replace('%{command}', args['command'])
    text = text.replace('%{done}', args['tasks']['done']['str'])
    return text

class Done:
  @classmethod
  def process(self, resource, args):
    text = '@' + args['user']['screen_name'] + ' '
    text += resource.replace('%{command}', args['command'])
    text = text.replace('%{done}', args['tasks']['done']['str'])
    return text

class Notfound_Without_Done:
  @classmethod
  def process(self, resource, args):
    text = '@' + args['user']['screen_name'] + ' '
    text += resource.replace('%{command}', args['command'])
    text = text.replace('%{notfound}', args['tasks']['notfound']['str'])
    return text

class Done_With_Notfound:
  @classmethod
  def process(self, resource, args):
    text = '@' + args['user']['screen_name'] + ' '
    text += resource.replace('%{command}', args['command'])
    text = text.replace('%{done}', args['tasks']['done']['str'])
    text = text.replace('%{notfound}', args['tasks']['notfound']['str'])
    text = text.replace('%{new}', args['tasks']['new']['str'])
    return text

class Clear:
  @classmethod
  def process(self, resource, args):
    text = '@' + args['user']['screen_name'] + ' '
    text += resource.replace('%{command}', args['command'])
    return text
