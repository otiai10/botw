
def get_file_name(file__, contain_file_extension=False):
  if contain_file_extension:
    return file__.split('/')[-1]
  return file__.split('/')[-1].split('.')[0]

def convert_twitter_format(tw):
  return _convert_v1(tw)

def _convert_v1(tw):
  result = {
    'user' : {},
    'text' : '',
    'friends' : None,
    'retweeted' : False,
    'retweet_count' : 0,
    'in_reply_to_screen_name' : '',
    'id' : '',
  }
  #for k,v in tw.items():
  #  if k == 'retweeted' or k == 'retweet_count':
  #    print(v)

  # implementation
  for k,v in result.items():
    if (k in tw.keys()):
      result[k] = tw[k]
  return result
