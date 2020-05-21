import tweepy
from tweepy import OAuthHandler
import auth_credentials

#帳號密碼處理
auth = OAuthHandler(auth_credentials.CONSUMER_KEY, auth_credentials.CONSUMER_SECRET)
auth.set_access_token(auth_credentials.ACCESS_TOKEN, auth_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# 利用tweepy發文
api.update_status("")
print("done!!")

# # Get the User object for twitter...
# user = api.get_user('twitter')
# print(user.screen_name)
# print(user.followers_count)
# for friend in user.friends():
#    print(friend.screen_name)





