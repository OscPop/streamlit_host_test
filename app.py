import streamlit as st

st.title("Hello World")

st.write("This is a simple example of Streamlit")

st.session_state.color = st.radio("What is your favorite color?", ("Blue", "Red", "Green"))

if st.session_state.color != "":
    st.write(f"Your favorite color is {st.session_state.color}")
