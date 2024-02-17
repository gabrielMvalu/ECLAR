from streamlit_elements import elements, mui, html
import streamlit as st

with elements("style_mui_sx"):

    mui.Box(
        "Some text in a styled box",
        sx={
            "bgcolor": "background.paper",
            "boxShadow": 2,
            "borderRadius": 5,
            "p": 2,
            "minWidth": 200,
        }
    )
with elements("style_elements_css"):

    html.div(
        "This has a hotpink background",
        css={
            "backgroundColor": "hotpink",
            "&:hover": {
                "color": "lightgreen"
            }
        }
    )
