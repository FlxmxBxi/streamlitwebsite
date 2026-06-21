import streamlit as s
from backend import chat

s.title("Hi, how can I help You today? ")
s.write("Calvin is the best programmer")
with s.sidebar:
    s.write("Settings")
    Current_Chat = s.radio("pick the type", ["Genius", "Average", "Stupid"])
s.audio_input(label = "Insert message below", sample_rate=16000, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", width="stretch")
with s.chat_message(name = "Bot", avatar="🤖", width="stretch"):
    s.write("How can I help You today")
input = s.chat_input("Type your message")

if Current_Chat not in s.session_state:
    if Current_Chat = "Genius":
        s.session_state[Current_Chat] = [{"role": "system", "content": "No Emojis, You answer every question seriously without jokes or humor ( Maybe a little )"}]

    if Current_Chat = "Average":
        s.session_state[Current_Chat] = [{"role": "system", "content": "you answer each question correctly with jokes and humor, but add the humor in a natural way"}]
    
    if Current_Chat = "Stupid":
        s.session_state[Current_Chat] = [{"role": "system", "content": "You are single handedly most retar*ed AI, even a 3 year old toddler is smarter, you make the unfunniest jokes and answer every question wrong, evern making some spelling mistakes"}]
    
# Display chat messages from history on app rerun
for message in s.session_state[Current_Chat]:
    with s.chat_message(message["role"]):
        s.markdown(message["content"])

if input:
    with s.chat_message(name = "user", width="stretch"):
        s.write(input)
    s.session_state[Current_Chat].append({"role": "user", "content": input})

    with s.chat_message(name = "assistant", width ="stretch"):
        chatt = s.write_stream(chat(s.session_state[Current_Chat])) 
    s.session_state[Current_Chat].append({"role": "user", "content": chatt})

