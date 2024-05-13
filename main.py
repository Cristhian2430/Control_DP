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
df['Monto Acumulado'] = df['monto'].cumsum()
monto_acumulado = df['Monto Acumulado'].iloc[-1]
porcentaje_acumulado = (monto_acumulado / monto_meta) * 100

col1, col2 = st.columns(2)

with col1:
    st.metric(label="Monto Acumulado", value=f"S/.{monto_acumulado:,.2f}")
    st.metric(label="Monto Meta", value=f"S/.{monto_meta:,.2f}")
    st.metric(label="% del Meta Alcanzado", value=f"{porcentaje_acumulado:.2f}%")
    st.metric(label="Abono Mensual", value=f"{df['Monto Acumulado'].mean():.2f}%")
with col2:
    fig = px.bar(df, x='fecha', y='Monto Acumulado', title='Monto Acumulado')
    st.plotly_chart(fig, use_container_width=True)



st.write('Registro de Pagos:')





fig = px.line(df, x='fecha', y='Monto Acumulado', title='Evolución del Monto Acumulado')
fig.add_hline(y = monto_meta, line_dash="dash", line_color="red", annotation_text="Meta de monto", 
              annotation_position="top right")


st.dataframe(df.head())
