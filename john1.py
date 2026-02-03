import streamlit as st

st.title("🤖 Ennoda Chatbot")

# Chat history-ah maintain panna
if "messages" not in st.session_state:
    st.session_state.messages = []

# Pazhaya chat-ah screen-la kaata
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User kitta irundhu input vanga
if prompt := st.chat_input("Enna kekkanum?"):
    # User message-ah add panna
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Bot response (Inga dhaan unga logic varum)
    response = f"Neenga '{prompt}' nu sonninga, idhu nalla iruke!"
    
    # Bot message-ah add panna
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
