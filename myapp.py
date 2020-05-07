import tweepy
from tweepy import OAuthHandler
import credentials

#帳號密碼處理
auth = OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# 利用tweepy發文
api.update_status("我是劉碩傑*2222")
print("done!!")

# # Get the User object for twitter...
# user = api.get_user('twitter')
# print(user.screen_name)
# print(user.followers_count)
# for friend in user.friends():
#    print(friend.screen_name)





