import streamlit as st 
import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "col1": 23.35,
    "col2": 44.01,
    "col3": np.random.randn(1000) * 200,
    "col4": np.random.rand(1000, 10).tolist(),
})

st.map(df,
    latitude='col1',
    longitude='col2',
    size='col3',
    color='col4')




st.set_page_config(layout="wide")
st.image("./data/logoECLAR.png", width=100) 
st.divider()

