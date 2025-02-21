import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos limpios
# Recuerda cambiar la ruta del archivo
vehicles = pd.read_csv(r"C:\Users\Usuario\Desktop\DATA SCIENTIST\DATA_SCIENTIS_TRIPLETEN\Sprint 7\Proyecto-SP7\notebooks\vehicles_cleaned.csv")

# Crear un encabezado
st.header("Dashboard de Vehículos en Venta")

# Casillas de verificación
show_histogram = st.checkbox("Mostrar histograma de kilometraje")
show_scatter = st.checkbox("Mostrar gráfico de dispersión (Precio vs Kilometraje)")

# Mostrar histograma si el usuario lo selecciona
if show_histogram:
    st.write("Histograma del Kilometraje")
    fig_hist = px.histogram(vehicles, x="odometer", title="Distribución del Kilometraje de los Vehículos")
    st.plotly_chart(fig_hist, use_container_width=True)

# Mostrar gráfico de dispersión si el usuario lo selecciona
if show_scatter:
    st.write("Gráfico de Dispersión: Precio vs Kilometraje")
    fig_scatter = px.scatter(
        vehicles, x="odometer", y="price", color="fuel",
        title="Relación entre Kilometraje y Precio"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)


