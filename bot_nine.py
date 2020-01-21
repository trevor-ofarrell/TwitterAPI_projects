#!/usr/bin/python3
import tweepy

"""set consumer key and consumer secret"""
auth = tweepy.OAuthHandler(CONSUMER KEY, CONSUMER SECRET)

"""set access token and token secret"""
auth.set_access_token(ACCESS TOKEN, TOKEN SECRET)

api = tweepy.API(auth, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("verification approved")

except:
    print("Error during authentication")

"""query twitter api for various keywords and like the posts"""
qss = ["python", "lichess", "junior dev", "python", "node.js", "holberton school",
      "coding bootcamp", "tech internship", "flutter", "node js express", "chess"]
try:
    for tweet in api.search(q=qs, lang="en", rpp=1000):
        if not tweet.favorited:
            api.create_favorite(tweet.id)
            print("tweet liked")
        else:
            print("tweet already liked")
except tweepy.RateLimitError:
    print("rate exceeded")
    time.sleep(60)
except:
    pass
