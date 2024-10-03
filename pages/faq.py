import streamlit as st

st.title("FAQ")

# Initialize chat history
if "faq" not in st.session_state:
    st.session_state.faq = []

st.session_state.faq.append({"role": "assistant", "content": "Première question de la FAQ ??"})
st.session_state.faq.append({"role": "user", "content": "Réponse à la première question de la FAQ"})

# Display chat messages from history on app rerun
for message in st.session_state.faq:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

