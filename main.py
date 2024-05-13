import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")
st.title('Grupo 1 - PUCP Python')
st.write('¡Hola!')

with open(r"/mount/src/Control_DP/control.json", 'r') as file:
    data = json.load(file)

df = pd.DataFrame(list(data.items()), columns=['fecha', 'monto'])

st.write(df.head())
