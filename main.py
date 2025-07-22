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

# col3, col4 = st.columns(2)
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5]) #Adding space with empty_col
#ratio dimensions of the 3 columns, 1st column will be 3x wider tham the middle collumn


df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        # st.write("[Source Code] (https://pythonhow.com)") OR
        st.write(f"[Source Code]({row['url']})") #Takes the name of the link "Sorce Code" and the url as argument


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")






