# 📋 Django Todo List Application

A modern and responsive **Todo List Web Application** built using **Django**, **MySQL**, **Bootstrap 5**, **HTML**, **CSS**, and **JavaScript**. The application helps users organize daily tasks with features like task creation, editing, deletion, completion tracking, search, and progress monitoring.

---

## 📸 Project Preview

> Add screenshots of your project here.

### Dashboard

![Dashboard](screenshots/dashboard.png)

### Add Task

![Add Task](screenshots/add-task.png)

### Progress Tracking

![Progress](screenshots/progress.png)

---

# 🚀 Features

- ✅ Add New Tasks
- ✏️ Edit Existing Tasks
- 🗑️ Delete Tasks
- ✔️ Mark Tasks as Completed
- 📊 Dynamic Progress Bar
- 📈 Task Statistics
- 🔍 Search Tasks
- 📅 Current Date Display
- 💾 MySQL Database Storage
- 🎨 Responsive Bootstrap UI
- 📱 Mobile Friendly Design

---

# 🛠️ Tech Stack

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

## Backend

- Python 3.11
- Django 5

## Database

- MySQL

## Tools

- VS Code
- Git
- GitHub
- MySQL Workbench

---

# 📂 Project Structure

```text
todo_project/
│
├── todo/
│   ├── migrations/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│
├── todo_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── media/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/django-todo-app.git
```

```bash
cd django-todo-app
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

### Linux

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄️ Configure MySQL

Create a database.

```sql
CREATE DATABASE todo_db;
```

Update **settings.py**

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "todo_db",
        "USER": "root",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

---

# 🔄 Apply Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

# 👤 Create Superuser

```bash
python manage.py createsuperuser
```

---

# ▶️ Run Server

```bash
python manage.py runserver
```

Open your browser:

```
http://127.0.0.1:8000/
```

Admin Panel:

```
http://127.0.0.1:8000/admin/
```

---

# 📊 Database Model

| Field | Type |
|-------|------|
| Title | CharField |
| Description | TextField |
| Category | CharField |
| Emoji | CharField |
| Time | TimeField |
| Completed | BooleanField |
| Created At | DateTimeField |

---

# 📸 Screenshots

Add your screenshots inside a folder named:

```text
screenshots/
```

Example:

```
dashboard.png
add-task.png
edit-task.png
delete-task.png
progress.png
```

---

# 🌟 Future Improvements

- User Authentication
- Due Dates
- Task Priorities
- Categories
- Dark Mode
- AJAX CRUD
- Email Notifications
- Drag & Drop Task Sorting
- Docker Support
- AWS EC2 Deployment
- CI/CD Pipeline using GitHub Actions

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Add new feature"
```

4. Push

```bash
git push origin feature-name
```

5. Create a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Harish Raj S**

- GitHub: https://github.com/harishsubburaj
- LinkedIn: https://www.linkedin.com/in/harishsubburaj/

---

⭐ If you found this project helpful, please consider giving it a Star on GitHub!