import streamlit as st
import pandas as pd
import numpy as np
import json

st.set_page_config(layout="wide")
st.title('Control de Pagos')

with open(r"/mount/src/control_dp/control.json", 'r') as file:
    data = json.load(file)

df = pd.DataFrame(list(data.items()), columns=['fecha', 'monto'])
df['fecha'] = pd.to_datetime(df['fecha'])
df['fecha'] = df['fecha'].dt.strftime('%m/%Y')

st.write('Registro de Pagos:')

st.bar_chart(df, x="fecha", y="monto")


st.write(df.head())
