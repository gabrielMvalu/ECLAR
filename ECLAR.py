import streamlit as st 
from streamlit_timeline import timeline
from pyecharts import options as opts
from pyecharts.charts import Pie, Line
from streamlit_echarts import st_pyecharts



st.set_page_config(layout="wide")
st.header(':rainbow[Eclar STORY]')
st.divider()


with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)

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

# Funcția pentru generarea diagramei Line
def render_sales_line_chart():
    products = ["Mireasma din Tei", "Proaspăt ca Marea", "Parfumat ca Polenul", "Zero Parfum"]
    sales_values = [100, 150, 200, 50]
    
    c = (
        Line()
        .add_xaxis(products)
        .add_yaxis("Vânzări", sales_values, is_smooth=True)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Vânzări Produse per Luna Curentă"),
            yaxis_opts=opts.AxisOpts(name="Vânzări"),
            xaxis_opts=opts.AxisOpts(name="Produs")
        )
    )
    st_pyecharts(c)

# Crearea coloanelor și afișarea graficelor
column_1, column_2 = st.columns(2)

with column_1:
    render_basic_pie_chart()

with column_2:
    render_sales_line_chart()

