import tweepy
import os
import time


class Twitter:
    def __init__(self, consumer_key, consumer_key_secret, access_token, access_token_secret):
        authentication = tweepy.OAuthHandler(consumer_key, consumer_key_secret)

        authentication.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(authentication)

    def create_cursor(self, query):
        return tweepy.Cursor(self.api.search, q=query, lang="id", tweet_mode="extended")

    def limit_handled(self, cursor):
        while True:
            try:
                yield cursor.next()
            except tweepy.TweepError:
                print("Rate limit exceeds, start sleeping...")
                time.sleep(15 * 60)
                print("Starting again...")
