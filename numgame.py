import streamlit as st

# Session state variable to track button click
if 'submitted' not in st.session_state:
  st.session_state['submitted'] = False

st.header("WELCOME")
st.subheader("My name is Afsarva Hussain Mubarak")
st.write("**I can tell what number you're thinking...**")

def user_input(num):
 st.write("**the number you're thinking is:**", num)

st.subheader("Let's Start")

num = st.number_input("**think a number**")

# Submit button and progress bar
submitted = st.button("**Find**", key="submit_button")
if submitted:
  st.session_state['submitted'] = True
  with st.empty():
    for i in range(101):
      st.progress(i)  # Update progress bar
      if i == 100:  # Simulate calculation completion after reaching 100%
        st.success(f"**the number you're thinking is: {num}**")  # Display user_age as result
        st.session_state['submitted'] = False  # Reset button state

# Hide progress bar if button not clicked
if not st.session_state['submitted']:
  st.empty()
