import requests
import streamlit as st


st.title("Text Summarization System")
st.caption(
    "An extractive text summarization system using TF-IDF and sentence ranking."
)

st.write("Enter some text and generate a concise summary.")

text=st.text_area("Enter your text here", height=250)

summary_length=st.slider("Number of sentencesin summary:",min_value=1,max_value=10,value=3)


if st.button("Generate Summary"):

    if not text:
        st.error("Please enter some text first.")
    else:
        try:
            response=requests.post("http://127.0.0.1:8000/summarize",json={
                "text":text,"summary_length":summary_length
                },
                timeout=10
            )

            response.raise_for_status()

            result=response.json()
            summary=result["summary"]
        
            st.subheader("Summary:")
            st.write(summary)

            original_words = len(text.split())
            summary_words = len(summary.split())
        
            if original_words > 0:
                reduction = (1 - summary_words / original_words) * 100
            else:
                reduction = 0
            col1, col2, col3 = st.columns(3)
        
            with col1:
                st.metric("Original Words", original_words)
        
            with col2:
                st.metric("Summary Words", summary_words)
        
            with col3:
                st.metric("Reduction", f"{reduction:.1f}%")
        
            st.download_button(
                label="Download Summary",
                data=result["summary"],
                file_name="summary.txt",
                mime="text/plain")
        
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the API.")  
        except requests.exceptions.Timeout:
            st.error("The request took too long. Please try again later.")
        except requests.exceptions.RequestException as e:
            st.error(f"API request failed: {e}")


    