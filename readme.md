# 🩺 Doctor Desk

**Doctor Desk** is a modern, full-featured medical record management system built with Django. It allows doctors to manage patients, prescriptions, medical reports, and health records with ease — all in one secure platform.

🔗 **Live Demo**: [doctor-desk-okum.onrender.com](https://doctor-desk-okum.onrender.com/)

---

## 🚀 Features

- ✅ Secure doctor login and dashboard
- 👥 Patient management with profile, contact info, and visit history
- 💊 Prescription creation, editing, and tracking
- 📁 Upload & manage medical reports and records
- 🔍 Patient search by name, phone, email, gender, etc.
- 📊 Organized, clean UI with Bootstrap 5 and Font Awesome
- 🗃️ PostgreSQL/MySQL compatible (Production-ready)
- ☁️ Deployed on Render | Can be deployed on Vercel, Heroku, etc.

---

## 🛠️ Tech Stack

- **Backend**: Django 5.x
- **Database**: PostgreSQL / Supabase / MySQL
- **Frontend**: HTML, CSS, Bootstrap 5, Font Awesome
- **Authentication**: Django auth system
- **Storage**: Media & static handling via Whitenoise / Supabase
- **Deployment**: Render (Live) | Optional: Vercel + Supabase

---

## 📷 Screenshots

- Dashbord ![alt text](<Screenshot 2025-06-02 184527.png>)
- Patient list ![alt text](<Screenshot 2025-06-02 185254.png>)
- Profile page ![alt text](<Screenshot 2025-06-02 185322.png>)


---

## 🧑‍💻 Getting Started (Local Setup)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Doctor-Desk.git
cd Doctor-Desk
```

### 2️⃣ Set Up Virtual Environment

```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root and add the following (replace with your actual values):

```
SECRET_KEY=your-django-secret-key
DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

AWS_ACCESS_KEY_ID=your_supabase_anon_key
AWS_SECRET_ACCESS_KEY=your_supabase_service_role_key
AWS_STORAGE_BUCKET_NAME=your_supabase_bucket
AWS_S3_ENDPOINT_URL=https://your-supabase-url/storage/v1/s3
```

### 5️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create Superuser (Optional, for admin access)

```bash
python manage.py createsuperuser
```

### 7️⃣ Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 8️⃣ Run the Development Server

```bash
python manage.py runserver
```

Visit [http://localhost:8000](http://localhost:8000) in your browser.

---

## 🚀 Deployment

- **Render**: Uses [Procfile](Procfile) and [requirements.txt](requirements.txt). Just connect your repo and deploy.
- **Vercel**: Uses [vercel.json](vercel.json) and [setup.sh](setup.sh) for build steps.
- **Supabase**: Used for S3-compatible media storage.

---

## 📂 Project Structure

```
doctor_desk/
├── doctor_desk/         # Django project settings
├── doctors/             # Doctor app
├── patients/            # Patient app
├── static/              # Static files
├── templates/           # Shared templates
├── media/               # Uploaded files (local dev)
├── requirements.txt
├── Procfile
├── setup.sh
├── vercel.json
└── ...
```

---

## 🙋‍♂️ Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License.

---

## ✨ Credits

- Developed by Md. Fizur Rahman Fahim
- Thanks to Django, Bootstrap, Font Awesome, and the open-source