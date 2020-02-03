import nltk
import io
import numpy as np
import random
import string
import warnings
warnings.filterwarnings('ignore')

##################################
#Reading the file.
f = open('Deep_Learning.txt', 'r', errors='ignore')
raw = f.read()
raw = raw.lower()                                             #coverts into lower case letters
nltk.download('punkt')
nltk.download('wordnet')
###################################
#Pre Processing of the data
sent_tokens = nltk.sent_tokenize(raw)                         #coverts List into sentences
word_tokens = nltk.word_tokenize(raw)                         #converts list of words.

#lemmatization
lemmer = nltk.stem.WordNetLemmatizer()
def lemTokens(tokens):
    return[lemmer.lemmatize(token)for token in tokens]
remove_punct_dict = dict((ord(punct), None)for punct in string.punctuation)
def lemNormalize(text):
    return lemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

#Greetings

GREETING_INPUTS = ("HI","hello","how are you","whats up", "hey")
GREETING_RESPONSES = ["HI", "HELLO", "Good Thanks", "How are You?", "hey"]
def greetings(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


############
#Vectorizer
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def response(user_response):
    chatbot_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer = lemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1],tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        chatbot_response = chatbot_response+"I am sorry, I didn't understand "
        return chatbot_response
    else:
        chatbot_response = chatbot_response+sent_tokens[idx]
        return chatbot_response



flag = True
print("Goku : My name is Goku")
while(flag == True):
    user_response = input()
    user_response = user_response.lower()
    if(user_response != 'bye'):
        if(user_response=='thanks' or user_response=='thank you'):
            flag = False
            print("Goku: you are welcome")
        else:
            if( greetings(user_response)!= None):
                print("Goku: "+ greetings(user_response))
            else:
                print("Goku: ", end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("Goku: Bye Take Care")



