# Django Game Leaderboard API
A REST API for Pygame game "Falling Star".
It saves player scores and return the Top 10 leaderboard.

## Features
- **POST**`/api/scores/` - Submit a new score
- **GET**`/api/scores/` - Get Top 10 leaderboard
- Build with Django REST Framework
- SQLite Database

## Tech Stack
`Python 3.14`|`Django`|`Django REST Framework` |`SQLite`| `PythonAnywhere`

## How to Run Locally
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
