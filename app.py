# main process
import System
import skel

conf     = System.Config.get()
hisyotan = skel.get(conf)
hisyotan.listen()
