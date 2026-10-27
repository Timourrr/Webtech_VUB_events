# VUB Events

A Web application for discovering, creating and sharing events at and around VUB.
Group project for the course **Web Technologies** (VUB, 2026–2027).

## Team

| Name | GitHub |
|------|--------|
| Timour Theunissen | [@Timourrr](https://github.com/Timourrr) |
| _Member 2_ | _@username_ |
| _Member 3_ | _@username_ |
| _Member 4_ | _@username_ |

## Tech stack

- **Backend:** Django (Python)
- **Database:** PostgreSQL
- **API:** Django REST Framework
- **Map:**
- **Styling:** CSS / Sass

## Requirements

- Python **3.12+**
- Git
- Docker

## Setup

### 1. Clone the repository

```bash
git clone git@github.com:Timourrr/Webtech_VUB_events.git
cd Webtech_VUB_events
```

### 2. Create and activate a virtual environment

macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Your prompt should now start with `(venv)`.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

Open <http://127.0.0.1:8000>.

Stop the server with `Ctrl+C` and leave the virtual environment with `deactivate`.

## Workflow

- **Never push directly to `main`.** It is protected.
- Create a branch for every task:
  - `feature/<name>` for new functionality
  - `fix/<name>` for bug fixes
  - `docs/<name>` for documentation
- Open a **pull request**. It needs **1 approval** from a teammate before merging.
- After every `git pull`, run:
  ```bash
  pip install -r requirements.txt
  python manage.py migrate
  ```
- Installed a new package? Update the requirements file and commit it:
  ```bash
  pip freeze > requirements.txt
  ```
- **Log your hours** in the shared time sheet on the same day you worked. 
- https://docs.google.com/spreadsheets/d/1l63NvNomHOt0NzRcwLW-7G321yMWOKWz/edit?usp=sharing&ouid=113428561195025500800&rtpof=true&sd=true

## Project structure

```
Webtech_VUB_events/
├── config/            # Django project settings
├── manage.py          # Django command-line utility
├── requirements.txt   # Python dependencies
└── README.md
```
