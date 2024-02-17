from streamlit_elements import elements, mui, html
import streamlit as st

with elements("multiple_children"):

   with mui.Paper:
        with mui.Typography:
            html.p("Hello world")
            html.p("Goodbye world")
