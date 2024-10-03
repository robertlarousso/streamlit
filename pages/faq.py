import streamlit as st

st.title("FAQ")

# Initialize chat history
faq = []

faq.append({"role": "assistant", "content": "Première question de la FAQ ??"})
faq.append({"role": "user", "content": "Réponse à la première question de la FAQ"})

# Display chat messages from history on app rerun
for message in faq:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

