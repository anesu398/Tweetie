import tweepy
from textblob import TextBlob

# Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate to Twitter API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Function to post a tweet
def post_tweet(tweet_text):
    try:
        api.update_status(tweet_text)
        print("Tweet posted successfully!")
    except tweepy.TweepError as e:
        print(f"Error occurred: {e}")

# Function to like tweets containing a specific keyword
def like_tweets(keyword):
    tweets = api.search(q=keyword, count=10)
    for tweet in tweets:
        try:
            api.create_favorite(tweet.id)
            print(f"Liked tweet: {tweet.text}")
        except tweepy.TweepError as e:
            print(f"Error occurred: {e}")

# Function to perform sentiment analysis on a tweet
def analyze_sentiment(tweet_text):
    analysis = TextBlob(tweet_text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

# Example usage
if __name__ == "__main__":
    # Post a tweet
    post_tweet("Hello, Twitter! This is a test tweet.")

    # Like tweets containing the keyword "Python"
    like_tweets("Python")

    # Perform sentiment analysis on a tweet
    tweet_text = "I love using Python for automation tasks!"
    sentiment = analyze_sentiment(tweet_text)
    print(f"Sentiment of the tweet: {sentiment}")
