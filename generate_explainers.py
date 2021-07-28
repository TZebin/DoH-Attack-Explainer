from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from explainerdashboard import ClassifierExplainer, ExplainerDashboard


pkl_dir = Path.cwd() / "pkls"
data_dir= Path.cwd() / "data"
df=pd.read_csv(data_dir /'new_processed.csv')
y=df['JB_category']
X=df.drop(columns=['JB_category'])



# classifier
X_train, X_test,y_train, y_test=train_test_split(X,y, stratify=y,test_size = 0.1, random_state=42)
# classifier
model = RandomForestClassifier(n_estimators=10, random_state=42,max_depth=5,class_weight='balanced')
model.fit(X_train, y_train)
class_explainer = ClassifierExplainer(model, X_test, y_test, 
                               labels=['HEALTHY', 'UNHEALTHY'])
_ = ExplainerDashboard(class_explainer)
#class_explainer.dump(pkl_dir/ "class_explainer.joblib")
class_explainer.dump(pkl_dir/ "class_explainer.pkl")
