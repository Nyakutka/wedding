# nikt-wedding — сайт‑приглашение Никита & Кира

Проект хранит минимальный Flask‑сайт‑приглашение с деталями, вишлистом и формой RSVP.

Как запустить в devcontainer / локально

1. Откройте проект в VS Code devcontainer (Ubuntu) и откройте терминал внутри контейнера.
2. Создайте виртуальное окружение и установите зависимости:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Запуск приложения:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000
```

Откройте в браузере: http://localhost:5000

Файлы

- `app.py` — Flask-приложение (маршруты: /, /details, /rsvp, /thankyou).
- `templates/` — Jinja2 шаблоны.
- `static/` — стили.
- `data/` — сохраняются RSVP (создаётся при первом запуске).

Деплой: gunicorn + nginx + systemd, обязательно HTTPS для публичного хоста.
