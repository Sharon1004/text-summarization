import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def clean_sentence(sentence):
    # Remove special characters and numbers
    sentence = re.sub(r'[^a-zA-Z\s]', '', sentence)
    # Convert to lowercase
    sentence = sentence.lower()
    return sentence

def preprocess_text(text):
    # Split into sentences
    original_sentences = sent_tokenize(text)

    # Clean each sentence
    cleaned_sentences = []
    for sentence in original_sentences:
        cleaned = clean_sentence(sentence)
        cleaned_sentences.append(cleaned)

    return original_sentences, cleaned_sentences
