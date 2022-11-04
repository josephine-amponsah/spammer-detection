import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


# from app.pages import sales
FA = "https://fonts.googleapis.com/css?family=Lobster"
app = dash.Dash(__name__,  external_stylesheets=[ FA,
                dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])
# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

app.layout = html.Div([
    html.Div([
        dbc.Container([
            html.Div([
                html.H1("FAKE ACCOUNT POLICE", className = "app-title-text"),
                html.H5("ASSESS CREDIBILITY OF IG ACCOUNTS", className = "app-title-sub"),
                dbc.Row([
                    dbc.Col([ 
                        html.Div("ACCOUNT INFO"),
                        dbc.Row(),
                        dbc.Row(),
                        dbc.Row(),
                        dbc.Row(),
                        ]),
                    dbc.Col("Result")
                ], className = "active-space")
            ], className = "app-card")
        ], className= "app-container")
    ],className= "main-space" )
]
)

if __name__ == '__main__':
    app.run_server(debug=True)

