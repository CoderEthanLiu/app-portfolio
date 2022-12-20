import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.JPG")
with col2:
    st.title("Ethan (Shihui) Liu")
    content = """
    Hi, I am Ethan (Shihui) Liu. I graduated in 2022 with a Master of Science in Computing from the Cardiff 
University in the UK with a focus on using Python.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")
print(df[:10])
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
