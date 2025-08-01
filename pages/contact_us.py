import streamlit as st

st.header("Contact me ")

with st.form(key="email_form"):
    email = st.text_input("Enter Your Email")
    message = st.text_area("Enter Your Message")
    button = st.form_submit_button("Send")
    