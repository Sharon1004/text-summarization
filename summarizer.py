import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from preprocessing import preprocess_text

def summarize_text(text, num_sentences=3):
    original_sentences, cleaned_sentences = preprocess_text(text)

    # Filter out very long sentences (like lists)
    filtered_original = []
    filtered_cleaned = []

    for orig, clean in zip(original_sentences, cleaned_sentences):
        if len(orig.split()) <= 35:   # sentence length threshold
            filtered_original.append(orig)
            filtered_cleaned.append(clean)

    if len(filtered_original) <= num_sentences:
        return " ".join(filtered_original)

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(filtered_cleaned)

    sentence_scores = tfidf_matrix.sum(axis=1).A1
    ranked_indices = np.argsort(sentence_scores)[::-1]

    selected_indices = sorted(ranked_indices[:num_sentences])
    summary = " ".join([filtered_original[i] for i in selected_indices])

    return summary
