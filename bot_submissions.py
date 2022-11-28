import praw
import random

reddit = praw.Reddit('trek_star_bot')
subreddit = reddit.subreddit('cs40_2022fall')
for i in range(300):
    submission_list = list(reddit.subreddit('conservative').hot(limit=None))
    submission = random.choice(submission_list)
    sub_title = submission.title
    sub_selftext = submission.selftext

    if sub_selftext == '':
        sub_url=submission.url
        subreddit.submit(sub_title, url=sub_url)
    else:
        subreddit.submit(sub_title, selftext=sub_selftext)
    print('new submission complete')
    print(i)
