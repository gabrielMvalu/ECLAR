import streamlit as st 
from streamlit_timeline import timeline
from pyecharts import options as opts
from pyecharts.charts import Pie
from streamlit_echarts import st_pyecharts




st.set_page_config(layout="wide")
st.header(':rainbow[Eclar STORY]')
st.divider()


with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)






def render_basic_pie_chart():
    # Numele produselor
    products = ["Mireasma din Tei", "Proaspăt ca Marea", "Parfumat ca Polenul", "Zero Parfum"]
    
    # Valorile vânzărilor pentru fiecare produs
    sales_values = [100, 150, 200, 50]

    # Culorile personalizate pentru fiecare produs
    custom_colors = ["#f7cb39", "#4dc4be", "#ed6347", "#b0a989"]

    c = (
        Pie()
        .add("", [list(z) for z in zip(products, sales_values)])
        .set_colors(custom_colors)  # Setarea culorilor personalizate
        .set_global_opts()
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    st_pyecharts(c)

# Apelarea funcției pentru a afișa graficul
render_basic_pie_chart()
