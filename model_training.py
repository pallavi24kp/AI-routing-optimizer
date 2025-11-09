import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

df = pd.read_csv('data/routing_data.csv')

X = df[['latency_ms', 'bandwidth_mbps', 'traffic_load', 'hop_count']]
y = df['score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

score = model.score(X_test, y_test)
print(f" Model trained with accuracy: {score:.2f}")

joblib.dump(model, 'models/routing_model.pkl')
print(" Model saved in models/routing_model.pkl")
