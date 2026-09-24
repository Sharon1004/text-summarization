from backend.summarizer import summarize_text


def test_single_sentence():
    text = "Machine learning is useful."

    result = summarize_text(text, 1)

    assert result == text


def test_summary_is_not_empty():
    text = (
        "Machine learning is useful. "
        "Python is widely used for machine learning. "
        "Data is important for machine learning."
    )

    result = summarize_text(text, 2)

    assert result.strip() != ""


def test_summary_length():
    text = (
        "Machine learning is useful. "
        "Python is widely used for machine learning. "
        "Data is important for machine learning."
    )

    result = summarize_text(text, 2)

    assert len(result.split(". ")) <= 2