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
                html.H1(["FAKE ACCOUNT POLICE"], className = "app-title-text"),
                html.H5(["ASSESS CREDIBILITY OF IG ACCOUNTS"], className = "app-title-sub"),
                dbc.Row([
                    dbc.Col([
                        html.Div(["ACCOUNT INFO"]),
                        dbc.Row([
                            dbc.Col([
                                html.Div(["Username"]),
                                dcc.Input(id = "enter-username", type = "text", placeholder = "@username")
                                ]),
                            dbc.Col([
                                html.Div(["Full name"]),
                                dcc.Input(id = "enter-display-name", type = "text", placeholder = "display-name")
                                ]),
                    ]),
                        html.Br(),
                        dbc.Row([
                            html.Div(["Bio"]),
                            dcc.Input(id = "enter-bio", type = "text", placeholder = "bio")
                    ], justify = "center" ),
                        html.Br(),
                        dbc.Row([
                            dbc.Col([
                                html.Div(["Has Profile Picture?"]),
                                dcc.Dropdown(["Yes", "No"], "Choose", id = "profile-pic")
                            ]),
                            dbc.Col([
                                html.Div(["Link in bio?"]),
                                dcc.Dropdown(["Yes", "No"], "Choose", id = "url-bio")
                            ]),
                            dbc.Col([
                                html.Div(["Account private?"]),
                                dcc.Dropdown(["Yes", "No"], "Choose", id = "account-privacy")
                            ]),
                    ]),
                        html.Br(),
                        dbc.Row([
                            dbc.Col([
                                html.Div(["Followers"]),
                                dcc.Input(id = "follower-count", type = "number", placeholder = "no. of followers")
                            ]),
                            dbc.Col([
                                html.Div(["Following"]),
                                dcc.Input(id = "following-count", type = "text", placeholder = "no. of follows")
                            ]),
                            dbc.Col([
                                html.Div(["No. of posts"]),
                                dcc.Input(id = "posts-count", type = "text", placeholder = "no. of posts")
                            ]),
                    ]),
                        html.Br(),
                        dbc.Row([
                            html.Div([
                                dbc.Button(
                                    "Investigate", id="model-trigger", className="trigger-button", n_clicks=0
                                ),
                                
                            ]
)
                        ])
                        ], width=8, className = "input-section"),
                    dbc.Col([
                        
                        ], id = "change-picture" , width =4)
                ], className = "active-space")
            ], className = "app-card")
        ], className= "app-container")
    ],className= "main-space" )
]
)


@app.callback(
    Output("change-picture", "children"), 
    [Input("model-trigger", "n-clicks")],
    [State("enter-username", "value")],
    [State("enter-display-name", "value")],
    [State("enter-bio", "value")],
    [State("profile-pic", "value")],
    [State("account-privacy", "value")],
    [State("url-bio", "value")],
    [State("follower-count", "value")],
    [State("follow-count", "value")],
    [State("post-count", "value")]
)
def run_assessment(username, fullname, bio, pic, privacy, url, followers, following, posts):
    if pic == "Yes":
        profile = 0 + 1
    if url == "Yes":
        url_bio  = 0 + 1
    if privacy == "Yes":
        account_privacy = 0 + 1
    if username.lower() == fullname.lower():
        user_is_full = 0 + 1
    num_in_user = len(re.findall(r'[0-9]+', username))
    fraction_num_user = num_in_user/len(username)
    fullname_words = len(fullname.split())
    num_in_full = len(re.findall(r'[0-9]+', fullname))
    fraction_num_full = num_in_full/len(fullname)
    bio_length = len(bio)
    follower_count = followers.astype(int)
    following_count = following.astype(int)
    post_count = posts.astype(int)
    data_dict = {
    "profile_pic": profile, 
    "num_per_length_username": num_in_user,
    "fullname_words": fullname_words,
    "num_per_length_fullname": num_in_full,
    "fullname_is_username": user_is_full,
    "bio_length": bio_length,
    "url_in_bio": url_bio,
    "private":account_privacy,
    "#posts":post_count,
    "#followers":follower_count,
    "#follows":following_count,
    
}
    df = pd.DataFrame(data_dict)
    scaler = StandardScaler()
    scaled_data =scaler.fit_transform(df)
    prediction = model.predict(scaled_data)
    return prediction



if __name__ == '__main__':
    model = pickle.load(open("../models/LRmodel.sav", 'rb'))
    app.run_server(debug=True)

