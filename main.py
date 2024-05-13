import streamlit as st
import pandas as pd
import numpy as np
import json

st.set_page_config(layout="wide")
st.title('Control de Pagos')

with open(r"/mount/src/control_dp/control.json", 'r') as file:
    data = json.load(file)

df = pd.DataFrame(list(data.items()), columns=['fecha', 'monto'])
df['Fecha'] = pd.to_datetime(df['Fecha'])
df['Fecha'] = df['Fecha'].dt.strftime('%m/%Y')

st.write('Registro de Pagos:')
st.write(df.head())
