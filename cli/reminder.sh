
if [ $# -lt 1 ]; then
  echo 'Invalid Option : this cli only called from cron'
  exit 1
fi

python $PWD/remind.py --daily
