import streamlit as st

#NLP Pkgs
import spacy
from textblob import TextBlob

@st.cache
def text_analyzer(my_text):
    nlp = spacy.load("en_core_web_sm")
    docx = nlp(my_text)
    tokens = [token.text for token in docx]
    allData = [('"Token":{},\n"Lemma":{}'.format(token.text,token.lemma_))for token in docx ]
    return allData

@st.cache
def entity_analyzer(my_text):
    nlp = spacy.load("en_core_web_sm")
    docx = nlp(my_text)
    tokens = [ token.text for token in docx]
    entities = [(entity.text,entity.label_)for entity in docx.ents]
    allData = ['"Token":{},\n"Entities":{}'.format(tokens,entities)]
    return allData

   
# Pkgs



def main():
    """ NLP App with Streamlit """
    st.title("NLPiffy with Streamlit")
    st.subheader("Natural Language Processing on the Go")

    # Tokenization
    if st.checkbox("Show Tokens and Lemma"):
        st.subheader("Tokenize Your Text")
        message = st.text_area("Enter Your Text","Type Here")
        if st.button("Analyze"):
            nlp_result = text_analyzer(message)
            st.json(nlp_result)
    # Named Entity


    if st.checkbox("Show Named Entities"):
            st.subheader("Analyze Your Text")
            message = st.text_area("Enter Text","Type Here ..")
            if st.button("Extract"):
                        entity_result = entity_analyzer(message)
                        st.json(entity_result)

    # Sentiment Analysis

    # Text Summarizaion




if __name__ == '__main__':
    main()

