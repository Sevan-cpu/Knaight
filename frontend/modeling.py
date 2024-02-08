import requests 
import streamlit as st
import http.client
import json
import time

API_HOST = "backend_serv"
API_PORT = 8000



def generate_text(prompt):
    conn = http.client.HTTPConnection(API_HOST, API_PORT)
    headers = {"Content-type": "application/json"}
    data = {"prompt": prompt}
    json_data = json.dumps(data)
    conn.request("POST", "/generate/", json_data, headers)
    response = conn.getresponse()
    result = json.loads(response.read().decode())
    conn.close()
    return result["task_id"]


def get_task_status(task_id):
    conn = http.client.HTTPConnection(API_HOST, API_PORT)
    conn.request("GET", f"/task/{task_id}")
    response = conn.getresponse()
    status = response.read().decode()
    conn.close()
    return status

#AVATARS
av_us = 'avatar/man.png'
av_ass = 'avatar/lamini.png'


#TITLE
st.title("🦙 AI Builders ChatBot")
st.subheader("For internal use only")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message(message["role"],avatar=av_us):
            st.markdown(message["content"])
    else:
        with st.chat_message(message["role"],avatar=av_ass):
            st.markdown(message["content"])



# React to user input
if prompt := st.chat_input("What is up?"):

    # Display user message in chat message container
    with st.chat_message("user", avatar=av_us):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})


    # Display assistant response in chat message container
    with st.chat_message("assistant", avatar=av_ass):
        # For streaming
        message_placeholder = st.empty()
        full_response = ""

        task_id = generate_text(prompt)


        while True:
            status = get_task_status(task_id)
            if "Task not completed yet" not in status:
                print(status)
                break
            time.sleep(2)
        full_response += status               
        message_placeholder.markdown(status)

        # with requests.get(url, stream=True) as r:
        #     # printing response of each stream
        #     for chunk in r.iter_content(1024):
        #         response = chunk.decode("utf-8")
        #         full_response += response                
        #         message_placeholder.markdown(full_response + "▌")
        #     message_placeholder.markdown(full_response)


    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})