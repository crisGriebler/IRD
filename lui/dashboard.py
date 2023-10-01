import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Sample economic data
economic_data = pd.DataFrame({
    'Country': ['USA', 'Canada', 'Mexico'],
    'GDP': [21.43, 1.64, 1.27],
    'Unemployment_Rate': [5.2, 7.5, 4.8]
})

# Sample geographical data
geographical_data = pd.DataFrame({
    'Country': ['USA', 'Canada', 'Mexico'],
    'Latitude': [37.09, 56.13, 23.63],
    'Longitude': [-95.71, -106.35, -102.55]
})

# Create a map using Plotly
map_figure = go.Figure(go.Scattergeo(
    lon=geographical_data['Longitude'],
    lat=geographical_data['Latitude'],
    mode='markers',
    marker=dict(size=economic_data['GDP'] * 2),
    text=economic_data['Country'],
))

map_figure.update_geos(
    showcoastlines=True,
    coastlinecolor="Black",
    showland=True,
    landcolor="white",
    showocean=True,
    oceancolor="LightBlue",
)

map_figure.update_layout(
    title='Economic Data by Country',
    geo=dict(
        scope='world',
        showland=True,
    ),
)

# Define the layout of the dashboard
app.layout = dbc.Container([
    html.H1('Economic and Geographical Dashboard'),
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=map_figure)
        ], width=6),
        dbc.Col([
            dcc.Graph(
                id='economic-data',
                figure=px.bar(economic_data, x='Country', y='GDP', title='GDP by Country')
            ),
            dcc.Graph(
                id='unemployment-data',
                figure=px.bar(economic_data, x='Country', y='Unemployment_Rate', title='Unemployment Rate by Country')
            ),
        ], width=6),
    ]),
])

if __name__ == '__main__':
    app.run_server(port=8000,
               debug=True)