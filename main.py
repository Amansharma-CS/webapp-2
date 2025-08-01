import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/hariom.png")

with col2:
    st.title("Aman Sharma")
    content = """
    Hi , my name is aman sharma and i am a good boy.
    I am trying to learn python .
    Hari OM and my father name is navin sharma, my mother name is sunita sharma and my sisters name is bulbul and sheena
    and my jiju name is gourav . 
     """
    st.info(content)