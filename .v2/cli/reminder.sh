
if [ $# -lt 1 ]; then
  echo 'Invalid Option : this cli only called from cron'
  exit 1
fi

case $1 in
  "--daily")
    ~/.pyenv/versions/tool13.0721/bin/python ~/prj/python/hisyotan/app.py r daily
    break;;
  "--weekly")
    ~/.pyenv/versions/tool13.0721/bin/python ~/prj/python/hisyotan/app.py r weekly
    break;;
  *)
    break;;
esac
