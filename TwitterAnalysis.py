from cgitb import text
from decimal import DivisionByZero
from posixpath import split
import spacy
from nltk import Tree
from spacy.symbols import *
from Scraper import *

class Analyzer:
  datalist=[]
  search=""
  nlp = spacy.load("en_core_web_sm")
  listofsum=[]

  def __init__(self,datalist,search):
      self.datalist=datalist
      self.search=search
      nlp = spacy.load("en_core_web_sm")
      print(datalist,"DATALIST")
      pass

  def total_score(self):
      print("totalscore",sum(self.listofsum)/len(self.listofsum))

    #takes list of words and scores it against afinnlist 8)
  def rate(self,tweetwordlist,d):
    tweetscore=[]
    afinndict=d
    result=0
    for word in tweetwordlist:
        if " " in word:
          word=word.replace(" ","")
        try:
          tweetscore.append(afinndict[word])
        except KeyError as e:
            pass
    if tweetscore==None:
        print("Unable to rate",tweetwordlist)    
    try:
        result=sum(tweetscore)/len(tweetscore) 
        self.listofsum.append(result)   
    except ZeroDivisionError:
        pass
    print(self.listofsum)
    return result



  def punktum_test(self,tweet,search,d): 
    if "." in tweet:
        rating=0
        splitlist=[]
        tweet=tweet.split(".")
        for i in tweet:
            if search in i:
                    split=i.split()
                    splitlist.append(split)
                    rating=rating+self.rate(split,d)
        if rating:
            print(f"""SPLIT SCORE OF {splitlist} in sentence {tweet} = 

                                    {rating}""")                   
    else:
        tweetlist=tweet.split()
        rating=self.rate(tweetlist,d)
        if rating:
            print(f"""ENTIRE SENTENCE of {tweet} = 
                    
                                        {rating}""")
                            



    #FIRST APPROACH
  def flatten_tree(self,token,tree,search,tweet,d):
        tree=([token.text_with_ws for token in list(tree)])
        if len(tree)>2:
            rating=self.rate(tree,d)
            if rating:
                print(f"""TREE RATING of  {tree} 

                                        {rating}""")                        
            return tree
        else:
            self.punktum_test(tweet,search,d)


  def iterate(self):
        d=self.create_dict()
        for tweet in datalist:
            wordlistfortweet=[]
            doc=self.nlp(tweet)
            for token in doc: 
                if token.text==self.search:
                    wordlistfortweet.append(self.flatten_tree(token,token.subtree,self.search,tweet,d))       

                
            # print(f'LIST FOR tweet {wordlistfortweet}') 

            

  def create_dict(self):
        d = {}    
        with open ("AFINN-111.txt") as f:
            for i in f:
                a=i.split()
                value=int(a[-1])
                key=i[0:-2]
                #print(type(key))
                key=key.replace("-","")
                d[key[0:-1]]=value
        return d     

        
  def to_nltk_tree(self,node,source=None):

    if node.n_lefts + node.n_rights > 0:
        parsed_child_nodes = [self.to_nltk_tree(child) for child in node.children]
        return Tree(node.orth_, parsed_child_nodes)
    else:
        return node.orth_



"""
    def search_orgs(text):
        doc=nlp(text)
        ent_list=[]
        for entity in doc.ents:
            if entity.label_=="ORG" or "PERSON" or "MONEY":
                ent_list.append(entity.text)
        return ent_list        

    def check_org_for_POS_head(text,POS):
        ent_list=search_orgs(text)
        #print(ent_list)
        adjectives=set()
        doc=nlp(text)
        for token in doc:
            #token.text in ent_list and 
            if token.head.pos == POS and token.text in ent_list: 
                adjectives.add(token.head)
                print(f' ADJ  connected to {token.text} are {adjectives}')
                #Give points if true.
    data=data["title"]

    for tweet in data:
        check_org_for_POS_head(tweet,VERB)
        check_org_for_POS_head(tweet, ADJ)
    print (data)
"""

"""
    visited=[]
    def dfs(node):
        visited.append(node.text)
        if not node.children:
            return []
        for child in node.children:
            dfs(node)
        print(visited)    
"""        
