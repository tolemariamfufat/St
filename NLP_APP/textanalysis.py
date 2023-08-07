import streamlit as st
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

st.set_page_config(layout='wide', initial_sidebar_state='expanded')
st.title('Text Analysis using Spacy Textblob')
st.markdown('Type a sentence in the below text box and choose the desired option in the adjacent menu.')
side = st.sidebar.selectbox("Select an option below", ("Sentiment", "Subjectivity", "NER"))
Text = st.text_input("Enter the sentence")

@st.cache_data
def sentiment(text):
    nlp = spacy.load('en_core_web_sm')
    nlp.add_pipe('spacytextblob')
    doc = nlp(text)
    if doc._.polarity<0:
        return "Negative"
    elif doc._.polarity==0:
        return "Neutral"
    else:
        return "Positive"
    
@st.cache_data
def subjectivity(text):
    nlp = spacy.load('en_core_web_sm')
    nlp.add_pipe('spacytextblob')
    doc = nlp(text)
    if doc._.subjectivity > 0.5:
        return "Highly Opinionated sentence"
    elif doc._.subjectivity < 0.5:
        return "Less Opinionated sentence"
    else:
        return "Neutral sentence"
    
@st.cache_data
def ner(sentence):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)
    ents = [(e.text, e.label_) for e in doc.ents]
    return ents
def run():
    if side == "Sentiment":
        st.write(sentiment(Text))
    if side == "Subjectivity":
        st.write(subjectivity(Text))
    if side == "NER":
        st.write(ner(Text))
if __name__ == '__main__':
    run()
    
