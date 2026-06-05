import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Sample dataset
data = {
    'url_length': [10, 50, 15, 70, 20, 90],
    'dots': [1, 5, 1, 7, 2, 8],
    'https': [1, 0, 1, 0, 1, 0],
    'label': [0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[['url_length', 'dots', 'https']]
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "phishing_model.pkl")

print("Model saved successfully!")