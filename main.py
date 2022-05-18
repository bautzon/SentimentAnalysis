from os import remove
import spacy
from nltk import Tree
from Scraper import *
from Cleaner import *
from Stemmer import *
from Counter import *
from TwitterAnalysis import Analyzer


def choose_method():
    print("""
    Welcome - Choose an option
    1) Scrape from link
    2) Scrape from subreddit
    3) Scrape from twitter hashtag
    4) print clean
    5) Quit
    6) Save to file
    7) print tree
    8) analyse
    9) totalscore
    """)
    cleanlist=[]
    quit=False
    while quit == False:
        userinput=input("Write choice ")
        if userinput=="1":
            determine_link()
        elif userinput=="2":
            subredditinput=input("Write a subreddit name ")
            scrape_subrreddit("https://www.reddit.com/r/"+subredditinput+".json?limit=10")
        elif userinput=="3":
            twitterinput=input("Write a topic to search twitter ").lower()
            dirtylist=scrape_twitter(twitterinput)[0]
            print(dirtylist)
            if dirtylist:
                print(f"-Added tweets for {twitterinput}-")
            search=scrape_twitter(twitterinput)[1]
            cleanlist=remove_regex(dirtylist)
            
            print("""
            
            """)
        elif userinput=="4":
            print_cleaned_data(cleanlist)
        elif userinput=="5":
            quit=True
        elif userinput=="6":
            save_to_txt()
        elif userinput=="7":
            make_tree()
        elif userinput=="8":
            analyzer=Analyzer(cleanlist,search)
            analyzer.iterate()
        elif userinput=="9":
            analyzer.total_score()  
        else:
            print("Unable to understand")


choose_method()   #scraper

