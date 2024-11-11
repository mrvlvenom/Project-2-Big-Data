import pandas as pd
import random
import time
from kafka import KafkaProducer
import json

# Membaca dataset cuaca
data = pd.read_csv('/home/ilhanahmads/projek2/data/weather_forecast_data.csv')

# Inisialisasi producer Kafka
producer = KafkaProducer(bootstrap_servers='localhost:9092', 
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Kafka topic tempat data akan dikirim
topic = 'weather-topic'

# Mengirimkan data satu baris per waktu
for _, row in data.iterrows():
    message = row.to_dict()  # Mengubah baris menjadi dictionary
    producer.send(topic, value=message)  # Mengirim data ke Kafka
    
    # Simulasikan delay acak antara 0.1 sampai 1 detik
    time.sleep(random.uniform(0.1, 1.0))

# Pastikan semua pesan terkirim sebelum keluar
producer.flush()
producer.close()

