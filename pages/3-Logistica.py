import streamlit as st 
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.set_page_config(layout="wide")
st.image("./data/logoECLAR.png", width=100) 
st.divider()


# Definim coordonatele pentru centrul României și pentru Bailești
center_of_romania = [45.9432, 24.9668]  # Coordonate aproximative pentru centrul României
bailesti_location = [44.01, 23.35]  # Coordonate pentru Bailești

# Creăm un DataFrame cu puncte aleatorii în România
df_random_points = pd.DataFrame({
    "latitude": np.random.uniform(low=43.5, high=48.0, size=100),  # Latitudini aleatorii în intervalul geografic al României
    "longitude": np.random.uniform(low=20.0, high=29.0, size=100),  # Longitudini aleatorii în intervalul geografic al României
})

# Adăugăm un punct special pentru Bailești
df_bailesti = pd.DataFrame({
    "latitude": [bailesti_location[0]],
    "longitude": [bailesti_location[1]],
})

# Configurăm harta PyDeck
view_state = pdk.ViewState(
    latitude=center_of_romania[0],
    longitude=center_of_romania[1],
    zoom=5.5,
    pitch=0
)

# Layer pentru punctele aleatorii
layer_random_points = pdk.Layer(
    'ScatterplotLayer',
    data=df_random_points,
    get_position='[longitude, latitude]',
    get_color='[200, 30, 0, 160]',
    get_radius=5000,
)

# Layer pentru Bailești
layer_bailesti = pdk.Layer(
    'ScatterplotLayer',
    data=df_bailesti,
    get_position='[longitude, latitude]',
    get_color='[0, 0, 255, 160]',  # Albastru pentru a-l distinge
    get_radius=10000,  # Un radius mai mare pentru a evidenția locația
)

# Renderăm harta
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=view_state,
    layers=[layer_random_points, layer_bailesti]
))






