import praw
import argparse
import time
import datetime
from textblob import TextBlob

parser = argparse.ArgumentParser(description='Gets number and name of bot from the command line')
parser.add_argument('--name', default='')
args = parser.parse_args()
reddit = praw.Reddit('trek_star_bot' + args.name)
name = 'trek_star_bot' + args.name

for sub in list(reddit.subreddit('cs40_2022fall').hot(limit=100)):
    if 'trump' in sub.title.lower():
        sub_textblob = TextBlob(sub.title)
        sub_value = sub_textblob.sentiment.polarity
        if sub_value > 0.2:
            sub.downvote()
            print('Downvote successful: ', sub.title)
        else:
            sub.upvote()
            print('Upvote sucessful: ', sub.title)
    sub.comments.replace_more(limit=None, threshold=0)
    for comment in sub.comments.list():
        if 'trump' in comment.body.lower():
            comment_textblob = TextBlob(comment.body)
            comment_value = comment_textblob.sentiment.polarity
            if comment_value > 0.2:
                comment.downvote()
                print('Downvote successful: ', comment.body)
            else:
                comment.upvote()
                print('Upvote sucessful: ', comment.body)

