file train_model.py

import json
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Fungsi untuk mempersiapkan data
def prepare_data(file_path, features, target, num_rows):
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

    # Memilih jumlah data sesuai dengan parameter num_rows
    df = df.head(num_rows)

    # Memisahkan fitur dan target
    X = df[features]  # Fitur yang digunakan untuk pelatihan
    y = df[target]  # Target yang ingin diprediksi
    return X, y, df

# Model 1: Prediksi Rain dengan 800 data pertama
def train_model_1():
    features = ['Temperature', 'Humidity', 'Pressure']
    target = 'Rain'  # Kolom target untuk prediksi hujan

    # Menyiapkan data dari file model_data.json dengan 800 data pertama
    X, y, df = prepare_data('model_1_data.json', features, target, 800)

    # Membagi data menjadi training dan testing set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Membuat dan melatih model RandomForestClassifier
    model_1 = RandomForestClassifier(n_estimators=100, random_state=42)
    model_1.fit(X_train, y_train)

    # Evaluasi model
    y_pred = model_1.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model 1 (Rain Prediction - 800 data): Accuracy = {accuracy:.4f}")

    # Menyimpan model
    joblib.dump(model_1, 'model_1.pkl')

    # Prediksi nilai target 'rain' untuk data yang ada
    df['Predicted_Rain'] = model_1.predict(X)
    print("\nPredictions for Rain using Machine Learning (Model 1 - 800 data):")
    print(df[['Temperature', 'Humidity', 'Pressure', 'Predicted_Rain']].head())

# Model 2: Prediksi Rain dengan 1600 data pertama
def train_model_2():
    features = ['Temperature', 'Humidity', 'Pressure']
    target = 'Rain'  # Kolom target untuk prediksi hujan

    # Menyiapkan data dari file model_data.json dengan 1600 data pertama
    X, y, df = prepare_data('model_2_data.json', features, target, 1600)

    # Membagi data menjadi training dan testing set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Membuat dan melatih model RandomForestClassifier
    model_2 = RandomForestClassifier(n_estimators=100, random_state=42)
    model_2.fit(X_train, y_train)

    # Evaluasi model
    y_pred = model_2.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model 2 (Rain Prediction - 1600 data): Accuracy = {accuracy:.4f}")

    # Menyimpan model
    joblib.dump(model_2, 'model_2.pkl')

    # Prediksi nilai target 'rain' untuk data yang ada
    df['Predicted_Rain'] = model_2.predict(X)
    print("\nPredictions for Rain using Machine Learning (Model 2 - 1600 data):")
    print(df[['Temperature', 'Humidity', 'Pressure', 'Predicted_Rain']].head())

# Model 3: Prediksi Rain dengan semua data (2500 data)
def train_model_3():
    features = ['Temperature', 'Humidity', 'Pressure']
    target = 'Rain'  # Kolom target untuk prediksi hujan

    # Menyiapkan data dari file model_data.json dengan semua data (2500)
    X, y, df = prepare_data('model_3_data.json', features, target, 2500)

    # Membagi data menjadi training dan testing set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Membuat dan melatih model RandomForestClassifier
    model_3 = RandomForestClassifier(n_estimators=100, random_state=42)
    model_3.fit(X_train, y_train)

    # Evaluasi model
    y_pred = model_3.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model 3 (Rain Prediction - 2500 data): Accuracy = {accuracy:.4f}")

    # Menyimpan model
    joblib.dump(model_3, 'model_3.pkl')

    # Prediksi nilai target 'rain' untuk data yang ada
    df['Predicted_Rain'] = model_3.predict(X)
    print("\nPredictions for Rain using Machine Learning (Model 3 - 2500 data):")
    print(df[['Temperature', 'Humidity', 'Pressure', 'Predicted_Rain']].head())

# Fungsi utama untuk melatih semua model
def train_all_models():
    train_model_1()
    train_model_2()
    train_model_3()

if _name_ == "_main_":
    train_all_models()
