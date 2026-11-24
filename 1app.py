import streamlit as st
import pandas as pd
import plotly.express as px
import json
import urllib.request

# Título de la aplicación
st.title("🇲🇽 Mapa del PIB por Estado en México")
st.write("Este mapa muestra cuánto dinero (PIB) genera cada estado. Los colores más oscuros indican mayor riqueza.")

# --- PASO 1: Crear datos de ejemplo (PIB ficticio en millones de dólares) ---
data = {
    'Estado': [
        'Ciudad de México', 'Nuevo León', 'Jalisco', 'Estado de México', 
        'Puebla', 'Yucatán', 'Querétaro', 'Chihuahua', 'Sonora', 'Veracruz'
    ],
    'PIB_millones': [150000, 95000, 85000, 110000, 45000, 30000, 40000, 35000, 38000, 50000]
}
df = pd.DataFrame(data)

# --- PASO 2: Descargar el mapa de México (GeoJSON) ---
# Esto le dice a Python dónde están las fronteras de los estados
url_geojson = "https://raw.githubusercontent.com/angelnmara/geojson/master/mexicoHigh.json"
with urllib.request.urlopen(url_geojson) as response:
    mexico_geojson = json.loads(response.read())

# --- PASO 3: Crear el mapa dinámico con Plotly ---
fig = px.choropleth(
    df,
    geojson=mexico_geojson,
    locations='Estado',          # La columna de tu tabla que tiene los nombres
    featureidkey="properties.name", # Cómo se llaman los estados en el mapa
    color='PIB_millones',        # La columna que define el color
    color_continuous_scale="Blues", # Paleta de colores (azul claro a oscuro)
    range_color=(0, df['PIB_millones'].max()),
    scope="north america",       # Para que el mapa se enfoque en América
    labels={'PIB_millones': 'PIB (Millones USD)'}
)

# Ajustar el mapa para que se vea bonito y centrado en México
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Mostrar el mapa en Streamlit
st.plotly_chart(fig, use_container_width=True)

# --- PASO 4: Mostrar la tabla de datos debajo del mapa ---
st.subheader("📊 Datos del PIB")
st.dataframe(df, use_container_width=True)
