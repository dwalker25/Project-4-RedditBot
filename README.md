# Project-4-RedditBot

## Political Stance 
**The reddit bot 'trek_star_bot' has strongly supports George W. Bush and promotes his famous 'Bush-isms'.**

The *trek_star_bot* comments one of six famous 'Bush-isms', which has been slightly altered via the word replacement method of Madlibs. Example:
"You work one thousand jobs? ... especially American, isn't it? I mean, that is awesome that you're doing that. It's the best thing I've ever heard."

## Creating New Submission Posts
The *trek_star_bot* scans the hot submissions in /r/conservative, checking if the submission is just a link or a full submission with a body section, and posting them accordingly to the 'cs40_2022fall' subreddit.

```
submission_list = list(reddit.subreddit('conservative').hot(limit=None))
    submission = random.choice(submission_list)
    sub_title = submission.title
    sub_selftext = submission.selftext

    if sub_selftext == '':
        sub_url=submission.url
        subreddit.submit(sub_title, url=sub_url)
    else:
        subreddit.submit(sub_title, selftext=sub_selftext)
```

## Upvoting and Downvoting for a Political Agenda
The *trek_star_bot* uses the `TextBlob` library to determine the polarity of any submission or comment that includes 'Trump'. The bot downvotes any submission or comment that includes 'Trump' and significantly favors Trump, shown in the code below:

```
if 'trump' in sub.title.lower():
        sub_textblob = TextBlob(sub.title)
        sub_value = sub_textblob.sentiment.polarity
        if sub_value > 0.2:
            sub.downvote()
            print('Downvote successful: ', sub.title)
        else:
            sub.upvote()
            print('Upvote sucessful: ', sub.title)
```

## Grading
Completed `bot.py` - 12 points

Completed github repo - 3 points

Get 800+ valid comments - 6 points

*Extra Credit*
Creating new submission posts in `bot_submissions.py` - 2 points

Upvoting and Downvoting for a political agenda using TextBlob - 4 points

**Total points = 27/30**

    Provides a link to your favorite thread involving your bot, an image screenshot of the thread, and a short description of what you like about it. (Below each comment is a button labeled permalink that lets you link to a comment.)
   
