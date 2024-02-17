import streamlit as st 
from streamlit_timeline import timeline
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
from streamlit_echarts import st_pyecharts




st.set_page_config(layout="wide")
st.header(':rainbow[Eclar STORY]')
st.divider()


with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)




def render_basic_pie_chart():
    c = (
        Pie()
        .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
        .set_global_opts(title_opts=opts.TitleOpts(title="Exemplu de diagramă Pie"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    st_pyecharts(c)

render_basic_pie_chart()
