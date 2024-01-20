from flask import Flask, request, jsonify
import tweepy
import praw
import json
import os

app = Flask(__name__)

def twitter_post(auth_details, post):
    # Initialize Tweepy Client with bearer token
    client = tweepy.Client(bearer_token=auth_details['bearer_token'],
                           consumer_key=auth_details['consumer_key'],
                           consumer_secret=auth_details['consumer_secret'],
                           access_token=auth_details['access_token'],
                           access_token_secret=auth_details['access_token_secret'])

    try:
        # Post the tweet
        response = client.create_tweet(text=post)
        return True
    except Exception as e:
        print(f"Twitter error: {e}")
        return False

    

def reddit_post(auth_details, post):
    reddit = praw.Reddit(client_id=auth_details['client_id'],
                         client_secret=auth_details['client_secret'],
                         user_agent=auth_details['user_agent'],
                         username=auth_details['username'],
                         password=auth_details['password'])

    try:
        title = ' '.join(post.split()[:4])
        reddit.subreddit(auth_details['subreddit']).submit(title, selftext=post)
        return True
    except Exception as e:
        print(f"Reddit error: {e}")
        return False

@app.route('/', methods=['POST'])
def post_to_platforms():
    post_content = request.data.decode('utf-8')
    result = {}

    # Check and post to Twitter if config exists
    if os.path.exists('twitter.conf'):
        with open('twitter.conf', 'r') as file:
            twitter_conf = json.load(file)
        result['twitter'] = twitter_post(twitter_conf, post_content)

    # Check and post to Reddit if config exists
    if os.path.exists('reddit.conf'):
        with open('reddit.conf', 'r') as file:
            reddit_conf = json.load(file)
        result['reddit'] = reddit_post(reddit_conf, post_content)

    return jsonify({"result": result}), 200

if __name__ == '__main__':
    app.run(debug=True)
