
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import joblib

data = pd.read_csv("egg_model.csv",sep='\t') 

encoder = LabelEncoder()
data['Breed_Type'] = encoder.fit_transform(data['Breed_Type'])


X = data[['Feed_kg', 'Temperature_C', 'Humidity_%', 'Breed_Type']]
y = data['Egg_Count']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, "egg_model.pkl")  
joblib.dump(encoder, "egg_label_encoder.pkl") 
print("Model trained and saved as egg_model.pkl")
