import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    # message = message + "\n" + user_email
    message = f"""\n
    Subject: New email from {user_email}
    From: {user_email}
    {raw_message}
    """
    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info("Your email was sent successfully")

        # print(button)
        # print("I was pressed")

