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
- **Python** 3.8+  
- **Django** 4.2+  
- **SQLite** (default, mudah diganti ke database lain)  
- **Class-Based Views (CBV)**  

---

## 🚀 Cara Menjalankan

1. **Clone repository** (atau download ZIP):
```bash
git clone https://github.com/USERNAME/aplikasi-kelurahan.git
cd aplikasi-kelurahan
Install dependencies:

bash
Copy code
pip install django
Setup database:

bash
Copy code
python manage.py migrate
Jalankan server:

bash
Copy code
python manage.py runserver
Akses aplikasi di browser:

Daftar warga: http://127.0.0.1:8000/warga/

Admin panel: http://127.0.0.1:8000/admin/
