import os
import tweepy as tw
import pandas as pd
## Tutorial url ="https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/twitter-data-in-python/"

ACCESS_TOKEN = '1258014133355601921-SrqKg58eix8S498iIsRUX67UOXe0tl'
ACCESS_TOKEN_SECRET = 'iVHGL1LhXCtjpB1AzwFa2D9F1tnUcdurwbW1AvNo7Xlpi'
CONSUMER_KEY = 'lyeoTefgEtw7c0F8BnEZyFlfj'
CONSUMER_SECRET = 'NwCDXgGlrRag1e6v17zb5xxGu8uiRkPpfvV4ZwD0RljVFOX89d'

auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tw.API(auth, wait_on_rate_limit=True)

# Post a tweet from Python
# api.update_status("Look, I'm tweeting from #Python in my #earthanalytics class! @EarthLabCU")
# Your tweet has been posted!

search_words = "#MLB"
# date_since = "2018-04-02"
#
# tweets = tw.Cursor(api.search,
#               q=search_words,
#               lang="en",
#               since=date_since).items(5)
# # print(tweets)
#
# # Collect tweets
# tweets = tw.Cursor(api.search,
#               q=search_words,
#               lang="en",
#               since=date_since).items(5)
#
# # Iterate and print tweets
# # for tweet in tweets:
# #     print(tweet.text)

# # Collect tweets
# tweets = tw.Cursor(api.search,
#                        q=search_words,
#                        lang="en",
#                        since='2018-04-02').items(5)
# # Collect a list of tweets
# abc = [tweet.text for tweet in tweets]
# print(abc)

new_search = search_words + " -filter:retweets"
print(new_search)
tweets = tw.Cursor(api.search,
                       q=new_search,
                       lang="en",
                       since='2020-05-18').items(1000)

users_locs = [[tweet.user.screen_name, tweet.user.location,tweet.created_at] for tweet in tweets]
# print(users_locs)

tweet_text = pd.DataFrame(data=users_locs,
                    columns=['user', "location","date"])
print(tweet_text)

# new_search = "climate+change -filter:retweets"

# tweets = tw.Cursor(api.search,
#                    q=new_search,
#                    lang="en",
#                    since='2018-04-02').items(5)
#
# all_tweets = [tweet.text for tweet in tweets]
# print(all_tweets)