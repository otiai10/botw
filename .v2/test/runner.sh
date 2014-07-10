#!/bin/sh

print_help()
{
  echo "\tall\t\t: 全部実行"
  echo "\t{SOME KEYWORD}\t: asset/resource/test.tw.jsonを見てね"
  exit 0
}

# script for run the test
if [ $# -lt 1 ]; then
  print_help
fi

case $1 in
  "all" )
    python -B $PWD/app.py o all
    break;;
  * )
    python -B $PWD/app.py o $1
esac
