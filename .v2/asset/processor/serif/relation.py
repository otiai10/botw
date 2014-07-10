class Create:
  @classmethod
  def process(self, resource, args):
    text = '@' + args['user']['screen_name'] + ' '#TODO : DRY? or It's needed?
    text += resource.replace('%{command}', args['command'])
    return text

class AlreadyCreated:
  @classmethod
  def process(self, resource, args):
    text = '@' + args['user']['screen_name'] + ' '#TODO : DRY? or It's needed?
    text += resource.replace('%{command}', args['command'])
    return text

class Destroy:
  @classmethod
  def process(self, resource, args):
    text = '@' + args['user']['screen_name'] + ' '
    text += resource.replace('%{command}', args['command'])
    return text
