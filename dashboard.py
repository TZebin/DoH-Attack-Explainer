
# xgboost is a dependency of dtreeviz, but too large (>350M) for heroku
# so we uninstall it and mock it here:
from unittest.mock import MagicMock
import sys
sys.modules["xgboost"] = MagicMock()

from pathlib import Path
from flask import Flask

import dash
from dash_bootstrap_components.themes import FLATLY, BOOTSTRAP # bootstrap theme
from explainerdashboard import *

from index_layout import index_layout, register_callbacks
from custom import CustomModelTab, CustomPredictionsTab

pkl_dir = Path.cwd() / "pkls"

app = Flask(__name__)

class_explainer = ClassifierExplainer.from_file(pkl_dir / "class_explainer.joblib")
class_dashboard = ExplainerDashboard(class_explainer, 
                    title="Classifier Explainer: Predicting Health_status for Salmon", 
                    server=app, url_base_pathname="/classifier/", 
                    header_hide_selector=True)


index_app = dash.Dash(
    __name__, 
    server=app, 
    url_base_pathname="/", 
    external_stylesheets=[BOOTSTRAP])

index_app.title = 'Salmon explainerdashboard'
index_app.layout = index_layout
register_callbacks(index_app)

@app.route("/")
def index():
    return index_app.index()

@app.route('/classifier')
def classifier_dashboard():
    return class_dashboard.app.index()
