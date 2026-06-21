import streamlit as s
from backend import chat

s.title("Hi, how can I help You today? ")
s.write("Calvin is the best programmer")
with s.sidebar:
    s.write("Settings")
    CurrentChat = s.radio("pick the type", ["Genius", "Average", "Stupid"])
s.audio_input(label = "Insert message below", sample_rate=16000, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", width="stretch")
with s.chat_message(name = "Bot", avatar="🤖", width="stretch"):
    s.write("How can I help You today")
input = s.chat_input("Type your message")

if "messages" not in s.session_state:
    s.session_state.messages = []

# Display chat messages from history on app rerun
for message in s.session_state.messages:
    with s.chat_message(message["role"]):
        s.markdown(message["content"])

if input:
    with s.chat_message(name = "user", width="stretch"):
        s.write(input)
    s.session_state.messages.append({"role": "user", "content": input})

    with s.chat_message(name = "assistant", width ="stretch"):
        chatt = s.write_stream(chat(s.session_state.messages)) 
    s.session_state.messages.append({"role": "user", "content": chatt})

