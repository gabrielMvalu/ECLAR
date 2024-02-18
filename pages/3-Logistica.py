import streamlit as st 
import pandas as pd
import numpy as np
import pydeck as pdk
import random

st.set_page_config(layout="wide")
st.image("./data/logoECLAR.png", width=100) 
st.divider()

# Coordonatele pentru centrul României și pentru Bailești
center_of_romania = [45.9432, 24.9668]
bailesti_location = [44.01, 23.35]

# Creăm un DataFrame cu puncte aleatorii în România
df_random_points = pd.DataFrame({
    "latitude": np.random.uniform(low=43.5, high=48.0, size=20),
    "longitude": np.random.uniform(low=20.0, high=29.0, size=20),
})

# Culori personalizate pentru liniile dintre Bailești și punctele aleatorii
custom_colors = ["#f7cb39", "#4dc4be", "#ed6347", "#b0a989"]

# Creăm un DataFrame pentru linii, care conectează Bailești cu fiecare punct aleatoriu
# și asignăm fiecărei linii o culoare aleasă aleator din lista custom_colors
df_lines = pd.DataFrame({
    "source": [[bailesti_location[1], bailesti_location[0]]] * len(df_random_points),
    "target": list(zip(df_random_points["longitude"], df_random_points["latitude"])),
    "color": [random.choice(custom_colors) for _ in range(len(df_random_points))],  # Alege o culoare aleatorie pentru fiecare linie
})

# Configurăm harta PyDeck
view_state = pdk.ViewState(
    latitude=center_of_romania[0],
    longitude=center_of_romania[1],
    zoom=5.5,
    pitch=45
)

# Layer pentru punctele aleatorii
layer_random_points = pdk.Layer(
    'ScatterplotLayer',
    data=df_random_points,
    get_position='[longitude, latitude]',
    get_color='[200, 200, 200, 160]',  # Culoare gri pentru punctele aleatorii
    get_radius=5000,
)

# Layer pentru Bailești
layer_bailesti = pdk.Layer(
    'ScatterplotLayer',
    data=pd.DataFrame({"latitude": [bailesti_location[0]], "longitude": [bailesti_location[1]]}),
    get_position='[longitude, latitude]',
    get_color='[0, 0, 255, 160]',  # Albastru pentru Bailești
    get_radius=10000,
)

# Layer pentru linii, cu culori personalizate
layer_lines = pdk.Layer(
    "LineLayer",
    data=df_lines,
    get_source_position="source",
    get_target_position="target",
    get_color="color",  # Utilizează coloana 'color' din df_lines pentru culoarea fiecărei linii
    get_width=2,
)

# Renderăm harta
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=view_state,
    layers=[layer_random_points, layer_bailesti, layer_lines]
))



