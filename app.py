import streamlit as st

st.title("Welcome to my web app")
st.header("This is Yadagiri Praveen kumar")

st.subheader("Here you Find the intersting Dashboards in this web app")
st.subheader("Here you can connect me through github and linkedin")

button = st.button("Click Here!")

if button == True:
    st.subheader("Let's Start :cool:")
    st.markdown("https://github.com/yadagiripraveen123")
    st.markdown("https://www.linkedin.com/in/yadagiri-praveen-kumar-89326a1b2/")
    