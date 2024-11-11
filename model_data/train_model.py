import json
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Fungsi untuk mempersiapkan data
def prepare_data(file_path, features, target):
    # Membaca data dari file JSON
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Mengubah data ke dalam format DataFrame
    df = pd.DataFrame(data)

    # Melakukan Exploratory Data Analysis (EDA)
    print("Data Overview:")
    print(df.head())
    print("\nSummary Statistics:")
    print(df.describe())

    # Memisahkan fitur dan target
    X = df[features]  # Fitur yang digunakan untuk pelatihan
    y = df[target]  # Target yang ingin diprediksi
    return X, y, df

# Model 2: Prediksi Pola Musiman atau Zona Iklim (Berdasarkan Temperature, Humidity, Pressure)
def train_model_2():
    features = ['Temperature', 'Humidity', 'Pressure']
    target = 'Seasonal_Pattern'  # Kolom target untuk pola musiman

    # Menyiapkan data dari file model_2_data.json
    X, y, df = prepare_data('model_2_data.json', features, target)

    # Membagi data menjadi training dan testing set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Membuat dan melatih model RandomForestClassifier
    model_2 = RandomForestClassifier(n_estimators=100, random_state=42)
    model_2.fit(X_train, y_train)

    # Evaluasi model
    y_pred = model_2.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model 2 (Pola Musiman): Accuracy = {accuracy:.4f}")

    # Menyimpan model
    joblib.dump(model_2, 'model_2.pkl')

    # Prediksi nilai target 'Seasonal_Pattern' untuk data yang ada
    df['Predicted_Seasonal_Pattern'] = model_2.predict(X)
    print("\nPredictions for Seasonal_Pattern using Machine Learning:")
    print(df[['Temperature', 'Humidity', 'Pressure', 'Predicted_Seasonal_Pattern']].head())

# Model 3: Prediksi Potensi Bencana Alam
def train_model_3():
    features = ['Temperature', 'Humidity', 'Pressure', 'Wind_Speed', 'Cloud_Cover']
    target = 'Disaster_Potential'  # Kolom target untuk potensi bencana alam

    # Menyiapkan data dari file model_3_data.json
    X, y, df = prepare_data('model_3_data.json', features, target)

    # Membagi data menjadi training dan testing set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Membuat dan melatih model RandomForestClassifier
    model_3 = RandomForestClassifier(n_estimators=100, random_state=42)
    model_3.fit(X_train, y_train)

    # Evaluasi model
    y_pred = model_3.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model 3 (Potensi Bencana Alam): Accuracy = {accuracy:.4f}")

    # Menyimpan model
    joblib.dump(model_3, 'model_3.pkl')

    # Prediksi nilai target 'Disaster_Potential' untuk data yang ada
    df['Predicted_Disaster_Potential'] = model_3.predict(X)
    print("\nPredictions for Disaster_Potential using Machine Learning:")
    print(df[['Temperature', 'Humidity', 'Pressure', 'Wind_Speed', 'Cloud_Cover', 'Predicted_Disaster_Potential']].head())

# Fungsi utama untuk melatih semua model
def train_all_models():
    train_model_2()
    train_model_3()

if __name__ == "__main__":
    train_all_models()

