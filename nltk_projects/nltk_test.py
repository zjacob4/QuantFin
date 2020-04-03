import nltk
from nltk.corpus import treebank
from nltk.tag import pos_tag_sents
from urllib import request
from bs4 import BeautifulSoup

url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
ebook_tokens = nltk.word_tokenize(raw)

url2 = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = request.urlopen(url2).read().decode('utf8')
raw2 = BeautifulSoup(html, 'html.parser').get_text()
bbc_tokens = nltk.word_tokenize(raw2)
print('html')
print(bbc_tokens[:60])

sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)

print('tokens')
print(tokens)

tagged = nltk.pos_tag(tokens)
print('tagged')
print(tagged)

entities = nltk.chunk.ne_chunk(tagged)
print('entities')
print(entities)

#t = treebank.parsed_sents('wsj_0001.mrg')[0]
#t.draw()

#nltk.plot_word_freq_dist(tokens)
