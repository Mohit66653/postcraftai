import streamlit as st
from lm_helper import generate_post

st.title("LinkedIn Post Generator")

topic = st.text_input("What is your post about?")

tone = st.selectbox(
    "Choose the tone",
    ["Professional", "Casual", "Motivational"]
)

length = st.selectbox(
    "Choose the length",
    ["Short", "Medium", "Long"]
)

if st.button("Generate Post"):
    if topic:
        post = generate_post(topic, tone, length)
        st.write(post)
    else:
        st.warning("Please enter a topic.")