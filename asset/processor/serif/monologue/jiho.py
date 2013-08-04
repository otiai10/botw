class Jiho:
  @classmethod
  def process(self, resource, args):
    text = resource.replace('%{hour}', str(args['hour']))
    return text
