
import streamlit as st 
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Kline
from streamlit_echarts import st_pyecharts
from pyecharts.charts import Pie, Line



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




# Funcția pentru generarea diagramei Pie
def render_basic_pie_chart():
    products = ["Mireasma din Tei", "Proaspăt ca Marea", "Parfumat ca Polenul", "Zero Parfum"]
    sales_values = [100, 150, 200, 50]
    custom_colors = ["#f7cb39", "#4dc4be", "#ed6347", "#b0a989"]
    
    c = (
        Pie()
        .add("", [list(z) for z in zip(products, sales_values)])
        .set_colors(custom_colors)
        .set_global_opts()
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    st_pyecharts(c)



def render_sales_line_chart():
    months = ["Ian", "Feb", "Mar", "Apr", "Mai", "Iun", "Iul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    products = ["Mireasma din Tei", "Proaspăt ca Marea", "Parfumat ca Polenul", "Zero Parfum"]
    
    # Culorile personalizate pentru fiecare produs și culoarea roșie pentru vânzările totale
    custom_colors = ["#f7cb39", "#4dc4be", "#ed6347", "#b0a989", "BLUE"]
    
    # Date ajustate pentru vânzările lunare ale "Mireasma din Tei", începând din iunie
    sales_mireasma = [0, 0, 0, 0, 0, 120, 150, 100, 230, 240, 270, 265]
    sales_proaspat = [80, 100, 120, 140, 160, 180, 200, 220, 200, 180, 160, 140]
    sales_parfumat = [50, 70, 90, 110, 130, 120, 110, 100, 90, 80, 70, 60]
    sales_zero = [200, 180, 160, 140, 120, 100, 80, 60, 40, 20, 10, 5]

    # Calcularea vânzărilor totale pentru fiecare lună
    sales_total = [sum(x) for x in zip(sales_mireasma, sales_proaspat, sales_parfumat, sales_zero)]

    # Crearea graficului Line
    c = Line().add_xaxis(months)

    # Adăugarea seriilor de date pentru fiecare produs și vânzările totale cu culorile specificate
    c.add_yaxis(products[0], sales_mireasma, is_smooth=True, color=custom_colors[0])
    c.add_yaxis(products[1], sales_proaspat, is_smooth=True, color=custom_colors[1])
    c.add_yaxis(products[2], sales_parfumat, is_smooth=True, color=custom_colors[2])
    c.add_yaxis(products[3], sales_zero, is_smooth=True, color=custom_colors[3])
    c.add_yaxis("Vânzări Totale", sales_total, is_smooth=True, linestyle_opts=opts.LineStyleOpts(width=2, type_="dotted"), color=custom_colors[4])

    # Setarea opțiunilor globale
    c.set_global_opts(
        title_opts=opts.TitleOpts(),
        yaxis_opts=opts.AxisOpts(name="Vânzări"),
        xaxis_opts=opts.AxisOpts(name="Lună")
    )

    st_pyecharts(c)


# Crearea unui set de taburi
tab1, tab2, tab3 = st.tabs(["Vanzari lunare / anuale", "Siguranta Datelor", "Statistici logistica"])

# Conținut pentru Tab 1
with tab1:
    st.header(":blue[Statistici și Previziuni în Timp Real]")
    st.info(""" Soluții avansate pentru importul și analiza datelor de vânzări. 
    Cu CASTEMILL SRL, aveți la dispoziție uneltele necesare pentru a stimula creșterea afacerii, 
    optimizând în același timp procesele de vânzări și marketing.""")

    column_1, column_2 = st.columns(2)
    
    with column_1:
        st.header(":rainbow[Vânzări luna curentă]")
        render_basic_pie_chart()
    
    with column_2:
        st.header(":rainbow[Vânzări 2023]")
        render_sales_line_chart()



# Conținut pentru Tab 2
with tab2:
    st.header(":shield: Soluții Criptografice")
    st.success("Implementare servere interne cu criptografie de ultimă generație, asigurând o securitate impenetrabilă pentru datele și comunicații")

    # Definirea datelor pentru graficul Candlestick cu variații mai mari pentru a vedea lumânările
    try_attempts_data = [
        [2, 100, 99.90, 110.05], 
        [100, 100, 99.91, 100.04], 
        [95, 100, 99.92, 100.03],
        [9.95, 100, 99.90, 100.05], 
        [9.96, 100, 99.91, 120.04], 
        [97, 100, 99.92, 110.03],
        [94.95, 100, 99.90, 100.05], 
        [91, 100, 99.91, 100.04], 
        [80, 100, 99.92, 100.03],
        [13, 100, 99.90, 100.05], 
        [96, 100, 99.91, 100.04], 
        [10, 100, 99.92, 101.03],
        [99.99, 100, 99.90, 100.05], 
        [100, 100, 99.91, 100.04], 
        [91.97, 100, 99.92, 100.03],
        [99.95, 100, 99.90, 100.05], 
        [98.96, 100, 99.91, 120.04], 
        [93.97, 100, 99.92, 110.03],
        [94.95, 100, 99.90, 100.05], 
        [9.96, 10, 99.91, 100.04], 
        [8, 10, 9.92, 100.03],
        [9, 100, 9.90, 100.05], 
        [2, 10, 99.91, 100.04], 
        [99, 100, 99.92, 101.03],
        [2, 100, 99.90, 110.05], 
        [100, 100, 99.91, 100.04], 
        [95, 100, 99.92, 100.03],
        [9.95, 100, 99.90, 100.05], 
        [9.96, 100, 99.91, 120.04], 
        [97, 100, 99.92, 110.03],
        [94.95, 100, 99.90, 100.05],
    
    ]
    days = [f"Ziua {i+1}" for i in range(30)]  # Presupunem 30 de zile în lună

    c = Kline()
    c.add_xaxis(days)
    c.add_yaxis("Server Status", try_attempts_data)
    c.set_global_opts(
        title_opts=opts.TitleOpts(),
        yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
        xaxis_opts=opts.AxisOpts(is_scale=True),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        visualmap_opts=opts.VisualMapOpts(
            max_=100.05,
            min_=99.90,
            range_color=["#ff0000", "#00ff00"],
        )
    )

    st_pyecharts(c)

with tab3:
   

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
