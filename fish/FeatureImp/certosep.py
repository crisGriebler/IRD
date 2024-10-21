import plotly.express as px
import pandas as pd

df = pd.read_excel("Variavel_out.xlsx")

df.columns = df.columns.str.strip()

# Convert necessary columns to numeric values, with coercion for errors
df['comprimento_Total'] = pd.to_numeric(df['comprimento_Total'], errors='coerce')
df['peso'] = pd.to_numeric(df['peso'], errors='coerce')
df['altura'] = pd.to_numeric(df['altura'], errors='coerce')

df['peso_categoria'] = pd.cut(df['peso'], bins=range(0, int(df['peso'].max()) + 100, 100), right=False)
df['peso_categoria'] = df['peso_categoria'].astype(str)  # Convert intervals to string for plotting

# Create the 3D scatter plot
fig = px.scatter_3d(df, x='comprimento_Total', y='peso', z='altura', color='peso_categoria',
                    title='Scatter Plot 3D de Peso vs Comprimento Total vs Altura',
                    labels={'peso_categoria': 'Intervalo de Peso'},
                    color_continuous_scale=px.colors.cyclical.IceFire)

fig.show()

## passar para ipynb 