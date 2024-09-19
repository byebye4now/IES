import streamlit as st
st.header("INTEGRAL")
st.write("Integral Energy Solution")
st.sidebar.header("Welcome to Integral Energy Solution")
st.sidebar.write("We provide the following services: ")



#st.subheader('')
options = st.multiselect(
    "We provide the following services: ",
    ["nergy System Design", "Energy System Deployment", "Procurement", "R&D"]
)

