import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


# from app.pages import sales

app = dash.Dash(__name__,  external_stylesheets=[
                dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])
# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

app.layout = html.Div([
    html.Div([
        dbc.Container([
            dbc.Card([
                "FAKE ACCOUNT POLICE"
            ], className = "app-card")
        ], className= "app-container")
    ],className= "main-space" )
]
)

if __name__ == '__main__':
    app.run_server(debug=True)

