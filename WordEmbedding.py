""""Pip installs """
#pip install gensim
from distutils.command import clean
""""Imports"""
import scipy as sp
import spacy
import re
from gensim.models import Word2Vec
import nltk
from nltk.corpus import stopwords
""""load modules"""
stopwords= stopwords.words('english')
spacy_model = spacy.load("en_core_web_md")


example_lower = example.lower()
filtered_words=[]

for word in example_lower:
    example_split = example_lower.split()
    filtered_list = [i for i in example_split if i not in stopwords]
    filtered_words.append(filtered_list)
    
print(filtered_list)

example='This is an Example, to show us how many words get filtered out'
sentence = "The war in ukraine is making me suicidal"

good = spacy_model("good")
bad = spacy_model("bad")

f = open("english-adjectives.txt","r")
clean_list = []

long_list_adjectives = [x for x in f]
for i in long_list_adjectives:
    i = i.replace("\n", "")
    clean_list.append(i)
print(clean_list)

string1=""
for i in clean_list:
   string1=string1+i+" "
print(string1)
#print(string2)

#print(str(clean_list))
doc = spacy_model(string1)

for token1 in doc:
    #for token2 in doc:
    print("good words", token1.text,token1.similarity(good))
    print("bad words", token1.text,token1.similarity(bad))
    print ("  ")
    
        #print(token1.text,token2,token1.similarity(token2))
        #gensim_models.most_similar(positive=("author"))



# print(stopwords_nltk)

