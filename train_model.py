import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from feature_extractor import extract_features

# Load dataset
df = pd.read_csv("phishing_dataset.csv")

# Extract features from URLs
df['features'] = df['url'].apply(extract_features)
X = pd.DataFrame(df['features'].to_list())
y = df['label']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "phishing_model.joblib")
print("✅ Model saved as phishing_model.joblib")
