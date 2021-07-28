import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State

navbar = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("github", href="https://github.com/Shahadate-Rezvy/salmon_explainer"),
            ],
            nav=True,
            in_navbar=True,
            label="Source",
        ),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("readthedocs", href="http://explainerdashboard.readthedocs.io/en/latest/"),
                dbc.DropdownMenuItem("pypi", href="https://pypi.org/project/explainerdashboard/"),
            ],
            nav=True,
            in_navbar=True,
            label="explainerdashboard",
        ),
        
    ],
    brand="Salmon Model Explainer",
    brand_href="https://github.com/Shahadate-Rezvy/salmon_explainer",
    color="primary",
    dark=True,
    fluid=True,
)

salmon_card = dbc.Card(
    [
       
        dbc.CardBody(
            [
                html.H4("Classifier Dashboard", className="card-title"),
                html.P(
                    "Salmon dashboard."
                    ,className="card-text",
                ),
                html.A(dbc.Button("Go to dashboard", color="primary"),
                       href="/classifier"),
                dbc.Button("Show Code", id="clas-code-modal-open", className="mr-1"),
                dbc.Modal(
                    [
                        dbc.ModalHeader("Code needed for this Classifier Dashboard"),
                        dcc.Markdown(
"""
```python
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from explainerdashboard import ClassifierExplainer, ExplainerDashboard


pkl_dir = Path.cwd() / "pkls"
data_dirz= Path.cwd() / "data"
df=pd.read_csv(data_dir /'new_processed.csv')
y=df['JB_category']
X=df.drop(columns=['JB_category'])

# classifier
X_train, y_train, X_test, y_testtrain_test_split(X,y, stratify=y,test_size = 0.1, random_state=0)
rf = RandomForestClassifier(n_estimators=10, random_state=0,max_depth=5, \
                            class_weight='balanced').fit(X_train, y_train)
clas_explainer = ClassifierExplainer(model, X_test, y_test, 
                               descriptions=feature_descriptions,
                               labels=['HEALTHY', 'UNHEALTHY'])
_ = ExplainerDashboard(clas_explainer)
clas_explainer.dump(pkl_dir/ "clas_explainer.pkl")
```
"""
                        ),
                        dbc.ModalFooter(
                            dbc.Button("Close", id="clas-code-modal-close", className="ml-auto")
                        ),
                    ],
                    id="clas-code-modal",
                    size="lg",
                ),
            ]
        ),
    ],
    style={"width": "18rem"},
)

default_cards = dbc.CardDeck([salmon_card])

index_layout =  dbc.Container([
    navbar,     
    dbc.Row([
        dbc.Col([
            html.H3("explainerdashboard"),
           
        ])
    ]),
    
    
    dbc.Row([
        dbc.Col([
            html.H3("Examples"),
            dcc.Markdown("""
Below you can find demonstrations of the three default dashboards for classification, 
regression and multi class classification problems, plus one demonstration of 
a custom dashboard.
"""),
        ])
    ]),
    
    dbc.Row([
        dbc.Col([
            default_cards,
        ]),
    ]),
    
    ])

def register_callbacks(app):
    @app.callback(
        Output("clas-code-modal", "is_open"),
        Input("clas-code-modal-open", "n_clicks"), 
        Input("clas-code-modal-close", "n_clicks"),
        State("clas-code-modal", "is_open"),
    )
    def toggle_modal(click_open, click_close, is_open):
        if click_open or click_close:
            return not is_open
        return is_open
