import streamlit as st
import pandas as pd
import numpy as np
import json
import plotly.express as px

st.set_page_config(layout="wide")
st.title('Control de Pagos')
monto_meta = 5500
with open(r"/mount/src/control_dp/control.json", 'r') as file:
    data = json.load(file)

df = pd.DataFrame(list(data.items()), columns=['fecha', 'monto'])
df['fecha'] = pd.to_datetime(df['fecha'])
df.sort_values('fecha', inplace=True)
df['fecha'] = df['fecha'].dt.strftime('%Y/%m')

st.write('Registro de Pagos:')

df['Monto Acumulado'] = df['monto'].cumsum()

st.bar_chart(df, x="fecha", y="Monto Acumulado")
st.line_chart(df, x="fecha", y="Monto Acumulado")

fig = px.line(df, x='fecha', y='Monto Acumulado', title='Evolución del Monto Acumulado')
fig.add_hline(y = monto_meta, line_dash="dash", line_color="red", annotation_text="Meta de monto", 
              annotation_position="top right")
st.plotly_chart(fig, use_container_width=True)

st.write(df.head())
