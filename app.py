import streamlit as st

with st form("my_form"):
    st.write("My Form")
    name = st.text_input("Your name ?")

    submitted = st.form_submit_button("Submit")

    if submitted:
      st.write(f"Hi {name}")
