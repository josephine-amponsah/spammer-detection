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
                html.H1(["FAKE ACCOUNT POLICE"], className = "app-title-text"),
                html.H5(["ASSESS CREDIBILITY OF IG ACCOUNTS"], className = "app-title-sub"),
                dbc.Row([
                    dbc.Col([
                        html.Div(["ACCOUNT INFO"]),
                        dbc.Row([
                            dbc.Col([
                                html.Div(["Username"]),
                                dcc.Input(value = "")
                                ]),
                            dbc.Col([
                                html.Div(["Full name"]),
                                dcc.Input(value = "")
                                ]),
                    ]),
                        html.Br(),
                        dbc.Row([
                            html.Div(["Bio"]),
                            dcc.Input(value = "")
                    ], justify = "center" ),
                        html.Br(),
                        dbc.Row([
                            dbc.Col([
                                html.Div(["Has Profile Picture?"]),
                                dcc.Input(value = "")
                            ]),
                            dbc.Col([
                                html.Div(["Link in bio?"]),
                                dcc.Input(value = "")
                            ]),
                            dbc.Col([
                                html.Div(["Account private?"]),
                                dcc.Input(value = "")
                            ]),
                    ]),
                        html.Br(),
                        dbc.Row([
                            dbc.Col([
                                html.Div(["Followers"]),
                                dcc.Input(value = "")
                            ]),
                            dbc.Col([
                                html.Div(["Following"]),
                                dcc.Input(value = "")
                            ]),
                            dbc.Col([
                                html.Div(["No. of posts"]),
                                dcc.Input(value = "")
                            ]),
                    ]),
                        ], width=8, className = "input-section"),
                    dbc.Col([
                        html.Img([
                        ], src = "../app/assets/search-img.png")
                        ] , width =4)
                ], className = "active-space")
            ], className = "app-card")
        ], className= "app-container")
    ],className= "main-space" )
]
)









if __name__ == '__main__':
    app.run_server(debug=True)

