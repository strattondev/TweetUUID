import tweepy

if __name__ == "__main__":
    try:
        from config import CONFIG_TWITTER
    except Exception, e:    
        CONFIG_TWITTER = None

    if CONFIG_TWITTER and "key" in CONFIG_TWITTER and "secret" in CONFIG_TWITTER:
        consumer_key = CONFIG_TWITTER['key'].strip()
        consumer_secret = CONFIG_TWITTER['secret'].strip()
    else:
        consumer_key = raw_input('Consumer key: ').strip()
        consumer_secret = raw_input('Consumer secret: ').strip()

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # Open authorization URL in browser
    print "Please go to {} to get authorization PIN".format(auth.get_authorization_url())

    # Ask user for verifier pin
    pin = raw_input('Verification PIN: ').strip()

    # Get access token
    token = auth.get_access_token(verifier=pin)
    print token
    # Give user the access token
    print 'Access token:'
    print '  Key: %s' % token[0]
    print '  Secret: %s' % token[1]