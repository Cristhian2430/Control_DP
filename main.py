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
df.sort_values('fecha', inplace=True)
df['fecha'] = df['fecha'].dt.strftime('%m/%Y')

st.write('Registro de Pagos:')

df['Monto Acumulado'] = df['monto'].cumsum()

st.bar_chart(df, x="fecha", y="Monto Acumulado")



st.write(df.head())
