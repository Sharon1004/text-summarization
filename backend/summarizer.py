import nltk
import numpy as np
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)

def summarize_text(text,summary_length):
    
    #Convert given paragraph into tokens of sentences
    #gives list of sentences
    sentences=sent_tokenize(text)
    if len(sentences) <= 1:
        return sentences[0] if sentences else ""
    stop_words = stopwords.words("english")

    #(fit)=> Identify unique words in the sentences and
    # (transform)=> assign scores for each word in the sentence
    #gives a matrix of scores for each word in each sentence
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    tfidf_matrix=vectorizer.fit_transform(sentences)

    #Calculate average score for each sentence
    sentence_scores=np.mean(tfidf_matrix.toarray(),axis=1)

    #Sort the sentences based on their scores in ascending order and reverse it
    #gives the list of arranged indices
    ranked_scores=np.argsort(sentence_scores)[::-1]
    print("\nSentence Scores:")

    for i, score in enumerate(sentence_scores):
        print(f"Sentence {i + 1}: {score:.4f}")
        print(sentences[i])

    #pick top indices based on the summary length
    summary_length = min(summary_length, len(sentences))

    top_indices = ranked_scores[:summary_length]

    #Preserve the original order
    top_indices.sort()

    #get the original sentences corresponding to the top indices
    selected_sentences=[sentences[i] for i in top_indices]

    #join them together to form the summary
    summary="".join(selected_sentences)
    original_words = len(text.split())
    summary_words = len(summary.split())
    compression_ratio = (
    1 - summary_words / original_words) * 100

    return summary
