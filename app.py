import streamlit as s

s.set_page_config(page_title="WILLIAM BUTCHER.AI",page_icon=":collision:",layout="wide")
with s.container():
    s.title("VELTECH HIGHTECH Dr.RANGARAJAN Dr.SAKUNTHALA ENGINEERING COLLEGE")
    s.subheader("Aavishkaar Project Expo 2024 :heart_on_fire:")
    s.write("[About this Event >](https://velhightech.com)")
    s.title("Hi! I am William Butcher :speech_balloon: ")


from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyCsKBsxEb95bQh31g8vbYwyu1ITsOwoJ3U")

model=genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])
def get_butcher_response(question):
    
    response=chat.send_message(question,stream=True)
    return response
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

with st.container():
    c1,c2=st.columns(2)
    with c1:
        input=st.text_input(label='')
    with c2:
        submit=st.button("Enter")

if ("name" not in input) and (input.lower()!="who are you"):
    if submit and input:
        response=get_butcher_response(input)
        st.session_state['chat_history'].append(("You", input))

        for chunk in response:
            st.write(chunk.text)
            st.session_state['chat_history'].append(("Butcher", chunk.text))
        
 #   for role in st.session_state['chat_history']:
 #       st.write(f"{role}:{response}")
elif input.lower()=="who are you":
    st.write("Butcher : The name is William Butcher")
else :
    st.write("Butcher : seems like you are asking my name , if you are , then the name is BUTCHER else ask your question with the word \"name\" spelled as \"nam\"")
    
with st.container():
    st.write("---")
    left_column,right_column= st.columns(2)
    with left_column:
        st.header("OI!")
        st.write("##")
        st.subheader("=> You can ask me anything.. ")  
        st.subheader("=> I will answer it...The best way possible")
        st.subheader("=> I have access to internet up to date")
        st.subheader("=> I am powered by generative api by google")
        st.subheader("=> I am completely developed by python")
        st.subheader("=> Don't ever ask my name.")

    with right_column:
        image_url="https://cdna.artstation.com/p/assets/images/images/051/522/774/large/jonathan-kagimba-butcher2.jpg?1657528840"
        st.image(image_url,caption="Butcher",width=550)


st.title ("Crew Members... ")
with st.container():
    st.write("---")
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.subheader("DINESH KUMAR E.")
        st.subheader("VH12761")
    with col2:
        st.subheader("ANAND S.")
        st.subheader("VH12739")
    with col3:
        st.subheader("BALA KUMAR T.")
        st.subheader("VH12746")
    with col4:
        st.subheader("HARINI M.")
        st.subheader("VH12776")
    with col5:
        st.subheader("AKSHAYAA S.")
        st.subheader("VH12736")

with st.container():
    st.subheader("Contact: team_7@myyahoo.com")