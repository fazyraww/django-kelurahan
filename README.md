# 🏠 Aplikasi Data Warga Kelurahan

Aplikasi **manajemen data warga** berbasis **Django** menggunakan **Class-Based Views (CBV)**.  
Dibuat sebagai proyek tugas kuliah, namun dirancang dengan struktur **clean code** dan **best practices Django**.

---

## ✨ Fitur Utama
| Fitur | Deskripsi |
|-------|-----------|
| ✅ Model Warga | Field lengkap: NIK, Nama, Alamat, Telepon |
| ✅ Admin Django | Manajemen data cepat dan mudah |
| ✅ Class-Based Views | Tampilan daftar warga yang terstruktur |
| ✅ Template Responsive | Tampilan daftar warga yang rapi dan user-friendly |

---

## 🛠️ Teknologi

- `🐍 Python` 3.8+  
- `🌐 Django` 4.2+  
- `💾 SQLite` (default, mudah diganti ke database lain)  
- `🏗️ Class-Based Views (CBV)`  

---

🚀 Cara Menjalankan Aplikasi

```bash
# Clone repository & masuk ke folder
git clone https://github.com/fazyraww/django-kelurahan.git
cd aplikasi-kelurahan

# Install dependencies
pip install django

# Setup database & jalankan server
python manage.py migrate
python manage.py runserver

# Akses aplikasi di browser
Daftar warga: http://127.0.0.1:8000/warga/
Admin panel: http://127.0.0.1:8000/admin/
```


