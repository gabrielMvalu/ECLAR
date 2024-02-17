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

def render_sales_line_chart():
    # Lunile anului 2023
    months = ["Ian", "Feb", "Mar", "Apr", "Mai", "Iun", "Iul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    # Date fictive pentru vânzările lunare ale fiecărui produs
    sales_mireasma = [120, 150, 180, 200, 220, 210, 200, 190, 180, 170, 160, 150]
    sales_proaspat = [80, 100, 120, 140, 160, 180, 200, 220, 200, 180, 160, 140]
    sales_parfumat = [50, 70, 90, 110, 130, 120, 110, 100, 90, 80, 70, 60]
    sales_zero = [200, 180, 160, 140, 120, 100, 80, 60, 40, 20, 10, 5]
    
    # Calcularea vânzărilor totale pentru fiecare lună
    sales_total = [sum(x) for x in zip(sales_mireasma, sales_proaspat, sales_parfumat, sales_zero)]
    
    # Crearea graficului Line
    c = (
        Line()
        .add_xaxis(months)
        .add_yaxis("Mireasma din Tei", sales_mireasma, is_smooth=True)
        .add_yaxis("Proaspăt ca Marea", sales_proaspat, is_smooth=True)
        .add_yaxis("Parfumat ca Polenul", sales_parfumat, is_smooth=True)
        .add_yaxis("Zero Parfum", sales_zero, is_smooth=True)
        .add_yaxis("Vânzări Totale", sales_total, is_smooth=True, linestyle_opts=opts.LineStyleOpts(width=2, type_="dotted"))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Vânzări Produse pe Luna - 2023"),
            yaxis_opts=opts.AxisOpts(name="Vânzări"),
            xaxis_opts=opts.AxisOpts(name="Lună")
        )
    )
    st_pyecharts(c)


# Crearea coloanelor și afișarea graficelor
column_1, column_2 = st.columns(2)

with column_1:
    render_basic_pie_chart()

with column_2:
    render_sales_line_chart()

