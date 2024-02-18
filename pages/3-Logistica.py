import streamlit as st 
import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(layout="wide")
st.image("./data/logoECLAR.png", width=100) 
st.divider()

# Creăm un DataFrame cu coloane pentru latitudine și longitudine
df = pd.DataFrame({
    "latitude": np.random.randn(1000) / 50 + 44.01,  # Am redenumit 'col1' în 'latitude'
    "longitude": np.random.randn(1000) / 50 + 23.35,  # Am redenumit 'col2' în 'longitude'
    "col3": np.random.randn(1000) * 100,
    "col4": np.random.rand(1000, 4).tolist(),
})

# Utilizăm funcția 'st.map' doar cu coloanele de latitudine și longitudine
st.map(df)





