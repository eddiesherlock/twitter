import tweepy
from tweepy import OAuthHandler
import auth_credentials

#帳號密碼處理
auth = OAuthHandler(auth_credentials.CONSUMER_KEY, auth_credentials.CONSUMER_SECRET)
auth.set_access_token(auth_credentials.ACCESS_TOKEN, auth_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)


# wait_on_rate_limit = True
# Whether or not to automatically wait for rate limits to replenish

# -  wait_on_rate_limit_notify = True
# Whether or not to print a notification when Tweepy is waiting for rate limits to replenish
# Using the API object to get tweets from your timeline
#
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# public_tweets = api.user_timeline('LeoDiCaprio')
# for tweet in public_tweets:
#     print(tweet.text)


tweepy.Cursor(api.user_timeline, id="twitter")

for status in tweepy.Cursor(api.home_timeline,133880286).items(1000):
    print(status._json)