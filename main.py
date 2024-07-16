import streamlit as st

st.set_page_config(layout="wide")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Gaurav Pandey")
    content = """
    Aspiring dev partially caring about college :)
    
    """
    st.info(content)
content2 = """
          Below you can find some of the apps i have built in Python.Feel free to contact me!
          """
st.write(content2)
