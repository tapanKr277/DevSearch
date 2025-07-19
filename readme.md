# 🧠 DevSearch

A full-stack portfolio and project collaboration platform for developers. Users can showcase projects, vote, review, and connect with others in the community.

---

## 📌 Features

- 🧑 User registration and login
- 🔐 Profile management
- 📝 Project creation and tagging
- ⭐ Upvote/downvote system
- 💬 Review system (one review per user per project)
- 🔍 Search projects by title, tag, or owner
- 📩 Messaging between users

---

## 🛠️ Tech Stack

**Backend:**
- Python 3.x
- Django
- Django REST Framework
- SQLite (for dev)
- UUID for unique identification

**Frontend (if applicable):**
- HTML/CSS with Django templates (or React for API use)

**Other:**
- Django Signals
- Image uploads
- Faker (for seed data)
- CORS headers

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/DevSearch.git
cd DevSearch
```

2. Create and Activate Virtual Environment

python -m venv env
source env/bin/activate   # On Windows use: env\Scripts\activate

3. Install Requirements
   
pip install -r requirements.txt

5. Setup Environment Variables

SECRET_KEY=your-django-secret-key
DEBUG=True
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_password

5. Apply Migrations

python manage.py makemigrations
python manage.py migrate

6. Create Superuser (for admin panel)

python manage.py createsuperuser

7. Seed the Database (Optional)

python populate.py

8. Run the Server

python manage.py runserver

Then visit: http://127.0.0.1:8000

🔒 Admin Panel
Access the Django admin panel at:

http://127.0.0.1:8000/admin

Use the superuser credentials you created.

🧪 Sample Users (after seeding)
Email: fake@example.com

Password: password123

(Or check in Django admin after populate.py script)

✨ Credits
Built by Tapan Kumar
Reach me at: tapankr277@gmail.com
