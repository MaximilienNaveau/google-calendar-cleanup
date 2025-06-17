# 🗑️ Google Calendar Cleanup

A Python utility to **bulk delete Google Calendar events** with a specific name. Useful for cleaning up wrongly imported events (e.g. non-repeating duplicates from .ics files).

---

## 📌 Features

- Deletes all future events with the title `"PAL-LAAS biweekly"` from your **primary Google Calendar**.
- Uses the **Google Calendar API** with OAuth2 authentication.
- Isolated environment using **Poetry**.
- Safe, transparent deletions (shows event date/time as it's deleted).

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/google-calendar-cleanup.git
cd google-calendar-cleanup
```

### 2. Install dependencies using Poetry

If Poetry isn't installed yet:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Then:

```bash
poetry install
poetry shell
```

---

## 🔐 Setup Google Calendar API

1. Visit [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project (or use an existing one).
3. Enable **Google Calendar API** for that project.
4. Go to **APIs & Services → Credentials**.
5. Create **OAuth client ID** credentials:
    - Application type: **Desktop app**
6. Download the `credentials.json` file.
7. Place `credentials.json` in the project root.

---

## ▶️ Usage

Once inside the Poetry shell:

```bash
python google_calendar_cleanup/cleanup.py
```

You will be prompted to authorize access via a browser. After you approve, the script will:

- Fetch all upcoming events from your calendar.
- Delete only those named `"PAL-LAAS biweekly"`.

---

## ⚠️ Disclaimer

- This script only deletes events named `"PAL-LAAS biweekly"`.
- It does not affect other events or recurring events created properly.
- Always **review your credentials and access scopes** before running scripts that modify calendar data.

---

## 🧪 Development & Code Style

Use the following tools for code formatting and linting:

```bash
poetry run black .
poetry run isort .
poetry run flake8
```

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- [Google Calendar API Docs](https://developers.google.com/calendar)
- [Poetry](https://python-poetry.org/)
