#!/usr/bin/env python
# encoding: utf-8
# https://gist.github.com/yanofsky/5436496
import tweepy  # https://github.com/tweepy/tweepy
import csv
import auth_credentials as c




def user_informadtion(screen_name):
    auth = tweepy.OAuthHandler(c.consumer_key, c.consumer_secret)
    auth.set_access_token(c.access_token,c.access_token_secret)
    api = tweepy.API(auth)
    user = api.get_user(screen_name)
    print('User Screen Name: ' + user.screen_name)
    print('User Name: ' + user.name)
    print('User ID: ' + user.id_str)
    print('Location : ' + user.location)
    print('Description : ' + user.description)
    print('How many tweets : ' + str(user.statuses_count))
    print('Url : ' + user.url)
    print('How many followers : '+str(user.followers_count))
    print('How many friends : '+str(user.friends_count))
    for friend in user.friends():
        print('Following : '+friend.screen_name)

def get_all_tweets(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method
    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(c.consumer_key, c.consumer_secret)
    auth.set_access_token(c.access_token,c.access_token_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200,tweet_mode="extended")

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print(f"getting tweets before {oldest}")

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest,tweet_mode="extended")

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        # for reply in alltweets:
        #     # 提及user
        #     if hasattr(reply, 'quoted_status'):
        #         # print(reply.quoted_status.full_text)
        #         quote = reply.quoted_status.full_text
        #         alltweets.append(quote)
        #     elif hasattr(reply, 'reply_status'):
        #         # print(reply.reply_status.full_text)
        #         reply = reply.reply_status.full_text
        #         alltweets.append(reply)
        #
        #     else:
        #         alltweets.append("null")
        #     # print(alltweets)

        print(f"...{len(alltweets)} tweets downloaded so far")



        # transform the tweepy tweets into a 2D array that will populate the csv

        outtweets = [[tweet.id_str, tweet.created_at, tweet.full_text,tweet.truncated,tweet.retweet_count,tweet.favorite_count,reply] for tweet in alltweets]


        # write the csv
        with open(f'{screen_name}_tweets.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["id", "created_at", "text","truncated","retweet_count","favorite_count","reply"])
            writer.writerows(outtweets)
        # pass in the username of the account you want to download
        pass


if __name__ == '__main__':

    screen_name=[]
    screen_name.append()
    print(type(screen_name))
    # for screen_name in crawl_id:
    #     get_all_tweets('screen_name')