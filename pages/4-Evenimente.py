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

with elements("monaco_editors"):

    # Streamlit Elements embeds Monaco code and diff editor that powers Visual Studio Code.
    # You can configure editor's behavior and features with the 'options' parameter.
    #
    # Streamlit Elements uses an unofficial React implementation (GitHub links below for
    # documentation).

    from streamlit_elements import editor

    if "content" not in st.session_state:
        st.session_state.content = "Default value"

    mui.Typography("Content: ", st.session_state.content)

    def update_content(value):
        st.session_state.content = value

    editor.Monaco(
        height=300,
        defaultValue=st.session_state.content,
        onChange=lazy(update_content)
    )

    mui.Button("Update content", onClick=sync())

    editor.MonacoDiff(
        original="Happy Streamlit-ing!",
        modified="Happy Streamlit-in' with Elements!",
        height=300,
    )
