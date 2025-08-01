import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/hariom.png", width=800)

with col2:
    st.title("Aman Sharma")
    content = """
    Hi , my name is aman sharma and i am a good boy.
    I am trying to learn python .
    Hari OM and my father name is navin sharma, my mother name is sunita sharma and my sisters name is bulbul and sheena
    and my jiju name is gourav . 
     """
    st.info(content)
content2 = """ Below you can find some apps which i have created on my own in python .
feel free to contact me """
st.write(content2)

col3, empty_col, col4 = st.columns([1,0.5,1])

df = pandas.read_csv("data.csv")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
