import streamlit as st
import requests
st.title("FAQ")

# Initialize chat history
faq = []

rep = requests.get(st.session_state["server_url"] + "/chat_bot_histo")
for m in  rep.json():
    faq.append({"role": "user", "content":  m.prompt_user})
    faq.append({"role": "assistant", "content": m.response_gpt})



# Display chat messages from history on app rerun
for message in faq:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

