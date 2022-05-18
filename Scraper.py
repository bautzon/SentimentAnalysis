from urllib.error import HTTPError
import tweepy
import requests
import json
import urllib.request
from Cleaner import *

data= {"title":[],
              "body":[],
              "upvotes":[]   
      }

datalist=set()
def scrape_twitter(hashtag):
    search=hashtag
    bearer="AAAAAAAAAAAAAAAAAAAAAOD9ZwEAAAAAp5wAOHyavG6WIsJL7dmJEmclxO8%3DBw19697vkBcRxoEI5gRfiVCMiAoVSvXxYtWI48qI5lLvlqO8Zw"
    secret="t1HgnfQceyiviACoLBVeZ5mhVzwoVSGJrmHDvzznMOUdQu3uRX"
    api="SZPsGj9Ixdrfy1nhv6TzuzMbE"
    client=tweepy.Client(bearer_token=bearer)
    response=client.search_recent_tweets(query=hashtag,max_results=10,tweet_fields=['lang','text','public_metrics'],expansions=['author_id'])
    if response.data:
        for tweets in response.data:
            if tweets is not None and tweets.lang=="en":
                datalist.add(tweets.text)
                
    else: 
        print(f"unable to find anything for #{hashtag}")  
    #print(datalist)    
    return datalist, search


def scrape_subrreddit(subreddit):
  try:
    source2 = urllib.request.urlopen(subreddit).read()
    jsonResponse = json.loads(source2.decode('utf-8'))
    print(f"Adding content from /r/{subreddit} to dict")
    for i in jsonResponse['data']['children']:
        upvotes=i['data']['ups']
        title=i['data']['title']
        body=i['data']['selftext']
        if upvotes>50:
            data['title'].append(title)
            data['body'].append(body) 
            data['upvotes'].append(upvotes)    
  except HTTPError as e:
      print(f"Fejl: {e}")
  

def determine_link():
    url=input("Skriv et link til et subreddit eller til et twitter hashtag ")
    if "reddit" in url:
         scrape_subrreddit(url+".json?limit=10")
    elif "twitter" in url:
        hashtag=url.split("/")[-1][:-1]     #Extracting hashtag
        scrape_twitter(hashtag)

def save_to_txt():
    print ("saving data to textfile")
    f = open("demofile.txt", "w",encoding="utf-8")
    for i in datalist:
        f.write(i)



