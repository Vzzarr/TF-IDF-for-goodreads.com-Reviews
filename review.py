import numpy
import requests
import xml.etree.ElementTree as ET
import re
import string
import nltk
from nltk.stem.porter import *
from collections import Counter

'''
given a Book Author and a Book Title, this function retrieves his reviews on goodreads.com
'''
def request_book_reviews(book_author, book_title):
    key = 'uDvUqwGib06lJRCbM59VUg'  #don't steal it, please!
    url_request = "https://www.goodreads.com/book/title.xml?author=" + book_author + "&key=" + key + "&title=" + book_title
    root = ET.fromstring(requests.get(url_request).content)
    reviews = ''
    for description in root.iter('description'):
        reviews = reviews + description.text
    return reviews

def tf_idf(book_author, book_title):
    text = request_book_reviews(book_author, book_title)
    no_punctuation = text.translate(string.punctuation)
    noSpecialCharacters = re.sub('[^a-zA-Z\']', ' ', no_punctuation)
    tokens = nltk.word_tokenize(noSpecialCharacters.lower())
    stemmer = PorterStemmer()
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    count = Counter(stemmed)
    print(count.most_common(100))

tf_idf("", "Harry Potter")


#xmltext = ET.tostring(tree, encoding='utf8', method='xml')
# xmltext = re.sub('[\n]', '', xmltext)
#print(xmltext)

"""
matches = re.findall(r"<description>.*</description>", xmltext)
for match in matches:
	print match
"""
