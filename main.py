import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Simulasi Data: Usia & Pendapatan
np.random.seed(42)
usia = np.random.randint(20, 60, 200)
pendapatan = np.random.randint(2000, 10000, 200)
beli = ((usia > 35) & (pendapatan > 5000)).astype(int)

# Membuat DataFrame
df = pd.DataFrame({"Usia": usia, "Pendapatan": pendapatan, "Beli": beli})

# Split dataset
X = df[["Usia", "Pendapatan"]]
y = df["Beli"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat model Random Forest
model = RandomForestClassifier(n_estimators=20, max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Prediksi & Evaluasi
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print(classification_report(y_test, y_pred))

# Simpan model ke file
with open("models/random_forest_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model berhasil disimpan sebagai 'models/random_forest_model.pkl'")