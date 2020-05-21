from nltk.twitter.common import json2csv
from nltk.twitter.common import json2csv_entities
from nltk.corpus import twitter_samples
from nltk.twitter import Query, Streamer, Twitter, TweetViewer, TweetWriter, credsfromfile
import pandas as pd

tw = Twitter()
tw.tweets(follow=['759251'], limit=10) # see what CNN is talking about