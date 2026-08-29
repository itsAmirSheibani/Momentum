# Momentum

I built Momentum as a personal project to put what I learned about Django into practice and create something I could actually use in my daily life.

Instead of making another simple to-do list, I wanted to bring everyday planning into one place: tasks, goals, journaling, mood tracking, and personal finances.

---

## Features

### Authentication
- User registration
- User login and logout
- Password change
- Custom user model with email-based authentication

### Dashboard
- Today's tasks and completion progress
- Daily mood and energy level
- Today's reflections
- Upcoming goals with progress indicators
- Monthly financial summary

### Tasks
- Create, edit, and delete tasks
- Mark tasks as complete or incomplete
- Set priority: High / Medium / Low
- Add descriptions and categories
- Set due dates and times
- Filter tasks by status: All / Active / Completed

### Journal
- Add multiple reflections per day
- View today's reflections
- Browse previous entries

### Mood Tracking
- Record daily mood:
  - Great
  - Good
  - Okay
  - Low
  - Bad
- Track energy level from 1 to 10

### Goals
- Create, edit, and delete goals
- Set target dates
- Track progress from 0% to 100%
- Visual progress indicators

### Finance
- Record income and expenses
- View monthly income, expenses, and balance
- Browse transaction history

### Settings
- Update profile information
- Change password
- Logout

### Admin Panel
- Django admin interface for managing users and application data

---

## Tech Stack

| Layer | Technology |
| --- | --- |
| Backend | Python, Django 5.2 |
| Database | SQLite |
| Authentication | Custom Django User Model |
| Forms | Django Forms, ModelForms |
| Frontend | HTML, CSS, Vanilla JavaScript |
| Containerization | Docker, Docker Compose |

---

## Project Structure

```text
Momentum/
├── accounts/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── dashbord/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── static/
│       └── accounts/
│           ├── momentum-auth.css  
│           └── momentum-auth.js
        └── dashbord/
│           ├── css/
│           │   └── style.css
│           ├── js/
│           │   └── app.js
│           └── img/
│               └── favicon.svg
│
├── Momentum/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   ├── dashboard.html
│   ├── tasks.html
│   ├── journal.html
│   ├── goals.html
│   ├── finance.html
│   ├── settings.html
│   ├── add.html
│   ├── edit.html
│   └── accounts/
│       ├── login.html
│       ├── logout.html
│       └── signup.html
│
├── Dockerfile
├── compose.yaml
├── requirements.txt
├── manage.py
├── .gitignore
└── README.md

## Getting Started

### Local Development
```
#### 1. Clone the repository

```bash
git clone https://github.com/itsAmirSheibani/Momentum.git
cd Momentum
```

#### 2. Create a virtual environment

```bash
python -m venv venv
```

#### 3. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

#### 4. Install dependencies

```bash
pip install -r requirements.txt
```

#### 5. Apply migrations

```bash
python manage.py migrate
```

#### 6. Create a superuser

```bash
python manage.py createsuperuser
```

#### 7. Run the development server

```bash
python manage.py runserver
```

Open the application at:

```text
http://127.0.0.1:8000/
```

---

## Docker

Momentum also includes Docker support.

### Build and run

```bash
docker compose up --build
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

### Run Django management commands inside the container

```bash
docker compose exec python manage.py migrate
```

```bash
docker compose exec python manage.py makemigrations
```

```bash
docker compose exec python manage.py createsuperuser
```

### Stop the containers

```bash
docker compose down
```

---

## Django Concepts Practiced

Building Momentum gave me practical experience with:

- Django project and app structure
- URL routing
- Function-based views
- Templates and template context
- Django models and relationships
- `ForeignKey`
- QuerySets and Django ORM
- Forms and ModelForms
- Form validation
- CRUD operations
- Django authentication
- Custom User models
- `request.user`
- User-owned data and permissions
- Django admin
- Static files
- Migrations
- Deployment configuration
- Docker and Docker Compose

---

## Author

**Amir Sheibani**

- GitHub: https://github.com/itsAmirSheibani
- LinkedIn: https://www.linkedin.com/in/itsamirsheibani
