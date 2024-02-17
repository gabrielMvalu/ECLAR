import streamlit as st 
from pyecharts import options as opts
from pyecharts.charts import Kline
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
tab1, tab2, tab3 = st.tabs(["Vanzari lunare / anuale", "Siguranta Datelor", "Tab 3"])

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
    st.success("Implementare servere interne cu criptografie de ultimă generație, asigurând o securitate impenetrabilă pentru datele și comunicațiile ECLAR SRL")

    try_attempts_data = [
        [100, 99.98, 99.98, 100],  # Ziua 1
        [100, 99.98, 99.98, 100],  # Ziua 2
        [100, 99.98, 99.98, 100],  # Ziua 3
    ]

    c = Kline()
    c.add_xaxis(["Ziua 1", "Ziua 2", "Ziua 3"])
    c.add_yaxis("Server Status", try_attempts_data, itemstyle_opts=opts.ItemStyleOpts(color="#00ff00", color0="#00ff00", border_color="#00ff00", border_color0="#00ff00"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="Încercări de Spargere și Stabilitatea Serverului"),
        yaxis_opts=opts.AxisOpts(scale=True, splitline_opts=opts.SplitLineOpts(is_show=True)),
        xaxis_opts=opts.AxisOpts(is_scale=True),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
    )

    st_pyecharts(c)


with tab3:
    st.header("Acesta este Tab 3")
    st.write("Aici poți adăuga conținut pentru al treilea tab.")

    st.table(chart_data)

