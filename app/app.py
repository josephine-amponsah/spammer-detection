import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from sklearn.preprocessing import StandardScaler
import re
import pickle 


# from app.pages import sales
FA = "https://fonts.googleapis.com/css?family=Lobster"
app = dash.Dash(__name__,  external_stylesheets=[ FA,
                dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])
# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])


app.layout = html.Div([
    html.Div([
        dbc.Container([
            html.Div([
                html.H1(["INSTAGRAM SPAMMER DETECTOR"], className = "app-title-text"),
                # html.H5(["ASSESS CREDIBILITY OF IG ACCOUNTS"], className = "app-title-sub"),
                dbc.Card([
                    dbc.Row([
                        dbc.Col([
                            dbc.Card([
                                html.Div(["ACCOUNT INFO"], style = {'text-align': 'center', 'font-weight': 'bold', 'color':'#2d56b3'}),
                                html.Br(),
                                dbc.Row([
                                    dbc.Col([html.Div(["Username"])], width = 4),
                                    dbc.Col([dcc.Input(id = "enter-username", type = "text", placeholder = "@username", className = "input-long-box")], width = 7)
                                    ]),
                                html.Br(),
                                dbc.Row([
                                    dbc.Col([html.Div(["Full name"])], width = 4),
                                    dbc.Col([dcc.Input(id = "enter-display-name", type = "text", placeholder = "display-name", className = "input-long-box")], width = 7)
                                        
                                ]),
                                html.Br(),
                                dbc.Row([
                                    dbc.Col([
                                        html.Div(["Bio"]),
                                    ], width = 4),
                                    dbc.Col([dcc.Input(id = "enter-bio", type = "text", placeholder = "bio", className="input-long-box")], width = 7)
                                    
                            ], ),
                                html.Br(),
                                dbc.Row([
                                    dbc.Col([
                                        html.Div(["Profile Picture?"]),
                                        dcc.Dropdown(["Yes", "No"], "Choose", id = "profile-pic", className="dropdown-box")
                                    ], width=4),
                                    dbc.Col([
                                        html.Div(["Link in bio?"]),
                                        dcc.Dropdown(["Yes", "No"], "Choose", id = "url-bio", className="dropdown-box")
                                    ], width=4),
                                    dbc.Col([
                                        html.Div(["Account private?"]),
                                        dcc.Dropdown(["Yes", "No"], "Choose", id = "account-privacy", className="dropdown-box")
                                    ], width=4),
                                ], justify= 'start'),
                                html.Br(),
                                dbc.Row([
                                    dbc.Col([html.Div(["Followers"]),], width = 4),
                                    dbc.Col([dcc.Input(id = "follower-count", type = "number", placeholder = "no. of followers", className="input-long-box")], width = 7)
                                ]),
                                html.Br(),
                                dbc.Row([
                                    dbc.Col([html.Div(["Following"])], width=4),
                                    dbc.Col([dcc.Input(id = "following-count", type = "text", placeholder = "no. of follows", className="input-long-box")], width = 7)
                                ]),
                                html.Br(),
                                dbc.Row([
                                    dbc.Col([html.Div(["No. of posts"])], width = 4),
                                    dbc.Col([dcc.Input(id = "posts-count", type = "text", placeholder = "no. of posts", className="input-long-box")], width = 7)
                                   
                            ]),
                                html.Br(),
                                dbc.Row([
                                    dbc.Col([
                                        dbc.Button(
                                            "Investigate", id="model-trigger", className="trigger-button", n_clicks=0
                                        )
                                    ], width= 4)
                                ], justify='center')
                            ], className = "input-card", outline=True)
                        ], width=6),
                        dbc.Col([
                            dbc.Card([
                                dbc.Row([
                                    dbc.Row([html.H2("RESULTS...")],),
                                    dbc.Row([html.Img(src='../assets/Search-rafiki.png')])
                                ],className="image-search")
                            ], className="image-card")
                        ], id = "change-picture" , width =6)
                    ])
                ], className = "active-space")
            ], className = "app-card")
        ], className= "app-container")
    ],className= "main-space" )
]
)


# @app.callback(
#     Output("change-picture", "children"), 
#     [Input("model-trigger", "n-clicks")],
#     [State("enter-username", "value")],
#     [State("enter-display-name", "value")],
#     [State("enter-bio", "value")],
#     [State("profile-pic", "value")],
#     [State("account-privacy", "value")],
#     [State("url-bio", "value")],
#     [State("follower-count", "value")],
#     [State("follow-count", "value")],
#     [State("post-count", "value")]
# )
# def run_assessment(username, fullname, bio, pic, privacy, url, followers, following, posts):
#     # sourcery skip: inline-immediately-returned-variable
#     if pic == "Yes":
#         profile = 0 + 1
#     if url == "Yes":
#         url_bio  = 0 + 1
#     if privacy == "Yes":
#         account_privacy = 0 + 1
#     if username.lower() == fullname.lower():
#         user_is_full = 0 + 1
#     num_in_user = len(re.findall(r'[0-9]+', username))
#     fraction_num_user = num_in_user/len(username)
#     fullname_words = len(fullname.split())
#     num_in_full = len(re.findall(r'[0-9]+', fullname))
#     fraction_num_full = num_in_full/len(fullname)
#     bio_length = len(bio)
#     follower_count = followers.astype(int)
#     following_count = following.astype(int)
#     post_count = posts.astype(int)
#     data_dict = {
#     "profile_pic": profile, 
#     "num_per_length_username": num_in_user,
#     "fullname_words": fullname_words,
#     "num_per_length_fullname": num_in_full,
#     "fullname_is_username": user_is_full,
#     "bio_length": bio_length,
#     "url_in_bio": url_bio,
#     "private":account_privacy,
#     "#posts":post_count,
#     "#followers":follower_count,
#     "#follows":following_count,
    
# }
#     df = pd.DataFrame(data_dict)
#     scaler = StandardScaler()
#     scaled_data =scaler.fit_transform(df)
#     prediction = model.predict(scaled_data)
#     return prediction



if __name__ == '__main__':
    model = pickle.load(open("../models/LRmodel.sav", 'rb'))
    app.run_server(debug=True)

