import mlflow
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import random
import numpy as np
import os
import warnings
import sys
 
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(40)
 
    file_path = sys.argv[3] if len(sys.argv) > 3 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "train_pca.csv")
    data = pd.read_csv(file_path)
 
    X_train, X_test, y_train, y_test = train_test_split(
    data.drop("Credit_Score", axis=1),
    data["Credit_Score"],
    random_state=42,
    test_size=0.2
    )
    input_example = X_train[0:5]
    n_estimators = int(sys.argv[1]) if len(sys.argv) > 1 else 505
    max_depth = int(sys.argv[2]) if len(sys.argv) > 2 else 37
 
model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth)
model.fit(X_train, y_train)

# Simpan model ke folder output lokal
import mlflow.sklearn
mlflow.sklearn.save_model(
    sk_model=model,
    path="output_model",  # atau folder lain yang kamu inginkan
    input_example=input_example
)

# Simpan metric accuracy ke file
accuracy = model.score(X_test, y_test)

# Tulis metric ke file manual
with open("metrics.txt", "w") as f:
    f.write(f"accuracy: {accuracy:.4f}\n")
