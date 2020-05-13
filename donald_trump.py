import tweepy
from tweepy import OAuthHandler
import pandas as pd
from datetime import datetime
import credentials
# import  pymysql
import re
import csv
import json

# Twitter APIpip
auth = OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# 帳號=@realDonaldTrump, extended模式才能抓full_text
status = api.user_timeline('realDonaldTrump', tweet_mode="extended")
# print(status)
data=status[2]._json
abc = json.dumps(data,indent = 2)
print(abc)

# create_time = []
# user_name = []
# link_tweet = []
# tweet_content = []
# for i in range(0, len(status)):
#     # 日期轉換
#     t = status[i]._json['created_at'].replace('+0000 ', '')
#     t_format = datetime.strptime(t, "%a %b %d %H:%M:%S %Y")
#     create_time.append(t_format)
#
#     user_name.append(status[i]._json['user']['name'])
#     link_tweet.append('https://twitter.com/realDonaldTrump/status/' + status[i]._json['id_str'])
#     # 把多個空行轉成僅一個換行
#     tweet_content.append("\n".join(re.split(r"\n+", status[i]._json['full_text'])))
#
# twitter_table = pd.DataFrame({'Create Time': create_time,
#                               'User Name': user_name,
#                               'Tweet Content': tweet_content,
#                               'Link': link_tweet})
#
# twitter_table.to_csv('donaldtrump.csv', index=False, encoding='utf_8_sig')
