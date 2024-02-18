import streamlit as st
from streamlit_timeline import timeline

st.set_page_config(layout="wide")

st.image("./data/logoECLAR.png", width=100)  # Ajustează 'width' după necesități

st.divider()

with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=400)
