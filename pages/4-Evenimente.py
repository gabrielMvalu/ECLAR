from streamlit_elements import elements, mui, html
import streamlit as st



with elements("callbacks_retrieve_data"):

    if "my_text" not in st.session_state:
        st.session_state.my_text = ""

    def handle_change(event):
        st.session_state.my_text = event.target.value

    mui.Typography(st.session_state.my_text)

    mui.TextField(label="Input some text here", onChange=handle_change)

with elements("style_elements_css"):

    html.div(
        {st.session_state.my_text},
        css={
            "backgroundColor": "hotpink",
            "&:hover": {
                "color": "lightgreen"
            }
        }
    )

with elements("style_mui_sx"):

    mui.Box(
         {st.session_state.my_text},
        sx={
            "bgcolor": "background.paper",
            "boxShadow": 2,
            "borderRadius": 5,
            "p": 2,
            "minWidth": 200,
        }
    )
