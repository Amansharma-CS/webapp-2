import streamlit as st
from send_email import send_email

st.header("Contact me ")

with st.form(key="email_form"):
    email = st.text_input("Enter Your Email")
    raw_message = st.text_area("Enter Your Message")
    message = f"""\
subject: New mail from {email}
from: {email}
{raw_message}"""
    button = st.form_submit_button("Send")
    if button:
        send_email(message)
        st.info("Email sent successfully")