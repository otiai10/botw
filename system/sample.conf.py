from os.path import dirname
app_root = dirname(dirname(__file__))

admin_name = '@otiai10'
alert_tw_prefix = " [[ ALERT ]] I can't handle some tweets..., please look at the mail from me"

consumer_key        = 'XXXXXXXXXXXXXXXXXXX'
consumer_secret     = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_key    = '00000000-zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
access_token_secret = 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ'

mongo = {
  'host'           : 'some.db.host.net',
  'port'           : 0000,
  'dbname'         : 'YOURDBNAME',
  'collectionname' : 'YOURCOLLECTIONNAME',
}

bot_name    =  'hisyotan'
at_bot_name = '@hisyotan'

alert = {
  'mail_to' : [
    'alert.notify.adress@host.com'
  ],
  'mail_from' : 'hisyotan@host.com',
}

# execution rate of monologu
# for each cron call
monologue_rate = 0.01
