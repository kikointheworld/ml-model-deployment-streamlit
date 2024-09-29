import streamlit as st
import time
from PIL import Image

st.title('Machine Learning Model Deployment at the server')

# header
st.header("Introduction")

# subheading
st.subheader("This is subheader")

# text data
st.text("This is text")

# read input from the user
input_text = st.text_input('Type something', "default text....")
st.text(input_text)

input_text = st.text_area("Enter here", "this is large text area")

# markdown
st.markdown('This is __really important__')
st.markdown('## This isreally important')

# Button
button = st.button("Click Me")
if button:
    st.text("Button is clicked!")
    st.info("I am clicked!! Snap me fast!!")
    st.toast("I am disappear")
    st.warning("df")
    st.error("erroe")

# Image
st.image("kgptalkie.png")
img = Image.open("kgptalkie.png")
st.image(img)

# check box
flag = st.checkbox("Select me")
st.text(flag)

if flag:
    st.image(img)


# radio button
selection = st.radio("Choose your model", ["NLP", "Image", "Audio"])
st.write(selection)

# radio button
selection = st.selectbox("Choose your model", ["NLP", "Image", "Audio"])
st.write(selection)

# multi select
selection = st.multiselect("Choose your model", ["NLP", "Image", "Audio"])
st.write(selection)

# select numerical value from the given list
# TH = 0.5, large TH -> hight precision, small TH -> high recall
a = st.slider("Set Threshold", 0, 100, step = 10)

with st.spinner("Downloading... Please wait"):
    st.write("download your model here")
    time.sleep(10)