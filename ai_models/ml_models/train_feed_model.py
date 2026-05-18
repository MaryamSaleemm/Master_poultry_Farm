
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib


data = pd.read_csv("feed_data.csv")

le_feed = LabelEncoder()
le_formula = LabelEncoder()
le_season = LabelEncoder()

data["Feed_Type"] = le_feed.fit_transform(data["Feed_Type"])
data["Feed_Blend_Formula"] = le_formula.fit_transform(data["Feed_Blend_Formula"])
data["Season_Applied"] = le_season.fit_transform(data["Season_Applied"])

X = data[["Feed_Type", "Feed_Blend_Formula", "Avg_House_Temp_C", "Season_Applied"]]
y = data["Daily_Amount_kg"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Mean Absolute Error:", round(mean_absolute_error(y_test, y_pred), 2))
print("R² Score:", round(r2_score(y_test, y_pred), 3))

# Save trained model
joblib.dump(model, "feed_prediction_model.pkl")
print(" Model saved as feed_prediction_model.pkl")

joblib.dump({
    "Feed_Type": le_feed,
    "Feed_Blend_Formula": le_formula,
    "Season_Applied": le_season
}, "feed_label_encoders.pkl")
print("Label encoders saved as feed_label_encoders.pkl")
