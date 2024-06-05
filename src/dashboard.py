import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

from src.data_processing import load_data, preprocess_data

# Load and process data
data_path = '../data/dataset.csv'
df = preprocess_data(load_data(data_path))

# Create Dash app
app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div([
    html.H1('Panel de Análisis de Datos'),
    dcc.Dropdown(
        id='column-dropdown',
        options=[{'label': col, 'value': col} for col in df.columns],
        value='Valor'
    ),
    dcc.Graph(id='histogram'),
    dcc.Graph(id='scatter')
])


# Define functions to update charts
@app.callback(
    Output('histogram', 'figure'),
    Output('scatter', 'figure'),
    Input('column-dropdown', 'value')
)
def update_graphs(selected_column):
    hist_fig = px.histogram(df, x=selected_column, title=f'Distribución de {selected_column}')
    scatter_fig = px.scatter(df, x=selected_column, y='Valor', title=f'{selected_column} vs Valor')
    return hist_fig, scatter_fig

if __name__ == '__main__':
    app.run_server(debug=True)
