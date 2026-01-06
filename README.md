# 🏡 Django Kelurahan

**Aplikasi backend berbasis Django untuk manajemen data kelurahan dan warga** — dirancang rapi, mudah dikembangkan, dan siap dijadikan fondasi proyek administrasi wilayah.

---

## ✨ Ringkasan

`django-kelurahan` adalah proyek **Django** yang menyediakan fitur **CRUD** (Create, Read, Update, Delete) untuk mengelola data **kelurahan** dan **warga**. Cocok untuk:

* Latihan backend Python/Django
* Dasar sistem administrasi wilayah
* Boilerplate proyek akademik atau internal

---

## 🧠 Fitur Utama

* ✔️ CRUD data kelurahan
* ✔️ CRUD data warga
* ✔️ Struktur project Django yang bersih & modular
* ✔️ Mudah dikustomisasi (database, app, dan logic)
* ✔️ Dependency management dengan `requirements.txt`

---

## ⚙️ Teknologi

* **Python**
* **Django**
* **SQLite** (default — dapat diganti PostgreSQL/MySQL)
* **Django Template** (jika ada tampilan)

---

## 🚀 Instalasi & Menjalankan Project

Ikuti langkah berikut untuk menjalankan proyek secara lokal:

### 1️⃣ Clone Repository

```bash
git clone https://github.com/fazyraww/django-kelurahan.git
cd django-kelurahan
```

### 2️⃣ Buat Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
pip install django-cors-headers
```

### 4️⃣ Migrasi Database

```bash
python manage.py makemigrations
python manage.py migrate

``` bash
python manage.py createsuperuser

### 5️⃣ Jalankan Server

```bash
python manage.py runserver
```

Buka browser dan akses:

```
http://127.0.0.1:8000/
```

---

## 📂 Struktur Project

```text
django-kelurahan/
├── data_kelurahan/        # App pengelolaan kelurahan
├── warga/                 # App pengelolaan warga
├── manage.py              # Django CLI entry point
├── requirements.txt       # Dependency Python
└── README.md              # Dokumentasi project

