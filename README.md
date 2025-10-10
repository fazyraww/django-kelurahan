# Sistem Data Warga Kelurahan

Aplikasi web untuk management data kependudukan warga di tingkat kelurahan.

## 🚀 Akses Aplikasi

### 🌐 **LIVE DEMO**
```bash
# Jalankan server development
python manage.py runserver

# Buka browser dan akses:
🎯 Halaman	🔗 URL	📝 Keterangan
Halaman Utama	http://localhost:8000/warga/	Lihat daftar semua warga
Admin Dashboard	http://localhost:8000/admin/	Kelola data warga
Django Default	http://localhost:8000/	Halaman welcome Django
⚡ Quick Access
bash
# Langsung buka setelah server running:
# 1. http://127.0.0.1:8000/warga/    ← UTAMA
# 2. http://127.0.0.1:8000/admin/   ← ADMIN
🎮 Coba Fitur
Lihat Data → Buka /warga/

Login Admin → Buka /admin/ (butuh superuser)

Tambah Data → Via admin panel

Lihat Detail → Melalui interface admin

📋 Tentang Project
Project ini dikembangkan menggunakan Django framework dengan arsitektur MVT (Model-View-Template). Aplikasi ini memungkinkan pengelolaan data warga secara digital dengan antarmuka yang user-friendly.

🛠️ Fitur Utama
✅ Management data warga (NIK, nama, alamat, kontak)

✅ Interface admin untuk kelola data

✅ Tampilan daftar warga yang terstruktur

✅ Sistem pencatatan tanggal registrasi otomatis

💻 Teknologi yang Digunakan
Backend: Django 4.2+

Database: SQLite

Frontend: HTML, CSS

Architecture: Class-Based Views

📥 Instalasi & Menjalankan
Requirements
Python 3.8 atau lebih tinggi

Django framework

Langkah Instalasi
bash
# Clone repository
git clone https://github.com/fazyraww/django-kelurahan.git

# Masuk direktori project
cd django-kelurahan

# Install Django
pip install django

# Setup database
python manage.py migrate

# Buat superuser (untuk akses admin)
python manage.py createsuperuser

# Jalankan server
python manage.py runserver
