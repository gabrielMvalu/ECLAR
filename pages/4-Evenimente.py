from streamlit_elements import elements, mui, html
import streamlit as st



with elements("callbacks_retrieve_data"):

    if "my_text" not in st.session_state:
        st.session_state.my_text = ""

    def handle_change(event):
        st.session_state.my_text = event.target.value

    mui.Typography(st.session_state.my_text)

    mui.TextField(label="Input some text here", onChange=handle_change)

with elements("media_player"):

    # Play video from many third-party sources: YouTube, Facebook, Twitch,
    # SoundCloud, Streamable, Vimeo, Wistia, Mixcloud, DailyMotion and Kaltura.
    #
    # This element is powered by ReactPlayer (GitHub link below).

    from streamlit_elements import media

    media.Player(url="https://www.youtube.com/watch?v=iik25wqIuFo", controls=False)

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

with elements("nivo_charts"):

    # Streamlit Elements includes 45 dataviz components powered by Nivo.

    from streamlit_elements import nivo

    DATA = [
        { "taste": "fruity", "chardonay": 93, "carmenere": 61, "syrah": 114 },
        { "taste": "bitter", "chardonay": 91, "carmenere": 37, "syrah": 72 },
        { "taste": "heavy", "chardonay": 56, "carmenere": 95, "syrah": 99 },
        { "taste": "strong", "chardonay": 64, "carmenere": 90, "syrah": 30 },
        { "taste": "sunny", "chardonay": 119, "carmenere": 94, "syrah": 103 },
    ]

    with mui.Box(sx={"height": 500}):
        nivo.ResponsiveCalendar
            data={data}
            from="2015-03-01"
            to="2016-07-12"
            emptyColor="#eeeeee"
            colors={[ '#61cdbb', '#97e3d5', '#e8c1a0', '#f47560' ]}
            margin={{ top: 40, right: 40, bottom: 40, left: 40 }}
            yearSpacing={40}
            monthBorderColor="#ffffff"
            dayBorderWidth={2}
            dayBorderColor="#ffffff"
            legends={[
                {
                    anchor: 'bottom-right',
                    direction: 'row',
                    translateY: 36,
                    itemCount: 4,
                    itemWidth: 42,
                    itemHeight: 36,
                    itemsSpacing: 14,
                    itemDirection: 'right-to-left'
                }
            ]}
        />
    )
