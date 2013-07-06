class TwitterBot:
  conf = {}

  def tweet_hello(self):
    print 'tweet_hello!! TW_APP_CONSUMER_KEY is => %s' % self.conf['twitter']['TW_APP_CONSUMER_KEY']
