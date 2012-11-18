# coding: utf-8
import logging, gensim, bz2
from gensim import corpora, models, similarities

v = True

#macro
loc = '/Users/yifanwu/Dropbox/Dev/harvardfmlanalysis/'
data_add = loc+'data/fml_cleaned_text.txt'
dict_add = loc+'data/LDA.dict'
corp_add = loc+'data/corpus.mm'
lsi_add = loc+'data/LSI_model.lsi'
topics_add = loc+'data/topics.txt'
stoplist = set('''a, about, above, harvard, fol, across, after, again, against, all, almost, alone, along, already, also, although, always, am, among, an, and, another, any, anybody, anyone, anything, anywhere, are, area, areas, aren't, around, as, ask, asked, asking, asks, at, away, b, back, backed, backing, backs, be, became, because, become, becomes, been, before, began, behind, being, beings, below, best, better, between, big, both, but, by, c, came, can, cannot, can't, case, cases, certain, certainly, clear, clearly, come, could, couldn't, d, did, didn't, differ, different, differently, do, does, doesn't, doing, done, don't, down, downed, downing, downs, during, e, each, early, either, end, ended, ending, ends, enough, even, evenly, ever, every, everybody, everyone, everything, everywhere, f, face, faces, fact, facts, far, felt, few, find, finds, first, for, four, from, full, fully, further, furthered, furthering, furthers, g, gave, general, generally, get, gets, give, given, gives, go, going, good, goods, got, great, greater, greatest, group, grouped, grouping, groups, h, had, hadn't, has, hasn't, have, haven't, having, he, he'd, he'll, her, here, here's, hers, herself, he's, high, higher, highest, him, himself, his, how, however, how's, i, i'd, if, i'll, i'm, important, in, interest, interested, interesting, interests, into, is, isn't, it, its, it's, itself, i've, j, just, k, keep, keeps, kind, knew, know, known, knows, l, large, largely, last, later, latest, least, less, let, lets, let's, like, likely, long, longer, longest, m, made, make, making, man, many, may, me, member, members, men, might, more, most, mostly, mr, mrs, much, must, mustn't, my, myself, n, necessary, need, needed, needing, needs, never, new, newer, newest, next, no, nobody, non, noone, nor, not, nothing, now, nowhere, number, numbers, o, of, off, often, old, older, oldest, on, once, one, only, open, opened, opening, opens, or, order, ordered, ordering, orders, other, others, ought, our, ours, ourselves, out, over, own, p, part, parted, parting, parts, per, perhaps, place, places, point, pointed, pointing, points, possible, present, presented, presenting, presents, problem, problems, put, puts, q, quite, r, rather, really, right, room, rooms, s, said, same, saw, say, says, second, seconds, see, seem, seemed, seeming, seems, sees, several, shall, shan't, she, she'd, she'll, she's, should, shouldn't, show, showed, showing, shows, side, sides, since, small, smaller, smallest, so, some, somebody, someone, something, somewhere, state, states, still, such, sure, t, take, taken, than, that, that's, the, their, theirs, them, themselves, then, there, therefore, there's, these, they, they'd, they'll, they're, they've, thing, things, think, thinks, this, those, though, thought, thoughts, three, through, thus, to, today, together, too, took, toward, turn, turned, turning, turns, two, u, under, until, up, upon, us, use, used, uses, v, very, w, want, wanted, wanting, wants, was, wasn't, way, ways, we, we'd, well, we'll, wells, went, were, we're, weren't, we've, what, what's, when, when's, where, where's, whether, which, while, who, whole, whom, who's, whose, why, why's, will, with, within, without, won't, work, worked, working, works, would, wouldn't, x, y, year, years, yes, yet, you, you'd, you'll, young, younger, youngest, your, you're, yours, yourself, yourselves, you've, z, fml'''.split(", "))

def loadMatrix():
  documents = []
  for line in open(data_add):
    documents.append(line.replace("’","'").replace(".","").replace(",","").replace("girls","girl").replace("guys","guy"))
  #if v:
  #  print document

  texts = [[word for word in document.lower().split() if word not in stoplist]
           for document in documents]
  
  # remove words that appear only once
  all_tokens = sum(texts, [])
  tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
  texts = [[word for word in text if word not in tokens_once]
           for text in texts]
  
  if v:
    print texts

  dictionary = corpora.Dictionary(texts)
  dictionary.save(dict_add)
  corpus = [dictionary.doc2bow(text) for text in texts]
  corpora.MmCorpus.serialize(corp_add, corpus) 
  
def runLDA():
  logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

  # load id->word mapping (the dictionary), one of the results of step 2 above
  id2word = corpora.Dictionary.load(dict_add)
  # load corpus iterator
  mm = corpora.MmCorpus(corp_add)
  lda = models.ldamodel.LdaModel(corpus=mm, id2word=id2word, num_topics=5, update_every=0, passes=10)
  lda.print_topics(5)


loadMatrix() 
runLDA()