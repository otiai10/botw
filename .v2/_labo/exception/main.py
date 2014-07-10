import traceback,sys

try:
  {}.encode('utf8')
except:
  ex, ms, tb = sys.exc_info()
  print("\nex -> \t",type(ex))
  print(ex)
  print("\nms -> \t",type(ms))
  print(ms)
  print("\ntb -> \t",type(tb))
  print(tb)

  print("\n=== and print_tb ===")
  hoge = traceback.format_tb(tb)
  out = "\n".join(hoge) 
  print(out)
