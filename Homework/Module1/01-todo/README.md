# Django TODO App (01-todo)

This is a minimal Django project implementing a TODO app with create, edit, delete, due dates, and a resolved flag.

Quick start:

1. Create a virtual environment and activate it:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Apply migrations:

```bash
python manage.py migrate
```

4. Create a superuser (optional, to access admin):

```bash
python manage.py createsuperuser
```

5. Run the development server:

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` to view the TODO list.
