# randomforest-predictor-streamlit-app
Dashboard interaktif menggunakan Streamlit dan **Random Forest Classifier** untuk prediksi keputusan membeli berdasarkan usia dan pendapatan.

# 📊 Prediksi Keputusan Membeli dengan Streamlit + Random Forest

Proyek ini merupakan implementasi sederhana dari **Random Forest Classifier** menggunakan `scikit-learn`, disajikan sebagai **Dashboard interaktif** dengan Streamlit bergaya HUD Futuristik.

## 🚀 Fitur

- [✓] Dataset sintetik (usia & pendapatan)
- [✓] Training model Random Forest
- [✓] Simpan model ke file `.pkl`
- [✓] Antarmuka prediksi interaktif dengan Streamlit
- [✓] Tema dashboard futuristik (HUD-style)

## 📁 Struktur Proyek

```
.
├── app.py              # Streamlit dashboard interaktif
├── main.py             # Training model dan save ke pickle
├── requirements.txt    # Daftar dependency Python
├── .gitignore          # File/folder yang diabaikan Git
└── models/
    └── random_forest_model.pkl  # File model hasil training
```

## ⚙️ Instalasi

```bash
# 1. Clone repository ini
git clone https://github.com/username/streamlit-random-forest-app.git
cd streamlit-random-forest-app

# 2. Install dependensi
pip install -r requirements.txt

# 3. Jalankan training untuk membuat model
python main.py

# 4. Jalankan aplikasi Streamlit
streamlit run app.py
```

## 🖥️ Tampilan Dashboard

- Input usia & pendapatan
- Prediksi instan: apakah pelanggan akan membeli?
- Antarmuka neon modern dengan efek futuristik

## 🧠 Teknologi yang Digunakan

- Python 3.x
- scikit-learn
- Streamlit
- Pickle
- NumPy & Pandas
- Matplotlib (untuk training opsional)

## 🎨 Tema Warna Futuristik

| Elemen          | Warna       | Fungsi                        |
|-----------------|-------------|-------------------------------|
| Latar belakang  | `#0C3B5D`   | Dasar layar                   |
| Teks utama      | `#00FFFF`   | Kontras tinggi, neon look     |
| Hover tombol    | `#008B8B`   | Efek dinamis saat mouse hover |

## 📌 Lisensi

Proyek ini dilisensikan di bawah lisensi MIT — bebas digunakan, dimodifikasi, dan dibagikan.

---

Created with ❤️ by arielshakaramiro
