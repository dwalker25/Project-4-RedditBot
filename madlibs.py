'''
This lab has three tasks.

TASK 1:
Implement the `generate_comment` function below.

TASK 2:
Redefine the `madlibs` and `replacements` variables so that the generated comments are what you want your reddit bot to say.
You must have at least 6 different madlibs.
Each madlib should be 2-5 sentences long and have at least 5 [REPLACEMENT] [WORDS].

TASK 3:
Use your `generate_comment` function to post at least 100 messages to the `Practice posting messages here :)` submission, located at:
<https://old.reddit.com/r/cs40_2022fall/comments/yv4s9o/practice_posting_messages_here/>
You should have at least 10 top level comments and at least 10 replies to comments (but it's okay if they're all replies to the same comment).

IN order to make a reply .reply(); you'll have to figure out the details.

SUBMISSION:
Upload your bot's name and your `madlib.py` file to sakai.
'''
import random
import praw
reddit = praw.Reddit('trek_star_bot')
import time
import datetime

url = "https://old.reddit.com/r/cs40_2022fall/comments/yv4s9o/practice_posting_messages_here/"
submission = reddit.submission(url=url)

madlibs = [
    'I [KNOW] the [HUMAN BEING] and [FISH] can coexist peacefully. This is my [GREATEST] [DREAM].', 
    'I [CALL UPON] all nations, to do everything they can, to [STOP] these [TERRORIST KILLERS]. Thank you… now watch [THIS DRIVE].',
    'I [THINK] we [AGREE], the past is [OVER]. [THANK GOODNESS] because I\'m [TIRED OF] the past.',
    '[THEY] misunderestimated me. And I [KNOW] [THEY] will not be so [STUPID] [NEXT TIME].',
    'You work [THREE] jobs? ... [UNIQUELY] American, isn\'t it? I mean, that is [FANTASTIC] that you\'re doing that. It\'s the [GREATEST] [THING] I\'ve ever heard.',
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
    'THING' : ['thing', 'story'],
    'YESTERDAY' : ['Yesterday', 'Last week', 'A few days ago'],
    'MADE NOTE' : ['made note', 'observed'],
    'TALENT' : ['talent', 'poise', 'skill'],
    'DANCING' : ['dancing', 'singing', 'coding'],
    'JOY' : ['joy', 'happiness', 'contentment'],
    }

def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.

    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.

    For example, if we randomly selected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    Instead, you should ensure that the madlibs that you create will all be grammatically correct when this substitution procedure is followed.
    '''
    madlib = random.choice(madlibs)
    for replacement in replacements.keys():
        madlib = madlib.replace('[' +replacement+']', random.choice(replacements[replacement]))
    return madlib

# essentially infinite loop to create comments
for i in range(2):
    print(datetime.datetime.now(), ': made a comment, i=',i)
    try:
        comment = generate_comment()
        print(comment)
        submission.reply(comment)
    except praw.exceptions.APIException:
        print('sleeping for 5 seconds')
        time.sleep(5)

for comment in submission.comments.list():
    try:
        comment.reply('reply')
        print(comment)
        print('reply success')
    except praw.exceptions.APIException:
        print('sleeping for 5 seconds')
        time.sleep(5)

