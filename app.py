import pandas as pd
import streamlit as st
import plotly.express as px

# títulos 
st.title('II SIMPÓSIO CIENTÍFICO DO DCET - UNIFAP')
st.subheader('Visualização de dados de queimadas - Fonte: INPE')

# Definição de uma sidebar
dados = st.sidebar.selectbox('Selecione a data', ['2025-11-25', 
                                                  '2025-11-26',
                                                  '2025-11-27',
                                                  '2025-11-28',
                                                  '2025-11-29',
                                                  '2025-11-30'])

csv_file = f'dados\\focos_diario_br_{dados.replace('-', '')}.csv'

df = pd.read_csv(csv_file)

df_amapa = df[df['estado'] == 'AMAPÁ']

