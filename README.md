
# AI Poster

A web service that can do posts to **twitter** or **reddit**

The body of the POST is the content of the post to make.


---

## Install

```
python3 -m pip install flask
python3 -m pip install tweepy
python3 -m pip install praw
python3 -m pip install json
```

## Setup

Create the files `twitter.conf` and `reddit.conf` based on the corresponding `example.twitter.conf` and `example.reddit.conf`

And then go to https://developer.twitter.com/en/portal/dashboard    
and https://www.reddit.com/prefs/apps

## Run

```
python3 ai_poster.py
```
