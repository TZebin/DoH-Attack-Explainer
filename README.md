# DoH Attack Explainer
An Explainable AI-based Intrusion Detection System for DNS over HTTPS (DoH) Attacks
![dashboard_recording_First_Frame](https://user-images.githubusercontent.com/31511385/169506515-39478118-e37f-4c81-aa2c-72cd5ba07b54.png)

 ## Installation

You can install the package through pip:

`pip install explainerdashboard`

or conda-forge:

`conda install -c conda-forge explainerdashboard`


##The library includes:
- *Shap values* (i.e. what is the contributions of each feature to each individual prediction?)
- *Permutation importances* (how much does the model metric deteriorate when you shuffle a feature?)
- *Partial dependence plots* (how does the model prediction change when you vary a single feature?
- *Shap interaction values* (decompose the shap value into a direct effect an interaction effects)
- For Random Forests and xgboost models: visualisation of individual decision trees
- Plus for classifiers: precision plots, confusion matrix, ROC AUC plot, PR AUC plot, etc


## Command line tool

You can store explainers to disk with `explainer.dump("explainer.pkl")`
and then run them from the command-line:

```bash
$ explainerdashboard run explainer.pkl
