import streamlit as st
import numpy as np


if "color" not in st.session_state:
    st.session_state.color = "Green"


st.title("Hello World")

st.write("This is a simple example of Streamlit")

st.session_state.color = st.radio("What is your favorite color?", ("Blue", "Red", "Green"))

if st.session_state.color != "":
    st.write(f"Your favorite color is {st.session_state.color}")



with st.container():
    st.write("This is inside the container")
    st.button("This is a button")
    st.bar_chart(np.random.randn(50, 3))