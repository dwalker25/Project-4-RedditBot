import praw
import random
import datetime
import time
import argparse

madlibs = [
    'I [KNOW] the [HUMAN BEING] and [FISH] can coexist peacefully. This is my [GREATEST] [DREAM].', 
    'I [CALL UPON] all nations, to do everything they can, to [STOP] these [TERRORIST KILLERS]. Thank you… now watch [THIS DRIVE].',
    'I [THINK] we [AGREE], the past is [OVER]. [THANK GOODNESS] because I\'m [TIRED OF] the past.',
    '[THEY] misunderestimated me. And I [KNOW] [THEY] will not be so [STUPID] [NEXT TIME].',
    'You work [THREE] jobs? ... [UNIQUELY] American, isn\'t it? I mean, that is [FANTASTIC] that you\'re doing that. It\'s the [BEST] [THING] I\'ve ever heard.',
    '[YESTERDAY], you [MADE NOTE] of my—the lack of my [TALENT] when it came to [DANCING]. But nevertheless, I want you to know I did it with [JOY]. And no question Liberia has gone through very difficult times.',
    ]

replacements = {
    'KNOW' : ['know', 'am confident', 'believe', 'am certain', 'promise'],
    'HUMAN BEING' : ['human being', 'tree', 'goldfish', 'anteater'],
    'FISH' : ['fish', 'walrus', 'zebra', 'monkey'],
    'GREATEST' : ['greatest', 'most frequent', 'most exciting'],
    'DREAM' : ['dream', 'ideal', 'goal'],
    'CALL UPON' : ['call upon', 'ask', 'beseech', 'implore'],
    'EVERYTHING': ['everything', 'whatever', ],
    'STOP': ['stop', 'defend against', 'oppose', 'fight'],
    'TERRORIST KILLERS' : ['terrorist killers', 'bad guys', 'enemies', 'dangerous people'],
    'THIS DRIVE' : ['this drive', 'me shoot some hoops', 'me be a little silly and goofy', 'scarf down some peanuts and crackerjacks'],
    'THINK' : ['think', 'believe', 'know'],
    'AGREE' : ['agree', 'concur'],
    'OVER' : ['over', 'long gone', 'behind us'],
    'THANK GOODNESS' : ['thank goodness', 'Hallelujuah'],
    'TIRED OF' : ['tired of', 'done with', 'fed up with'],
    'THEY' : ['They', 'Everyone'],
    'KNOW' : ['know', 'believe', 'am confident', 'promise'],
    'STUPID' : ['stupid', 'dumb', 'foolish'],
    'NEXT TIME' : ['next time', 'in the future', 'going forward'],
    'THREE' : ['three', 'forty', 'one hundred', 'one thousand'],
    'UNIQUELY' : ['uniquely', 'especially', 'super'],
    'FANTASTIC' : ['incredible', 'awesome', 'cool'],
    'BEST' : ['best', 'coolest', 'most impressive'],
    'THING' : ['thing', 'story'],
    'YESTERDAY' : ['Yesterday', 'Last week', 'A few days ago'],
    'MADE NOTE' : ['made note', 'observed'],
    'TALENT' : ['talent', 'poise', 'skill'],
    'DANCING' : ['dancing', 'singing', 'coding'],
    'JOY' : ['joy', 'happiness', 'contentment'],
    }

# FIXME:
# copy your generate_comment function from the madlibs assignment here
def generate_comment():
    madlib = random.choice(madlibs)
    for replacement in replacements.keys():
        madlib = madlib.replace('[' +replacement+']', random.choice(replacements[replacement]))
    return madlib

# FIXME:
# connect to reddit 
parser = argparse.ArgumentParser(description='gets the bot username')
# this allows the user to run five bots simultaneously by adding (0, 2, 4, 5, 6) to the default botname
parser.add_argument('--name', default='')
args = parser.parse_args()
reddit = praw.Reddit('trek_star_bot' + args.name)
name = 'trek_star_bot' + args.name

# FIXME:
# select a "home" submission in the /r/cs40_2022fall subreddit to post to,
# and put the url below
#
# HINT:
# The default submissions are going to fill up VERY quickly with comments from other students' bots.
# This can cause your code to slow down considerably.
# When you're first writing your code, it probably makes sense to make a submission
# that only you and 1-2 other students are working with.
# That way, you can more easily control the number of comments in the submission.
submission_url = 'https://old.reddit.com/r/cs40_2022fall/comments/yyqwqx/test8/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:
    try:
        # printing the current time will help make the output messages more informative
        # since things on reddit vary with time
        print()
        print('new iteration at:',datetime.datetime.now())
        print('submission.title=',submission.title)
        print('submission.url=',submission.url)

        # FIXME (task 0): get a list of all of the comments in the submission
        # HINT: this requires using the .list() and the .replace_more() functions
        all_comments = []
        submission.comments.replace_more(limit=None, threshold=0)
        all_comments = submission.comments.list()
        # HINT: 
        # we need to make sure that our code is working correctly,
        # and you should not move on from one task to the next until you are 100% sure that 
        # the previous task is working;
        # in general, the way to check if a task is working is to print out information 
        # about the results of that task, 
        # and manually inspect that information to ensure it is correct; 
        # in this specific case, you should check the length of the all_comments variable,
        # and manually ensure that the printed length is the same as the length displayed on reddit;
        # if it's not, then there are some comments that you are not correctly identifying,
        # and you need to figure out which comments those are and how to include them.
        print('len(all_comments)=',len(all_comments))

        # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
        # HINT: 
        # use a for loop to loop over each comment in all_comments,
        # and an if statement to check whether the comment is authored by you or not
        not_my_comments = []
        for comment in all_comments:
            if comment.author != name:
                not_my_comments.append(comment)

        # HINT:
        # checking if this code is working is a bit more complicated than in the previous tasks;
        # reddit does not directly provide the number of comments in a submission
        # that were not gerenated by your bot,
        # but you can still check this number manually by subtracting the number
        # of comments you know you've posted from the number above;
        # you can use comments that you post manually while logged into your bot to know 
        # how many comments there should be. 
        print('len(not_my_comments)=',len(not_my_comments))

        # if the length of your all_comments and not_my_comments lists are the same,
        # then that means you have not posted any comments in the current submission;
        # (your bot may have posted comments in other submissions);
        # your bot will behave differently depending on whether it's posted a comment or not
        has_not_commented = len(not_my_comments) == len(all_comments)

        if has_not_commented:
            # FIXME (task 2)
            # if you have not made any comment in the thread, then post a top level comment
            #
            # HINT:
            # use the generate_comment() function to create the text,
            # and the .reply() function to post it to reddit;
            # a top level comment is created when you reply to a post instead of a message
            print(datetime.datetime.now(), ': made a top level comment')
            comment = generate_comment()
            print(comment)
            submission.reply(comment)
        else:
            # FIXME (task 3): filter the not_my_comments list to also remove comments that 
            # you've already replied to
            # HINT:
            # there are many ways to accomplish this, but my solution uses two nested for loops
            # the outer for loop loops over not_my_comments,
            # and the inner for loop loops over all the replies of the current comment from the outer loop,
            # and then an if statement checks whether the comment is authored by you or not
            comments_without_replies = []
            for comment in not_my_comments:
                    reply_author = []
                    for reply in comment.replies:
                        reply_author.append(str(reply.author))
                    if name in reply_author:
                        pass
                    else:
                        comments_without_replies.append(comment)

            # HINT:
            # this is the most difficult of the tasks,
            # and so you will have to be careful to check that this code is in fact working correctly;
            # many students struggle with getting a large number of "valid comments"
            print('len(comments_without_replies)=',len(comments_without_replies))

            # FIXME (task 4): randomly select a comment from the comments_without_replies list,
            # and reply to that comment
            #
            # HINT:
            # use the generate_comment() function to create the text,
            # and the .reply() function to post it to reddit;
            # these will not be top-level comments;
            # so they will not be replies to a post but replies to a message
            try:
                upvote_high = 0
                highest_comment = random.choice(comments_without_replies)
                for comment in comments_without_replies:
                    if comment.score >= upvote_high:
                        upvote_high = comment.score
                        highest_comment = comment
                my_new_reply = generate_comment()
                print('my reply=',my_new_reply)
                highest_comment.reply(my_new_reply)
            except:
                print("No reply possible.")
                pass

        # FIXME (task 5): select a new submission for the next iteration;
        # your newly selected submission should be randomly selected from the 5 hottest submissions
        submission_list = list(reddit.subreddit('cs40_2022fall').hot(limit=5))
        submission = random.choice(submission_list)

        # We sleep just for 1 second at the end of the while loop.
        # This doesn't avoid rate limiting
        # (since we're not sleeping for a long period of time),
        # but it does make the program's output more readable.

        time.sleep(1)
    except Exception as e:
        pass