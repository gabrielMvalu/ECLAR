import streamlit as st
from streamlit_timeline import timeline

st.set_page_config(layout="wide")

# Utilizarea coloanelor pentru a plasa logo-ul lângă titlu
col1, col2 = st.columns([1, 9])

# În prima coloană, afișează logo-ul
with col1:
    st.image("./data/logoECLAR.png", width=100)  # Ajustează 'width' după necesități

# În a doua coloană, afișează titlul
with col2:
    st.header(":blue:[ECLAR SRL]")

st.divider()

with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=400)
