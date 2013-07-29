
if [ $# -lt 1 ]; then
  echo 'Invalid Option : this cli only called from cron'
  exit 1
fi

case $1 in
  "--daily")
    python $PWD/remind.py --daily
    break;;
  "--weekly")
    python $PWD/remind.py --weekly
    break;;
  *)
    break;;
esac
