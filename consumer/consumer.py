from kafka import KafkaConsumer
import json

# Inisialisasi Kafka Consumer
consumer = KafkaConsumer(
    'weather-topic',  # Topic
    bootstrap_servers='localhost:9092',
    group_id='weather-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Menyimpan data dalam batch
batch_size = 100
batch = []
batch_counter = 1 
row_counter = 0  
max_rows = 2500 

all_data = []

for message in consumer:
    batch.append(message.value)
    row_counter += 1 
    
    if len(batch) >= batch_size:
        print(f"Saving batch {batch_counter} with rows {row_counter - batch_size + 1} to {row_counter}...")
        
        with open(f"batch_{batch_counter}.json", 'w') as f:
            json.dump(batch, f)  # Menyimpan batch dalam format JSON
        
        # Menambahkan batch yang telah diproses ke dalam data lengkap
        all_data.extend(batch)
        
        batch = []
        batch_counter += 1 

    if row_counter >= max_rows:
        print(f"Processed {row_counter} rows. Stopping Kafka Consumer.")
        break

# Pastikan consumer berhenti setelah mencapai 2500 baris
consumer.close()

# Menyimpan data lengkap ke file untuk pelatihan model
with open("all_data.json", 'w') as f:
    json.dump(all_data, f)

