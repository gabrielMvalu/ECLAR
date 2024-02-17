import streamlit as st 
from streamlit_timeline import timeline
from pyecharts import options as opts
from pyecharts.charts import Pie, Line
from streamlit_echarts import st_pyecharts



st.set_page_config(layout="wide")
st.title(':blue[ECLAR SRL -live sales-]')
st.divider()



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
    
    # Culorile personalizate pentru fiecare produs
    custom_colors = ["#f7cb39", "#4dc4be", "#ed6347", "#b0a989", "#34568B"]  # Am adăugat o culoare suplimentară pentru "Vânzări Totale"
    
    # Date fictive pentru vânzările lunare ale fiecărui produs
    sales_data = {
        "Mireasma din Tei": [120, 150, 180, 200, 220, 210, 200, 190, 180, 170, 160, 150],
        "Proaspăt ca Marea": [80, 100, 120, 140, 160, 180, 200, 220, 200, 180, 160, 140],
        "Parfumat ca Polenul": [50, 70, 90, 110, 130, 120, 110, 100, 90, 80, 70, 60],
        "Zero Parfum": [200, 180, 160, 140, 120, 100, 80, 60, 40, 20, 10, 5]
    }

    # Calcularea vânzărilor totale pentru fiecare lună
    sales_total = [sum(x) for x in zip(*sales_data.values())]

    # Crearea graficului Line
    c = Line().add_xaxis(months)

    # Adăugarea seriilor de date și a culorilor personalizate
    for i, (product, sales) in enumerate(sales_data.items()):
        c.add_yaxis(product, sales, is_smooth=True, 
                    linestyle_opts=opts.LineStyleOpts(color=custom_colors[i]))

    # Adăugarea seriei pentru vânzările totale
    c.add_yaxis("Vânzări Totale", sales_total, is_smooth=True, 
                linestyle_opts=opts.LineStyleOpts(color=custom_colors[-1], width=2, type_="dotted"))

    # Setarea opțiunilor globale
    c.set_global_opts(title_opts=opts.TitleOpts(),
                      yaxis_opts=opts.AxisOpts(name="Vânzări"),
                      xaxis_opts=opts.AxisOpts(name="Lună"))

    st_pyecharts(c)



# Crearea coloanelor și afișarea graficelor
column_1, column_2 = st.columns(2)

with column_1:
    st.header(":rainbow[Vânzări Produse - pentru luna curenta]")
    render_basic_pie_chart()

with column_2:
    st.header(":rainbow[Vânzări Lunare pe Anul 2023]")
    render_sales_line_chart()


with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)
