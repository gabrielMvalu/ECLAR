import streamlit as st 
from streamlit_timeline import timeline

st.set_page_config(layout="wide")
st.title(':blue[ECLAR SRL]')
st.subheader('pagina demonstrativa statistici / date locale / evenimente / etc.')
st.divider()


with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=400)
