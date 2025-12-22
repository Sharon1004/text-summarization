import streamlit as st
from summarizer import summarize_text

st.set_page_config(page_title="Text Summarization System", layout="centered")

st.title("📄 Text Summarization System")
st.write(
    "This system generates concise and coherent summaries of long text documents "
    "using Natural Language Processing techniques."
)

# Text input
input_text = st.text_area(
    "Enter the text you want to summarize:",
    height=250,
    placeholder="Paste your long document here..."
)

# Summary length selector
num_sentences = st.slider(
    "Select number of sentences in summary",
    min_value=1,
    max_value=10,
    value=3
)

# Generate summary button
if st.button("Generate Summary"):
    if input_text.strip():
        summary = summarize_text(input_text, num_sentences)
        st.subheader("📝 Generated Summary")
        st.success(summary)
    else:
        st.warning("Please enter some text to summarize.")
