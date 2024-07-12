import streamlit as st

st.header("WELCOME")
st.subheader("My name is Afsarva Hussain Mubarak")
st.write("**I can tell what number you're thinking...**")

def user_input(num):
 st.write("**the number you're thinking is:**", num)

st.subheader("Let's Start")

num = st.number_input("**think a number**")

if st.button("**tell me**"):
 user_input(num)
