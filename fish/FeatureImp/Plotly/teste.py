import plotly.express as px
import pandas as pd

df = pd.read_excel("Variavel.xlsx")

df.columns = df.columns.str.strip()

df['comprimento_Total'] = pd.to_numeric(df['comprimento_Total'], errors='coerce')


fig = px.scatter(df, x='comprimento_Total', y='peso', color='peso_categoria',
                 title='Scatter Plot de Peso vs Comprimento Total',
                 labels={'peso_categoria': 'Intervalo de Peso'},
                 color_continuous_scale=px.colors.cyclical.IceFire)


fig.show()