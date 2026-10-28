# VUB Events

A Web application for discovering, creating and sharing events at and around VUB.
Group project for the course **Web Technologies** (VUB, 2026–2027).

## Team

| Name | GitHub |
|------|--------|
| Timour Theunissen | [@Timourrr](https://github.com/Timourrr) |
| Yeno Ghijselings | @yenogh |
| Happy De-Benoit Bikorimana | @happybikorimana |
| Helena Hedbrant | @Lingonnet |

## Tech stack

- **Backend:** Django (Python)
- **Database:** PostgreSQL
- **Map:** Unknown
- **Styling:** CSS

## Requirements

- Python **3.12+**
- Git
- Docker (for DB so not yet needed)

## Setup

### 1. Clone the repository
If you have ssh setup:
```bash
git clone git@github.com:Timourrr/Webtech_VUB_events.git
cd Webtech_VUB_events
```
If not:
```bash
git clone https://github.com/Timourrr/Webtech_VUB_events.git
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
If you are using powershell on windows
```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

Your prompt should now start with `(venv)`.
Use AI if you get errors they are good at solving them
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

## Everyday Workflow
Every time you want to add a feature make a new branch. This is the easiest way to stay organised.
- Create a branch for every task:
  - `feature/<name>` for new functionality
  - `fix/<name>` for bug fixes
  - `docs/<name>` for documentation
```bash
git switch main
git pull
git switch -c feature/my-feature
```
After this you can just open it in any IDE.
- To see your changes on the website you can do the following
```bash
cd Webtech_VUB_events
source venv/bin/activate          # prompt shows (venv)
python manage.py runserver
```
And then just open <http://127.0.0.1:8000>.

If you are done for the day just commit by doing:
```bash
git status                       # check what changed
git add .                        # stage all changes
git commit -m "Add event list page"  # please give a useful name
git push origin <branch-name>    # push to GitHub
```
If you finished your feature open a pull request. This will merge your code to the main branch.
Try to not work on the same parts of the website in different branches this will cause merge conflicts.

If you start working on something again always first pull the up to date code with git pull.
- After every `git pull`, run:
  ```bash
  pip install -r requirements.txt
  python manage.py migrate
  ```

- **Log your hours** in the shared time sheet on the same day you worked. 
- https://docs.google.com/spreadsheets/d/1l63NvNomHOt0NzRcwLW-7G321yMWOKWz/edit?usp=sharing&ouid=113428561195025500800&rtpof=true&sd=tru
- YouTube tutorial for Django: https://www.youtube.com/watch?v=nGIg40xs9e4&t
  - This will of course not teach you everything but w3schools also has tutorials.

Any question contact AI first, if that doesn't work then me.
