#!/usr/bin/python3
from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class TwitterClient():
    def __init__(self):
        self.auth = TwitterAuthenticator().auth_twitter_app()
        self.twitter_client = API(self.auth)
    def get_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline).items(num_tweets):
            tweets.append(tweet)
        return tweets

class TwitterAuthenticator():

    def auth_twitter_app(self):
        """set consumer key and consumer secret"""
        auth = tweepy.OAuthHandler(CONSUMER KEY, CONSUMER SECRET)
        """set access token and token secret"""
        auth.set_access_token(ACCESS TOKEN, TOKEN SECRET)
        return auth

class TwitterStreamer():
    """class for streaming and processing live tweets"""
    def __init__(self):
        self.twitter_auth = TwitterAuthenticator()
    def stream_tweets(self, fetched_tweets_file, hashtag_list):
        listener = TwitterListener(fetched_tweets_file)
        auth = self.twitter_auth.auth_twitter_app()
        stream = Stream(auth, listener)

        stream.filter(track=hashtag_list)


class TwitterListener(StreamListener):

    def __init__(self, fetched_tweets_file):
        self.fetched_tweets_file = fetched_tweets_file

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_file, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        if status == 420:
            return False
        print(status)

if __name__ == "__main__":

    hashtag_list = ["iran", "Candiatestournament", "Firojza", "Carleson", "yanggang", "ww3"]
    fetched_tweets_file = "tweets.json"

    twitter_client = TwitterClient()
    print(twitter_client.get_tweets(1))
    #twitterstreamer = TwitterStreamer()
    #twitterstreamer.stream_tweets(fetched_tweets_file, hashtag_list)
