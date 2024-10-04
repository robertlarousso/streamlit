import streamlit as st
import requests

server_url = "https://f4a3-35-186-182-93.ngrok-free.app"

def add_bot_mess(mess):
    response = f"{mess}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    add_bot_mess("Comment puis-je vous aider ?")
    

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    myobj = {'message': prompt}
    rep = requests.post(server_url + '/chat_bot', params = myobj)

    add_bot_mess(f"Echo: {response.json().result}")
