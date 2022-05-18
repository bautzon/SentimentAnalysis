import spacy
spacy_model = spacy.load("en_core_web_md")
GoodWords = ["Good","Amazing","Happy"]
sentence="Kristersson argued it wasn’t a time for party politics, but couldn’t contain his excitement that a policy his party has been pushing for for two decades is finally coming into fruition."
doc = spacy_model(sentence)
for token1 in doc:
    for token2 in doc:
      print(token1.text,token2,token1.similarity(token2))