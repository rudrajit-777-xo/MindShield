import re #used to remove punctuation,special characters and numbers
import nltk #lib for text preprocessing and tokenization and stopwords
from nltk.tokenize import word_tokenize #function to split sentence into words
from nltk.corpus import stopwords #list of common useless words

stopword = set(stopwords.words('english'))
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = word_tokenize(text)             #"i always fail" → ["i", "always", "fail"]
    tokens = [word for word in tokens if word not in stopword]     #Removes useless words
    clean_text = " ".join(tokens)            #Joins the words back into sentence(without stopwords)
    return clean_text