
def get_file_name(file__, contain_file_extension=False):
  if contain_file_extension:
    return file__.split('/')[-1]
  return file__.split('/')[-1].split('.')[0]

def convert_twitter_format(tw):
  return _convert_v1(tw)

def _convert_v1(tw):
  return tw
