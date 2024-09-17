import streamlit as st

with st.form("my_form"):
    st.write("My Form")
    name = st.text_input("Your name ?")
    
    longitude = st.slider("longitude", 0, 100, 25)
    latitude = st.slider("latitude", 0, 100, 25)
    housing_median_age = st.slider("housing_median_age", 0, 100, 25)
    total_rooms = st.selectbox("total_rooms", range(50))
    total_bedrooms = st.slider("total_bedrooms", 0, 100, 25)
    population = st.slider("population", 0, 100, 25)
    households = st.slider("households", 0, 100, 25)
    median_income = st.slider("median_income", 0, 100, 25)
    median_house_value = st.slider("median_house_value", 0, 100, 25)

    submitted = st.form_submit_button("Submit")

    if submitted:
      st.write(f"Submitted !")
