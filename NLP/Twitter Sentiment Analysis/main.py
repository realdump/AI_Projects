from textblob import TextBlob
import tweepy
import sys

api_key= '7rhup8MGFp6NjeFnUOJZZECJ0'
api_key_secret = 'DNoB6mxXfpLhUhI9lkx8IIK734RIKF2EtJL2AXicNoL0AuZHWg'
access_token = '1788106167660503042-TpfCx39HxRMImJalONxcoskbUhH7ma'
access_token_secret = 'nXtsQCyNDGLiNLsgFxnv2NjkJqS3LW9TeNMhmzF3E5zfE'

auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret,)
auth_handler.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler)

search_term = 'stocks'

tweet_amount = 200

tweets = tweepy.Cursor(api.search_tweets, q=search_term, lang='en').items(tweet_amount)

for tweet in tweets:
    print(tweet.text)