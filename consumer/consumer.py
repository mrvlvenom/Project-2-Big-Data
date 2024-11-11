from kafka import KafkaConsumer
import json

# Inisialisasi Kafka Consumer
consumer = KafkaConsumer(
    'weather-topic',  # Nama topic
    bootstrap_servers='localhost:9092',
    group_id='weather-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Menyimpan data dalam batch
batch_size = 100
batch = []
batch_counter = 1  # Untuk nomor batch file
row_counter = 0  # Untuk menghitung jumlah row yang telah diproses
max_rows = 2500  # Batas maksimal jumlah baris yang akan diproses

# Menyimpan semua data untuk porsi pelatihan
all_data = []

for message in consumer:
    # Menambahkan pesan ke dalam batch
    batch.append(message.value)
    row_counter += 1  # Menambah hitungan baris yang diterima
    
    # Jika batch mencapai ukuran yang diinginkan, simpan data ke file JSON terpisah
    if len(batch) >= batch_size:
        print(f"Saving batch {batch_counter} with rows {row_counter - batch_size + 1} to {row_counter}...")
        
        # Menyimpan batch ke file terpisah dengan nama batch_X.json
        with open(f"batch_{batch_counter}.json", 'w') as f:
            json.dump(batch, f)  # Menyimpan batch dalam format JSON
        
        # Menambahkan batch yang telah diproses ke dalam data lengkap
        all_data.extend(batch)
        
        # Reset batch untuk menerima data berikutnya
        batch = []
        batch_counter += 1  # Increment nomor batch untuk file selanjutnya

    # Jika sudah mencapai jumlah baris maksimal, hentikan consumer
    if row_counter >= max_rows:
        print(f"Processed {row_counter} rows. Stopping Kafka Consumer.")
        break

# Pastikan consumer berhenti setelah mencapai 2500 baris
consumer.close()

# Menyimpan data lengkap ke file untuk pelatihan model
with open("all_data.json", 'w') as f:
    json.dump(all_data, f)

