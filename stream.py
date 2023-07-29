import streamlit as st
import time as t
# title - It used to add the title of an app
st.title("welcome to my test site.")

# Header
st.header("Machine Learning")

# subheader

st.subheader("Linear Regression")

# Information

st.info("Information details of a user")

# Warning message
st.warning("Be punctual or else you will be marked abscent!")

# Error message
st.error("Wrong password")

# Success message
st.success("Congrats you have got A grade!!!")

# write
st.write("Employee name")
st.write(range(50))

# Markdown
st.markdown("# Estifanos")

st.markdown(":moon:")

# Caption
st.caption("caption is here")

# maths expression

st.latex(r''' a+b x^2+c ''')


#widget
# checkbox

st.checkbox('Login')

# button

st.button("Click ")

# Radio widget

st.radio("Pick your gender",["Male","Female","Other"])

# select box
st.selectbox("Pick your course",["ML","Phonetics","NLP","Syntax"])

# multiselect
st.multiselect("Choose your department",["Law","Linguistics","Philology","IT"])

# select_slider
st.select_slider("Rating",["Bad","Good","Excellent","Outstanding"])

# slider
st.slider("Enter your number",0,30)

# number_input
st.number_input("Pick a  number",0,100)

# text_input
st.text_input("Enter your email address")

# date input
st.date_input("Opening ceremony")

# time input
st.time_input("Hey what the time is it now")

# text area
st.text_area("Welcome to the intellipaat area website. Hello learners!")

st.file_uploader("upload your file/folder")

st.color_picker("color")

st.progress(90)

# spinner
with st.spinner("Just wait"):
    t.sleep(2)

# ballon
st.balloons()

# sidebar
st.sidebar.title("welcome to Tolemariam")
st.sidebar.text_input("Mail Address")
st.sidebar.text_input("Password")
st.sidebar.text_input("Submit")
st.sidebar.radio("Professional Expert",["Student","Consultant","Other"])

#Data visualization
import pandas as pd
import numpy as np
st.title("Bar Chart")
data=pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
st.bar_chart(data)
st.title("Line Chart")
st.line_chart(data)
st.area_chart(data)