import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

data = pd.read_csv("environment_data.csv") 

le_sensor = LabelEncoder()
le_status = LabelEncoder()

data["Sensor_ID"] = le_sensor.fit_transform(data["Sensor_ID"])
data["Alert_Status"] = le_status.fit_transform(data["Alert_Status"])

X = data[["Sensor_ID", "Temperature_C", "Humidity_Pct"]]
y = data["Alert_Status"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=le_status.classes_))

joblib.dump(model, "environment_monitor_model.pkl")
joblib.dump({
    "Sensor_ID": le_sensor,
    "Alert_Status": le_status
}, "env_label_encoders.pkl")

print("\nModel saved as environment_monitor_model.pkl")
print("Label encoders saved as env_label_encoders.pkl")



