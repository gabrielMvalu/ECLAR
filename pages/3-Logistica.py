import streamlit as st 
import pandas as pd
import numpy as np
import pydeck as pdk
import random

st.set_page_config(layout="wide")
st.image("./data/logoECLAR.png", width=100) 
st.divider()

def hex_to_rgba(hex_color, alpha=255):
    """Converteste o culoare hexadecimale într-un tuple RGBA."""
    hex_color = hex_color.lstrip('#')
    lv = len(hex_color)
    return tuple(int(hex_color[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)) + (alpha,)

# Culori personalizate în format hexadecimale
custom_colors = ["#f7cb39", "#4dc4be", "#ed6347", "#b0a989"]
# Converteste culorile hexadecimale în RGBA
custom_colors_rgba = [hex_to_rgba(color) for color in custom_colors]



col1, col2 = st.columns(2)

with col1:

    # Coordonatele pentru centrul României și pentru Bailești
    center_of_romania = [45.9432, 24.9668]
    bailesti_location = [44.033049, 23.349555] 
    
    # Creăm un DataFrame cu puncte aleatorii în România
    df_random_points = pd.DataFrame({
        "latitude": np.random.uniform(low=44.01, high=47.0, size=30),
        "longitude": np.random.uniform(low=23.0, high=28.0, size=30),
    })
    
    # Creăm un DataFrame pentru linii, care conectează Bailești cu fiecare punct aleatoriu
    df_lines = pd.DataFrame({
        "source": [[bailesti_location[1], bailesti_location[0]]] * len(df_random_points),
        "target": list(zip(df_random_points["longitude"], df_random_points["latitude"])),
        "color": [random.choice(custom_colors_rgba) for _ in range(len(df_random_points))]  # Alege o culoare aleatorie în format RGBA pentru fiecare linie
    })
    
    # Configurăm harta PyDeck pentru linii
    view_state_lines = pdk.ViewState(
        latitude=center_of_romania[0],
        longitude=center_of_romania[1],
        zoom=5.5,
        pitch=45
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
    
    # Renderăm harta pentru linii
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=view_state_lines,
        layers=[layer_lines]
    ))

with col2:
    # Coordonatele centrale pentru județele specificate
    coordonate_judete = {
        'Dolj': [44.3189, 23.7949, 20],  # 20% din vânzări
        'Gorj': [45.0469, 23.2749, 10],  # 10% din vânzări
        'Cluj': [46.7712, 23.6236, 22],  # 22% din vânzări
        'Brașov': [45.6580, 25.6012, 27]  # 27% din vânzări
    }
    
    # Creăm un DataFrame pentru județele selectate
    df_judete = pd.DataFrame.from_dict(coordonate_judete, orient='index', columns=['latitude', 'longitude', 'procent_vanzari'])
    
    # Generăm punctele pentru Heatmap pe baza procentului de vânzări
    puncte_heatmap = []
    for index, row in df_judete.iterrows():
        for _ in range(int(row['procent_vanzari'] * 10)):  # Multiplicăm procentul cu 10 pentru a avea un număr suficient de puncte
            puncte_heatmap.append({'latitude': np.random.normal(row['latitude'], 0.05),
                                   'longitude': np.random.normal(row['longitude'], 0.05)})
    
    df_heatmap = pd.DataFrame(puncte_heatmap)
    
    # Configurăm harta PyDeck pentru Heatmap
    view_state_heatmap = pdk.ViewState(
        latitude=45.9432,  # Centrul geografic al României
        longitude=24.9668,
        zoom=5,
        pitch=0
    )
    
    # Creăm Heatmap Layer
    heatmap_layer = pdk.Layer(
        'HeatmapLayer',
        data=df_heatmap,
        get_position='[longitude, latitude]',
        opacity=0.9,
        get_weight="1"
    )
    
    # Renderăm harta pentru Heatmap
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=view_state_heatmap,
        layers=[heatmap_layer]
    ))

