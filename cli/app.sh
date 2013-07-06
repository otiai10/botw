#!/bin/sh

print_help()
{
  echo "\tstate\t状態を見る"
  echo "\tstart\t起動"
  echo "\tstop\t終了"
  exit 0
}

# script for run the daemon
if [ $# -lt 1 ]; then
  print_help
fi

cur_date=`date '+%Y.%m%d'`
log_path='log/'$cur_date'.log'

case $1 in
  "start" )
    if [ $# -lt 2 ]; then
      python -B $PWD/app.py
    elif [ "$2" = "d" ]; then
      nohup python -B $PWD/app.py >> $log_path &
    else
      print_help
    fi
    sleep 1s
    break;;
  "stop" )
    ps aux | grep python | grep $PWD/app.py | grep -v grep | awk '{print $2}' | xargs kill -9
    sleep 1s
    break;;
  "state" ) ps aux | grep $PWD | grep -v grep
    break;;
  "help" )
    echo "\033[0;33m"
    print_help
    break;;
  * )
    print_help
esac
