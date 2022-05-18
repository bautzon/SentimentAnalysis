from nltk.corpus import twitter_samples

all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')


def rate(all_positive_tweets,d): 
    tweetscore=[]
    afinndict=d
    for i in all_positive_tweets[0:100]:
        print(i)
        for word in i:
            try:
               tweetscore.append(afinndict[word])
            except KeyError as e:
               pass
        try:
            result=sum(tweetscore)/len(tweetscore)   
            print(f"""score of {i} 

                        {result}""")    
        except ZeroDivisionError:
            pass  

def create_dict():
    d = {}    
    print("!")
    with open ("AFINN-111.txt") as f:
        for i in f:
            a=i.split()
            value=int(a[-1])
            key=i[0:-2]
            #print(type(key))
            key=key.replace("-","")
            d[key[0:-1]]=value
        
    return d


d=create_dict()        
rate(all_positive_tweets,d)