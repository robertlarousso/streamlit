import streamlit as st

with st.form("my_form"):
    st.write("My Form")
    name = st.text_input("Your name ?")
    
    longitude = st.slider("longitude", 0, 100, 25)
    "latitude" = st.slider("longitude", 0, 100, 25)
    "housing_median_age" = st.slider("longitude", 0, 100, 25)
    "total_rooms" = st.selectbox("longitude", range(50))
    "total_bedrooms" = st.slider("longitude", 0, 100, 25)
    "population": = st.slider("longitude", 0, 100, 25)
    "households" = st.slider("longitude", 0, 100, 25)
    "median_income": = st.slider("longitude", 0, 100, 25)
    "median_house_value" = st.slider("longitude", 0, 100, 25)

    submitted = st.form_submit_button("Submit")

    if submitted:
      st.write(f"Submitted !")
