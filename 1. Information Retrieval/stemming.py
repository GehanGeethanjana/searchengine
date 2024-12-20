import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["Jump", "Jumped", "Jumping"]

stemmed_words = [stemmer.stem(word) for word in words]

for i in range(len(words)):
    print(words[i], "->", stemmed_words[i])