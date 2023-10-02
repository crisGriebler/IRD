import pydeck as pdk
import pandas as pd
import numpy as np

# Importação do arquivo csv e transformação para DataFrame
df = pd.read_csv("C:listings.csv")


# Criação da camada
layer = pdk.Layer(
    'HexagonLayer',  # Definir camada com o mapa HexagonLayer
    df, # DataFrame que contém seus dados
    get_position=['longitude', 'latitude'], # Colunas que possuem long. e lat. 
    auto_highlight=True, # Realçar hexágonos quando cursor passar por cima
    elevation_scale=50, # Altura dos hexágonos
    pickable=True, # Permitir que os hexágonos sejam selecionáveis
    elevation_range=[0, 3000], # Definir a faixa de altura dos hexágonos
    extruded=True, # Dimensão da altura dos hexágonos
    coverage=1) # Cobertura da camada

# Definição da visão
view_state = pdk.ViewState(
    longitude= -43.7763403, # Verificar longitude no Google Maps da região que vc está buscando
    latitude= -22.9131566, # Verificar latitude no Google Maps  
    zoom=6, # Definir zoom inicial do mapa
    min_zoom=5, # Especificar o nível de zoom mínimo permitido
    max_zoom=15, # Especificar o nível de zoom máximo permitido
    pitch=40.5, # Controlar inclinação do mapa
    bearing=-27.36) # Definir rotação do mapa

# Combinação em um objeto 'Deck'
r = pdk.Deck(layers=[layer], initial_view_state=view_state)

# Salvando como html
r.to_html('hexagon-example.html')