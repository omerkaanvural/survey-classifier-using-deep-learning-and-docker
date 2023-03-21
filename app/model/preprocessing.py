import string
import nltk
import re


def lower(text):
    return text.lower()


def remove_punctuations(text):
    return text.translate(str.maketrans('', '', string.punctuation))


def remove_stopwords(text):
    stop_words = set(nltk.corpus.stopwords.words('turkish'))
    filtered = " ".join([word for word in text.split() if word not in stop_words])
    return filtered


def remove_emojis(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)


def pipe(text):
    text = lower(text)
    text = remove_punctuations(text)
    text = remove_stopwords(text)
    text = remove_emojis(text)
    return text