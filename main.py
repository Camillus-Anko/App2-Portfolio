import streamlit as st
import pandas # Installed alongside pandas

st.set_page_config(layout="wide") #Configururations about your page

col1, col2 = st.columns(2) #Create two column objects

with col1: #Open with a context manager
    st.image("images/photo.png")

with col2:
    st.title("Camillus Anko")
    content = """
    Hi, I am Camillus! I am a Python programmer, teacher, and founder of PythonHow. I graduated in 2013 with a Master of Science in Geospatial Technologies from the University of Muenster in Germany with a focus on using Python for remote sensing.
I have worked with companies from various countries, such as the Center for Conservation Geography, to map and understand Australian ecosystems, image processing with the Swiss in-Terra, and performing data mining to gain business insights with the Australian Rapid Intelligence.
    """
    st.info(content)


content2 = """
Below you can find some of the apps I have built in Python. 
Feel Free to contact me!
"""

# st.info(content2)
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])

        


