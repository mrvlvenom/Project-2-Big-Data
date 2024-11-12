# Project-2-Big-Data
## Prediksi Hujan menggunakan Apache Kafka dan PySparkML

| No | Nama | NRP |
|---|---|---|
| 1 | M. Januar Eko Wicaksono | 50272221006 |
| 2 | Iki Adfi Nur Mohamad | 50272221033 |
| 3 | Ilhan Ahmad Syafa | 50272221040 |

# Setup
- `docker-compose.yaml` digunakan untuk mengatur konfigurasi docker beberapa service yang dibutuhkan
- `consumer.py` digunakan untuk menerima data yang dikirim dari producer berdasarkan dataset yang tersedia
- `producer.py` digunakan untuk mengirim data ke consumer berdasarkan dataset yang tersedia
- `prep_data.py` digunakan untuk memisahkan data yang akan digunakan untuk melatih model
- `train_model.py` digunakan untuk melatih model berdasarkan batch data yang diterima consumer
- `app.py` digunakan untuk routing endpoint

# Langkah
### 1. Setup Docker
Atur konfigurasi docker pada file `docker-compose.yaml` sesuai kebutuhan kemudian jalankan command `docker-compose up -d` untuk menjalankan service yang dibutuhkan

### 2. Setup Producer dan Consumer
Buat script untuk menjalankan skenario producer dan consumer. Pastikan consumer dapat menerima aliran data yang dikirim producer berdasarkan dataset yang tersedia.

