# Aplikasi Data Warga Kelurahan

Aplikasi management data warga berbasis Django dengan Class-Based Views untuk tugas kuliah.

## ✨ Fitur
- ✅ Model Warga dengan field lengkap (NIK, nama, alamat, telepon)
- ✅ Admin Django untuk management data
- ✅ Class-Based ListView (CBV)
- ✅ Template untuk menampilkan daftar warga
- ✅ 5 data contoh (Wahyu, Fatih, Faqih, Ibrahim, Dhea)

## 🛠️ Teknologi
- Django 4.2+
- SQLite
- Python 3.8+
- Class-Based Views

## 🚀 Cara Menjalankan
```bash
# Install dependencies
pip install django

# Setup database
python manage.py migrate

# Jalankan server
python manage.py runserver
Buka http://127.0.0.1:8000/warga/ untuk melihat daftar warga
Buka http://127.0.0.1:8000/admin/ untuk management data
