import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle

# Data load
df = pd.read_csv('cancer_data.csv')
X = df.drop('target', axis=1)
y = df['target']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Train
# model = RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42)
# Naya — n_estimators badlo
model = RandomForestClassifier(
    n_estimators=200, max_depth=6, random_state=42)
model.fit(X_train_scaled, y_train)

# Save
with open('cancer_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

print("Model aur Scaler saved!")