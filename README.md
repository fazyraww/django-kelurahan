# Aplikasi Data Warga Kelurahan

Aplikasi manajemen data warga berbasis **Django** dengan **Class-Based Views (CBV)**.  
Dibuat sebagai proyek tugas kuliah, tapi dikemas dengan struktur profesional dan clean code.

---

## ✨ Fitur Utama
- ✅ Model **Warga** lengkap (NIK, Nama, Alamat, Telepon)  
- ✅ Admin Django untuk manajemen data cepat  
- ✅ **Class-Based Views** untuk tampilan daftar warga  
- ✅ Template rapi untuk menampilkan daftar warga   

---

## 🛠️ Teknologi
- Python 3.8+  
- Django 4.2+  
- SQLite (default, mudah diganti ke database lain)  
- Class-Based Views (CBV)  

---

## 🚀 Cara Menjalankan
1. Install dependencies:
```bash
pip install django
Setup database:

bash
Copy code
python manage.py migrate
Jalankan server:

bash
Copy code
python manage.py runserver
Buka di browser:

Daftar warga: http://127.0.0.1:8000/warga/

Admin panel: http://127.0.0.1:8000/admin/
