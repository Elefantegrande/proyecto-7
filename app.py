import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Análisis de Vehículos en Venta (USA)')

# Botón para crear histograma de precios
hist_button = st.button('Construir histograma de precios')

if hist_button:
    st.write('Histograma de la columna "price"')

    fig = go.Figure(data=[go.Histogram(x=car_data['price'])])
    fig.update_layout(title_text='Distribución de Precios')

    st.plotly_chart(fig, use_container_width=True)

# Botón para crear gráfico de dispersión price vs model_year
scatter_button = st.button('Construir gráfico de dispersión: Price vs Model Year')

if scatter_button:
    st.write('Gráfico de dispersión entre precio y año del modelo')

    fig2 = go.Figure(data=[go.Scatter(
        x=car_data['model_year'],
        y=car_data['price'],
        mode='markers'
    )])

    fig2.update_layout(
        title_text='Precio vs Año del Modelo',
        xaxis_title='Año del Modelo',
        yaxis_title='Precio'
    )

    st.plotly_chart(fig2, use_container_width=True)


