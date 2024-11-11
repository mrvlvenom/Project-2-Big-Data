import json
# Membaca data dari file all_data.json
with open("/home/ilhanahmads/projek2/consumer/all_data.json", 'r') as f:
    all_data = json.load(f)

# Menentukan jumlah data untuk setiap model
model_1_data = all_data[:800]  # 800 data pertama
model_2_data = all_data[:1600]  # 800 data pertama + 800 data kedua
model_3_data = all_data[:]  # 800 data pertama + 800 data kedua + 900 data ketiga

# Menyimpan data yang dibagi ke dalam file terpisah untuk setiap model
with open("model_1_data.json", 'w') as f:
    json.dump(model_1_data, f)

with open("model_2_data.json", 'w') as f:
    json.dump(model_2_data, f)

with open("model_3_data.json", 'w') as f:
    json.dump(model_3_data, f)

print("Data successfully split into model training datasets.")

