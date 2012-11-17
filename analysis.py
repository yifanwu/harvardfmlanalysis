from gensim import corpora, models, similarities

v = True

#macro

data_add = '/Users/yifanwu/Dropbox/Dev/harvardfmlanalysis/data/fml_cleaned_text.txt'
stoplist = set('for a of the and to in'.split())

def loadRun():

  # collect statistics about all tokens
  dictionary = corpora.Dictionary(line.lower().split() for line in open(data_add))

  # remove stop words and words that appear only once
  stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
              if stopword in dictionary.token2id]
  once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
  dictionary.filter_tokens(stop_ids + once_ids) # remove stop words and words that appear only once
  dictionary.compactify() # remove gaps in id sequence after words that were removed
  print dictionary
Dictionary(12 unique tokens

  # doesn't load the corpus into memory!
  corpus_memory_friendly = MyCorpus() 
  if v:
    print corpus_memory_friendly
    
  # load one vector into memory at a time
  for vector in corpus_memory_friendly: 
    if v:
      print vector

  #todo:
  documents = ["Human machine interface for lab abc computer applications",
  "A survey of user opinion of computer system response time"]

  
  texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]

  all_tokens = sum(texts, [])
  tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
  texts = [[word for word in text if word not in tokens_once] for text in texts]

  if v:
    print texts

  dictionary = corpora.Dictionary(texts)
  dictionary.save('/Users/yifanwu/Dev/harvardfmlanalysis/data/LDA.dict')

  if v:
    print dictionary

def main():
  loadRun()


main()