import praw
import numpy as np
from numpy import random

reddit = praw.Reddit(client_id='DEVELOPER ID',
                     client_secret='DEVELOPER SECRET KEY',
                     username='BOT USERNAME HERE',
                     password='BOT PASSWORD HERE',
                     user_agent='OPTIONAL')
subreddit = reddit.subreddit('SUBREDDITS HERE')
dysl = '!hgu'
hug = '!hug'
joke = '!dadjoke'
encourage = '!encourage'

for comment in subreddit.stream.comments():
    if encourage in comment.body:
        saying = random.choice(["“It is impossible to live without failing at something, unless you live so "
                                "cautiously that you might as well not have lived at all, in which case you have "
                                "failed by default.” - J.K. Rowling",
                                "Tough time never last, tough people only last. reelepppe - Bo Demi Demi",
                                "“In the middle of every difficulty lies opportunity.” — Albert Einstein",


                                ])
    if joke in comment.body:
        joke = random.choice([
                            "My wife is really mad at the fact that I have no sense of direction. So I packed up my "
                            "stuff and right!",
                            "How do you get a squirrel to like you? Act like a nut.",
                            "Why don't eggs tell jokes? They'd crack each other up.",
                            "I don't trust stairs. They're always up to something.",
                            "Did you hear the rumor about butter? Well, I'm not going to spread it!",
                            "Why couldn't the bicycle stand up by itself? It was two tired.",
                            "Why can't a nose be 12 inches long? Because then it would be a foot.",
                            "This graveyard looks overcrowded. People must be dying to get in",
                            "What time did the man go to the dentist? Tooth hurt-y.",
                            "How many tickles does it take to make an octopus laugh? Ten tickles.",
                            "What concert costs just 45 cents? 50 Cent featuring Nickelback!",
                            "How do you make a tissue dance? You put a little boogie in it.",
                            "Why did the math book look so sad? Because of all of its problems!"
                              ])
        comment.reply(joke)
    if hug in comment.body:
        hugGifs = random.choice(["https://tenor.com/view/milk-and-mocha-hug-cute-kawaii-love-gif-12535134",
                                 "https://tenor.com/view/hug-love-sweet-cute-heart-gif-17444176",
                                 "https://tenor.com/view/big-hero6-baymax-feel-better-hug-hugging-gif-4782499",
                                 "https://tenor.com/view/peach-cat-hug-hug-up-love-mochi-mochi-peach-cat-gif-16334628",
                                 "https://tenor.com/view/cat-hug-back-hug-notice-me-attention-to-me-gif-14227401",
                                 "https://tenor.com/view/hug-peachcat-cat-cute-gif-13985247"
                                 ])

        author = comment.author
        print('Found, posted by '+ author.name)
        try:
            comment.reply("""Virtual Hug sent
            
""" + hugGifs + """

    I'm a bot, and this action was completed automatically. People need love sometimes so if you need a virtual hug just ask and I'll be there. I have a post limit right now because I don't have enough karma. If you could upvote me that would help spread the love <3""")

        except:
            print('Too frequent')

    if dysl in comment.body:
        print('Found')
        try:
            comment.reply("""Virtual Hug sent

    I'm a bot, and this action was completed automatically. People need love sometimes so if you need a virtual hug just ask and I'll be there. I have a post limit right now because I don't have enough karma. If you could upvote me that would help spread the love <3""")
        except:
            print('Too Frequent')

