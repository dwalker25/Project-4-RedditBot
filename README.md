# Project-4-RedditBot

## Political Stance 
**The reddit bot 'trek_star_bot' has strongly supports George W. Bush and promotes his famous 'Bush-isms'.**

The *trek_star_bot* comments one of six famous 'Bush-isms', which has been slightly altered via the word replacement method of Madlibs. Example:
"You work one thousand jobs? ... especially American, isn't it? I mean, that is awesome that you're doing that. It's the best thing I've ever heard."

## My favorite thread
This thread makes me laugh because it's so random. While one of the three commments does discuss Biden, the topic of the submission, it focuses on Biden's dog -- and the other two submissions are wildly irrelevant and useless.
![image of my favorite thread](https://user-images.githubusercontent.com/112443814/204164248-b36ddb81-e179-45fc-85e9-2837cfe27e7b.png)
Link: https://www.reddit.com/r/cs40_2022fall/comments/z61s7m/biden_deserves_props_for_his_masterful_ukraine/ixzvamc/

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

## Replying to the Most Upvoted Comment
Instead of having *trek_star_bot* reply randomly to comments, I added the following code so the bot replies to the most upvoted comment in a thread it hasn't replied to:

```
upvote_high = 0
highest_comment = random.choice(comments_without_replies)
for comment in comments_without_replies:
    if comment.score >= upvote_high:
        upvote_high = comment.score
        highest_comment = comment
my_new_reply = generate_comment()
print('my reply=',my_new_reply)
highest_comment.reply(my_new_reply)
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

## Running bot_counter.py
Running the `bot_counter.py` file on *trek_star_bot* returns the following output:
```
len(comments)= 1000
len(top_level_comments)= 139
len(replies)= 861
len(valid_top_level_comments)= 64
len(not_self_replies)= 807
len(valid_replies)= 740
========================================  
valid_comments= 804  
========================================  
NOTE: the number valid_comments will be used to determine your grade
```

## Grading
Completed `bot.py` - 12 points

Completed github repo - 3 points

Get 800+ valid comments - 6 points

*Extra Credit*

Replying to the most upvoted comment - 2 points

Creating new submission posts in `bot_submissions.py` - 2 points

Upvoting and Downvoting for a political agenda using TextBlob - 4 points

**Total points = 29/30**

    Provides a link to your favorite thread involving your bot, an image screenshot of the thread, and a short description of what you like about it. (Below each comment is a button labeled permalink that lets you link to a comment.)
   
