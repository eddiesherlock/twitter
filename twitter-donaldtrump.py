from nltk.twitter.common import json2csv
from nltk.twitter.common import json2csv_entities
from nltk.corpus import twitter_samples
from nltk.twitter import Query, Streamer, Twitter, TweetViewer, TweetWriter, credsfromfile
import pandas as pd

oauth = credsfromfile()
n = 10  # 設定拿取 tweets 資料則數
username = 'realDonaldTrump'

# Query
client = Query(**oauth)  # 歷史資料
client.register(TweetWriter())  # 寫入
client.user_tweets(username, n)  # 拿取 tweets 資料(n則)

'''
使用 json2csv 存取 tweets 資料 (text欄位)
input_file 的 abspath 需參考上述 Query 寫入資料的路徑做修改
'''

input_file = twitter_samples.abspath('/Users/youngmihuang/twitter-files/tweets.20180726-155316.json')
with open(input_file) as fp:
    json2csv(fp, 'tweets_text.csv', ['text'])

# 讀取
data = pd.read_csv('tweets_text.csv')
for line in data.text:
    print('Trump tweets content: ')
    print(line)

# 斷詞
tokenized = twitter_samples.tokenized(input_file)
for tok in tokenized[:5]:
    print('tokenized: ')
    print(tok)

# tweets 資料處理
with open(input_file) as fp:
    json2csv_entities(fp, 'tweets.20180726-155316.hashtags.csv',
                      ['id', 'text'], 'hashtags', ['text'])

with open(input_file) as fp:
    json2csv_entities(fp, 'tweets.20180726-155316.user_mentions.csv',
                      ['id', 'text'], 'user_mentions', ['id', 'screen_name'])

with open(input_file) as fp:
    json2csv_entities(fp, 'tweets.20180726-155316.media.csv',
                      ['id'], 'media', ['media_url', 'url'])

with open(input_file) as fp:
    json2csv_entities(fp, 'tweets.20180726-155316.urls.csv',
                      ['id'], 'urls', ['url', 'expanded_url'])
