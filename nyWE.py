import doctest
from nltk.corpus import twitter_samples
#pip install gensim
import spacy
import nltk
from nltk.corpus import stopwords
import re
 
positive=twitter_samples.strings('positive_tweets.json')
negative=twitter_samples.strings('negative_tweets.json')
#print(positive)
spacy_model = spacy.load("en_core_web_md")
sentence = ["The war in ukraine is making me suicidal", "Tesla stock is rising, elon musk is dead", "Marc just ate 5 kilo potatoes", "Microsoft is worse than Blizzard", "Bill gates is my father and my daddy", "I love Apple and iPhone", "i adore iphones <3", "Asus best in test"]
 
good_adj = spacy_model("positive")
bad_adj = spacy_model("negative")
#f = open("C:\\Users\\Bruger\\Desktop\\pythonpro\\englishwords.txt","r")
 
def make_list(f):
    clean_list=[]
    long_list_adjectives = [x for x in f]
    for i in long_list_adjectives:
        i = i.replace("\n", "")
        clean_list.append(i)
    return clean_list    
 
def clean_list_to_string(l):
    string_clean=""    
    for i in l:
        string_clean=string_clean+i+" "
    #print(string_clean)
    return string_clean
#print(string2)
#"The war in ukraine is making me suicidal"
 
def word_embed(tweet_list):
    tweet_list=" ".join(tweet)
    doc = spacy_model(tweet_list)
    score=0
    for word in doc:
        if(word.similarity and word.vector_norm):
            sim_negative= word.similarity(bad_adj)
            sim_positive= word.similarity(good_adj)
            max_=max(sim_negative,sim_positive)
            if max_ == word.similarity(bad_adj):
                #print(score,"score")
                difference = max_-sim_positive
                score=score-difference
                print(f" {word.text} is bad - score difference:  {difference}")
 
            elif max_ == word.similarity(good_adj):
                #print(score,"score")
                difference = max_+sim_negative
                score=score+difference
                print (f" {word.text} is good - score diffrence:  {difference}")
            print("    ")
    print(score, "for", tweet)      
 
stopword= stopwords.words('english')
def stop_words(sample, stopwords):
    #stopword= stopwords.words('english')
    list_of_sw_filtered_tweets = []
    for tweet in sample:
        sample_lower = tweet.lower()
        sample_split = sample_lower.split()
        filter_list= [j for j in sample_split if j not in stopwords]
        list_of_sw_filtered_tweets.append(filter_list)
# print(stopwords_nltk)
    return list_of_sw_filtered_tweets
    #print(list_of_sw_filtered_tweets)
 
listoflist=stop_words(sentence,stopword)
print(listoflist)
for tweet in listoflist:
    
    word_embed(tweet) 



 
# example='This is an Example, to show us how many words get filtered out'
# example_lower = example.lower()
# filtered_words=[]
 
# for word in example_lower:
#     example_split = example_lower.split()
#     filtered_list = [i for i in example_split if i not in stopwords]
#     filtered_words.append(filtered_list)
    
# print(filtered_list)
 
"""
def word_embed(sample,n_clean,p_clean):
    doc_p = spacy_model(p_clean)
    doc_n = spacy_model(n_clean)
    for i in sample:
        doc_tweet=spacy_model(i)
        sim_bad= doc_tweet.similarity(doc_n)
        sim_good= doc_tweet.similarity(doc_p)
        max_=max(sim_bad,sim_good)
        if max_ == doc_tweet.similarity(doc_n):
                difference = max_-sim_good
                print(f" {doc_tweet.text} is bad - score difference:  {difference}")
        elif max_ == doc_tweet.similarity(doc_p):
                difference = max_-sim_bad
                print (f" {doc_tweet.text} is good - score diffrence:  {difference}")
        print("                      ")   
 
"""



import nltk
from nltk . corpus import stopwords
stopwords_nltk = stopwords.words(’english’)
print ( stopw ords_nltk )