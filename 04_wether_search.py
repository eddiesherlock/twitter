import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import collections

import tweepy as tw
import nltk
from nltk.corpus import stopwords
import re
import networkx

import warnings
warnings.filterwarnings("ignore")

sns.set(font_scale=1.5)
sns.set_style("whitegrid")

ACCESS_TOKEN = '1258014133355601921-SrqKg58eix8S498iIsRUX67UOXe0tl'
ACCESS_TOKEN_SECRET = 'iVHGL1LhXCtjpB1AzwFa2D9F1tnUcdurwbW1AvNo7Xlpi'
CONSUMER_KEY = 'lyeoTefgEtw7c0F8BnEZyFlfj'
CONSUMER_SECRET = 'NwCDXgGlrRag1e6v17zb5xxGu8uiRkPpfvV4ZwD0RljVFOX89d'

auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tw.API(auth, wait_on_rate_limit=True)

search_term = "#climate+change -filter:retweets"

tweets = tw.Cursor(api.search,
                   q=search_term,
                   lang="en",
                   since='2018-11-01').items(1000)

all_tweets = [tweet.text for tweet in tweets]

print(all_tweets[:5])

def remove_url(txt):
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())
    """Replace URLs found in a text string with nothing
    (i.e. it will remove the URL from the string).

    Parameters
    ----------
    txt : string
        A text string that you want to parse and remove urls.

    Returns
    -------
    The same txt string with url's removed.
    """

all_tweets_no_urls = [remove_url(tweet) for tweet in all_tweets]
# print(all_tweets_no_urls[:5])
print(all_tweets_no_urls[0].split())