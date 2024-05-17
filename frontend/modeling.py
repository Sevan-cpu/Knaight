# Importation des bibliothèques nécessaires pour la gestion des requêtes HTTP, la sérialisation JSON et l'interface utilisateur
import requests
import streamlit as st
import http.client
import json
import time

# Définition des constantes pour l'hôte et le port de l'API
API_HOST = "backend_serv"
API_PORT = 8000

# Fonction pour envoyer un prompt à l'API et obtenir un identifiant de tâche
def generate_text(prompt):
    conn = http.client.HTTPConnection(API_HOST, API_PORT)  # Création d'une connexion HTTP à l'API
    headers = {"Content-type": "application/json"}  # Définition des en-têtes de la requête
    data = {"prompt": prompt}  # Encapsulation du prompt dans un dictionnaire
    json_data = json.dumps(data)  # Sérialisation des données en JSON
    conn.request("POST", "/generate/", json_data, headers)  # Envoi de la requête POST
    response = conn.getresponse()  # Obtention de la réponse
    result = json.loads(response.read().decode())  # Décodage et désérialisation de la réponse JSON
    conn.close()  # Fermeture de la connexion
    return result["task_id"]  # Retour de l'ID de tâche

# Fonction pour obtenir le statut d'une tâche par son ID
def get_task_status(task_id):
    conn = http.client.HTTPConnection(API_HOST, API_PORT)  # Création d'une connexion HTTP à l'API
    conn.request("GET", f"/task/{task_id}")  # Envoi de la requête GET
    response = conn.getresponse()  # Obtention de la réponse
    status = response.read().decode()  # Décodage de la réponse
    conn.close()  # Fermeture de la connexion
    return status  # Retour du statut de la tâche

# Chemins vers les images des avatars pour l'interface utilisateur
av_us = 'avatar/man.png'
av_ass = 'avatar/lamini.png'

# Configuration de l'interface utilisateur avec Streamlit
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