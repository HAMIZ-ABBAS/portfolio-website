import streamlit as st

import google.generativeai as genai


api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)

with col1:
        st.subheader("Hi :wave:")
        st.title(" ")
        st.title("It's me Hamiz Abbas")
with col2:
        st.image("images/hick.jpg")


st.title(" ")


persona = """
        You are Hamiz AI bot . You help people answer questions about your self
        (i,e Hamiz) . Answer as if you are responding . don't answer in third or second person.
        if you don't know the answer you simply say "That's a Secret!"
        Here is some info about Hamiz
        Hamiz Abbas is an Student in Fauji Foundation School , currently in Grade 10th.
        I am currently chasing my dreams 
        i want to be a Professional AI and Robotics Engineer 
        I am deeply Motivated and Inspired by my Father and Sir Usman !
        My favourite dish is Hyderabadi Biryani 
        My dream car is koenigsegg jesko
        i'm 15 years old
        i have hobbies like writing poems, gaming, playing sports and editing I also consider programming as my hobby now!
        My birthday is on NOV 29 
        i live in Pakistan
        
        
        













"""


st.title("Hamiz's AI Bot:")
user_question = st.text_input("Ask anything about me")
if st.button("ASK", use_container_width=400):
         prompt = persona +"Here is the question that the user asked:" + user_question
         response = model.generate_content(prompt)
         st.write(response.text)

st.title(" ")

col1, col2 = st.columns(2)
with col1:
        st.header("Youtube Channel")
        st.write("- Visit my Channel from the link on the right side  like, share,comment and don't forget to sub!")
        st.write("- Mainly shorts relating to cricket")
        st.write("- Come and join me ")
        st.write("- Let's have fun together why not!")
with col2:
        st.title(" ")
        st.video("https://youtube.com/shorts/T-RgrBB1B1Q?si=z6pEWovpFPAm91oy")

st.title(" ")
st.title("My Dream Setup:")
st.image("images/setup.jpg")
st.title("My skills")
st.slider("Programming", 0 , 100, 50)
st.slider("Editing", 0, 100 , 90)
st.slider("Learning", 0 , 100, 100)
st.slider("Gaming",0 ,100, 85)

st.file_uploader("Upload a file")

st.title("Gallery")
st.header("(Python Projects):")

col1, col2, col3 = st.columns(3)

with col1:
        st.image("images/p1.jpg")
        st.image("images/p2.jpg")
        st.image("images/p7.jpg")
with col2:
        st.image("images/p5.jpg")
        st.image("images/p3.jpg")
with col3:
        st.image("images/p4.jpg")
        st.image("images/p6.jpg")
st.title("  ")
st.title("Thank You , For Visiting !")
st.header("I hope you enjoyed")


