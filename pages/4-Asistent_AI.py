import streamlit as st
import pandas as pd
import numpy as np
from statsmodels.tsa.api import ExponentialSmoothing
import plotly.graph_objects as go
from openai import OpenAI


st.set_page_config(layout="wide")
st.header('Pagina Principală')
st.write('Bine ați venit la aplicația pentru completarea Planului de Afaceri!')

tab1, tab2 = st.tabs(["Predictii viitoare", "Asistent AI"])

with tab1:
    sales_mireasma = [0, 0, 0, 0, 0, 120, 150, 100, 230, 240, 270, 265]
    sales_proaspat = [80, 100, 120, 140, 160, 180, 200, 220, 200, 180, 160, 140]
    sales_parfumat = [50, 70, 90, 110, 130, 120, 110, 100, 90, 80, 70, 60]
    sales_zero = [20, 100, 60, 40, 120, 100, 110, 60, 40, 80, 10, 70]
    
    st.title('Analiza și Predicția Vânzărilor pentru Produse')
    
    produs_selectat = st.selectbox('Alege un produs:', ('Mireasmă', 'Proaspăt', 'Parfumat', 'Zero'))
    
    sales_data = {
        'Mireasmă': sales_mireasma,
        'Proaspăt': sales_proaspat,
        'Parfumat': sales_parfumat,
        'Zero': sales_zero
    }
    
    sales_selected = sales_data[produs_selectat]
    
    model = ExponentialSmoothing(sales_selected, trend='add', seasonal='add', seasonal_periods=6).fit()
    pred_sales = model.forecast(3)
    
    # Crearea graficului folosind Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=np.arange(len(sales_selected)), y=sales_selected, mode='lines+markers', name='Vânzări Istorice'))
    fig.add_trace(go.Scatter(x=np.arange(len(sales_selected), len(sales_selected) + 3), y=pred_sales, mode='lines+markers', name='Predicții Vânzări', line=dict(dash='dash')))
    
    fig.update_layout(title=f'Analiza și Predicția Vânzărilor pentru {produs_selectat}', xaxis_title='Perioada', yaxis_title='Vânzări', autosize=False, width=800, height=600)
    
    st.plotly_chart(fig)

    st.info("""
    Aceste predicții folosesc modelul de netezire exponențială, care ia în considerare tendințele și 
    sezonalitatea din datele istorice ale vânzărilor pentru a estima vânzările viitoare. Aceste estimări
    pot ajuta compania în planificarea stocurilor și în strategiile de marketing pentru a răspunde mai bine cererii viitoare.
    """)


with tab2:

    with st.expander(" ℹ️ Mesaj Informativ ℹ️  "):
        st.write("""
            Vă informăm că aceast bot se află într-o fază incipientă de dezvoltare. 
            În acest moment, funcționalitatea este limitată la furnizarea de răspunsuri generale.
        """)
    
    with st.sidebar:
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
        
    if not openai_api_key:
        st.info("Vă rugăm să introduceți cheia API OpenAI în bara laterală.")
    else:
        # Inițializarea clientului OpenAI cu cheia API introdusă
        client = OpenAI(api_key=openai_api_key)
    
        # Inițializarea stării sesiunii pentru model și mesaje
        if "openai_model" not in st.session_state:
            st.session_state["openai_model"] = "gpt-4-1106-preview"
    
        if "messages" not in st.session_state:
            st.session_state.messages = []
    
        # Afișarea mesajelor anterioare
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    
        # Input pentru mesaj nou de la utilizator
        if prompt := st.chat_input("Adaugati mesajul aici."):
            st.session_state.messages.append({"role": "user", "content": f"{prompt}" })
            with st.chat_message("user"):
                st.markdown(prompt)
    
            # Generarea răspunsului asistentului și afișarea acestuia
            with st.chat_message("assistant"):
                stream = client.chat.completions.create(
                    model=st.session_state["openai_model"],
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                    stream=True,
                )
                response = st.write_stream(stream)
            st.session_state.messages.append({"role": "assistant", "content": response})

