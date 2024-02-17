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


with elements("callbacks_lazy"):

    # With the two first examples, each time you input a letter into the text field,
    # the callback is invoked but the whole app is reloaded as well.
    #
    # To avoid reloading the whole app on every input, you can wrap your callback with
    # lazy(). This will defer the callback invocation until another non-lazy callback
    # is invoked. This can be useful to implement forms.

    from streamlit_elements import lazy

    if "first_name" not in st.session_state:
        st.session_state.first_name = None
        st.session_state.last_name = None

    if st.session_state.first_name is not None:
        first_name = st.session_state.first_name.target.value
    else:
        first_name = "John"

    if st.session_state.last_name is not None:
        last_name = st.session_state.last_name.target.value
    else:
        last_name = "Doe"

    def set_last_name(event):
        st.session_state.last_name = event

    # Display first name and last name
    mui.Typography("Your first name: ", first_name)
    mui.Typography("Your last name: ", last_name)

    # Lazily synchronize onChange with first_name and last_name state.
    # Inputting some text won't synchronize the value yet.
    mui.TextField(label="First name", onChange=lazy(sync("first_name")))

    # You can also pass regular python functions to lazy().
    mui.TextField(label="Last name", onChange=lazy(set_last_name))

    # Here we give a non-lazy callback to onClick using sync().
    # We are not interested in getting onClick event data object,
    # so we call sync() with no argument.
    #
    # You can use either sync() or a regular python function.
    # As long as the callback is not wrapped with lazy(), its invocation will
    # also trigger every other defered callbacks.
    mui.Button("Update first namd and last name", onClick=sync())
