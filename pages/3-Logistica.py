import streamlit as st 
import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "col1": np.random.randn(1000) / 50 + 44.01,
    "col2": np.random.randn(1000) / 50 + 23.35,
    "col3": np.random.randn(1000) * 100,
    "col4": np.random.rand(1000, 4).tolist(),

st.map(df,
    latitude='44.01',
    longitude='23.35',
    size='col3',
    color='col4')




st.set_page_config(layout="wide")
st.image("./data/logoECLAR.png", width=100) 
st.divider()

