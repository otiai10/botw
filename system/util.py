
def get_file_name(file__, contain_file_extension=False):
  if contain_file_extension:
    return file__.split('/')[-1]
  return file__.split('/')[-1].split('.')[0]
