import streamlit as st 
import pandas as pd
import numpy as np
import pydeck as pdk
import random

def hex_to_rgba(hex_color, alpha=255):
    """Converteste o culoare hexadecimale într-un tuple RGBA."""
    hex_color = hex_color.lstrip('#')
    lv = len(hex_color)
    return tuple(int(hex_color[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)) + (alpha,)

# Culori personalizate în format hexadecimale
custom_colors = ["#f7cb39", "#4dc4be", "#ed6347", "#b0a989"]

# Converteste culorile hexadecimale în RGBA
custom_colors_rgba = [hex_to_rgba(color) for color in custom_colors]

st.set_page_config(layout="wide")
st.image("./data/logoECLAR.png", width=100) 
st.divider()

# Coordonatele pentru centrul României și pentru Bailești
center_of_romania = [45.9432, 24.9668]
bailesti_location = [44.033049, 23.349555] 

# Creăm un DataFrame cu puncte aleatorii în România
df_random_points = pd.DataFrame({
    "latitude": np.random.uniform(low=42.01, high=47.0, size=40),
    "longitude": np.random.uniform(low=22.0, high=28.0, size=40),
})

# Creăm un DataFrame pentru linii, care conectează Bailești cu fiecare punct aleatoriu
df_lines = pd.DataFrame({
    "source": [[bailesti_location[1], bailesti_location[0]]] * len(df_random_points),
    "target": list(zip(df_random_points["longitude"], df_random_points["latitude"])),
    "color": [random.choice(custom_colors_rgba) for _ in range(len(df_random_points))]  # Alege o culoare aleatorie în format RGBA pentru fiecare linie
})

# Configurăm harta PyDeck
view_state = pdk.ViewState(
    latitude=center_of_romania[0],
    longitude=center_of_romania[1],
    zoom=5.9,
    pitch=70
)

# Layer pentru linii, cu culori personalizate în format RGBA
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
    layers=[layer_lines]
))



