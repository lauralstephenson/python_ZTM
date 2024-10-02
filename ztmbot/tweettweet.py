#This is a FAKE Twitter/X API
#Twitter/X now CHARGES for API use
#So I'm using pseudocode or commenting it out

#Tweepy is a library that works with Twitter/X
#import tweepy 
#need library for rate limiter
#import time

#what Twitter/X uses to access account
#go to Twitter/X and get consumer API keys and tokens
#never share with anybody
#copy and paste into the file OR keep as a text file
#click on regenerate on Twitter/X's site

#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)

#api = tweepy.API(auth)
#this gets MY information
#user = api.me()

#this prints out your public tweets
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#      print(tweet.text)

#print(api.me())
#print your username
#print(user.name)
#print your Twitter handle
#print(user.screen_name)
#count the number of followers
#print(user.followers_count)

#something useful: follow your followers
#there may be thousands of them
#def limit_handler(cursor)
#      try:
#            while True:
#                  yield cursor.next()
#      except tweepyRateLimitError:
#            #sleeps for 1000 milliseconds
#            time.sleep(1000)

#now you want a narcissistic bot that wants to follow your own tweets
#if they have certain keywords in them
#make sure your limit handler is working first
#search_string = "python"
#numbersOfTweets = 2

#for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
#     try:
#           tweet.favorite()
#you can also retweet them 
#           tweet.retweet()
#           print("I liked that tweet!")
#     except tweepy.TweepError as e:
#           print(e.reason)
#     except StopIteration:
#           break

#now search for tweets with your name and like them, ya narcissist
#search_string = "Your Name"
#numbersOfTweets = 5

#generous bot
#tweepy.Cursor is how to iterate over any items
#in the timeline with a limit handler
#for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     print(follower.name)
#Once this runs, grab a random name and check it
#or use this for specific followers
      #if follower.name == "randomname"
            #follower.follow()
            #break