import streamlit as st 
import pandas as pd
import numpy as np
import pydeck as pdk

st.set_page_config(layout="wide")
st.image("./data/logoECLAR.png", width=100) 
st.divider()

# Coordonatele pentru centrul României și pentru Bailești
center_of_romania = [45.9432, 24.9668]  # Coordonate aproximative pentru centrul României
bailesti_location = [44.01, 23.35]  # Coordonate pentru Bailești

# Creăm un DataFrame cu puncte aleatorii în România
df_random_points = pd.DataFrame({
    "latitude": np.random.uniform(low=44.00, high=47.3, size=30),  # Latitudini aleatorii în intervalul geografic al României
    "longitude": np.random.uniform(low=23.30, high=28.0, size=30),  # Longitudini aleatorii în intervalul geografic al României
})

# Creăm un DataFrame pentru linii, care conectează Bailești cu fiecare punct aleatoriu
df_lines = pd.DataFrame({
    "source": [[bailesti_location[1], bailesti_location[0]]] * len(df_random_points),  # Format corect [longitude, latitude]
    "target": list(zip(df_random_points["longitude"], df_random_points["latitude"]))  # Format corect [longitude, latitude]
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
    data=pd.DataFrame({"latitude": [bailesti_location[0]], "longitude": [bailesti_location[1]]}),
    get_position='[longitude, latitude]',
    get_color='[0, 0, 255, 160]',  # Albastru pentru a-l distinge
    get_radius=10000,  # Radius mai mare pentru a evidenția locația
)

# Layer pentru linii
layer_lines = pdk.Layer(
    "LineLayer",
    data=df_lines,
    get_source_position="source",
    get_target_position="target",
    get_color="[255, 0, 0, 100]",  # Roșu semi-transparent
    get_width=2,
)

# Renderăm harta
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=view_state,
    layers=[layer_random_points, layer_bailesti, layer_lines]
))




