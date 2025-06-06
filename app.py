import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Título de la app
st.title("Ejemplo de Página con Streamlit")

# Entrada de texto
nombre = st.text_input("Escribe tu nombre:")

# Botón
if st.button("Saludar"):
    st.success(f"¡Hola, {nombre}!")

# Generación de datos aleatorios
st.header("Gráfico de líneas con datos aleatorios")
data = pd.DataFrame({
    'x': np.arange(0, 100),
    'y': np.random.randn(100).cumsum()
})

# Mostrar gráfico
fig, ax = plt.subplots()
ax.plot(data['x'], data['y'])
ax.set_title("Gráfico aleatorio")
st.pyplot(fig)

# Selector interactivo
st.sidebar.header("Opciones")
opcion = st.sidebar.selectbox("Elige una opción:", ["Inicio", "Datos", "Acerca de"])

if opcion == "Inicio":
    st.write("Estás en la página de inicio.")
elif opcion == "Datos":
    st.write("Aquí están los datos:")
    st.dataframe(data)
elif opcion == "Acerca de":
    st.info("Hecho por Ángel con ❤️ usando Streamlit.")
