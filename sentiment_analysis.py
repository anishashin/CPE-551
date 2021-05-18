import re
import tweepy
import textblob
import matplotlib.pyplot
from config import consumer_key, consumer_secret, access_token, access_token_secret

def display_pie_chart(trump_tweets, biden_tweets):
    labels = ['Positive', 'Negative', 'Neutral']
    colors = ['green', 'red', 'blue']
    
    matplotlib.pyplot.figure(0)
    values = [trump_tweets[0], trump_tweets[1], trump_tweets[2]]
    matplotlib.pyplot.pie(values, colors = colors, startangle = 90, autopct = '%1.1f%%')
    matplotlib.pyplot.legend(labels)
    matplotlib.pyplot.title('Sentiment Analysis Result for Donald Trump')
    
    matplotlib.pyplot.figure(1)
    values = [biden_tweets[0], biden_tweets[1], biden_tweets[2]]
    matplotlib.pyplot.pie(values, colors = colors, startangle = 90, autopct = '%1.1f%%')
    matplotlib.pyplot.legend(labels)
    matplotlib.pyplot.title('Sentiment Analysis Result for Joe Biden')
    matplotlib.pyplot.show()

def get_sentiment(tweet):
    tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    result = textblob.TextBlob(tweet)
    if result.sentiment.polarity > 0:
        return 'positive'
    elif result.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'

def get_tweets(q, count):
    tweets = []
    fetched_tweets = api.search(q = q, count = count)
    for tweet in fetched_tweets:
        tweets.append(get_sentiment(tweet.text))
    return tweets

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    trump_tweets = get_tweets('donald trump -filter:retweets', 1000)
    ptweets = [tweet for tweet in trump_tweets if tweet == 'positive']
    ntweets = [tweet for tweet in trump_tweets if tweet == 'negative']
    trump_tweets = [len(ptweets), len(ntweets), len(trump_tweets) - len(ptweets) - len(ntweets)]

    biden_tweets = get_tweets('joe biden -filter:retweets', 1000)
    ptweets = [tweet for tweet in biden_tweets if tweet == 'positive']
    ntweets = [tweet for tweet in biden_tweets if tweet == 'negative']
    biden_tweets = [len(ptweets), len(ntweets), len(biden_tweets) - len(ptweets) - len(ntweets)]

    display_pie_chart(trump_tweets, biden_tweets)
