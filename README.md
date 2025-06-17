# 🗑️ Google Calendar Cleanup

A Python CLI tool to **bulk delete Google Calendar events** by title. Perfect for cleaning up mistakenly imported `.ics` files that created many duplicate one-time events instead of a repeating series.

---

## 📌 Features

- 🔎 Deletes all Google Calendar events matching a given title (e.g. `"PAL-LAAS biweekly"`)
- 📅 Works on future events by default, with optional support for past events
- 🔐 Uses Google's official Calendar API with OAuth2
- 🧪 Virtualenv isolation with [Poetry](https://python-poetry.org/)
- 💡 CLI interface: `poetry run cleanup --title "XYZ"`

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/google-calendar-cleanup.git
cd google-calendar-cleanup
```

### 2. Install dependencies using Poetry

If Poetry is not installed:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Then:

```bash
poetry install
```

---

## 🔐 Setting Up Google Calendar API Credentials

To use the script, you need OAuth credentials from Google:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project (or select an existing one).
3. In the left menu, go to: **APIs & Services → Library**
4. Search for and **enable** the **Google Calendar API**.
5. Go to **APIs & Services → Credentials**.
6. Click **"+ Create Credentials" → OAuth client ID**
   - If prompted, configure the OAuth consent screen:
     - User type: `External`
     - App name: e.g., `Calendar Cleanup`
     - Support email and developer contact email: your email
     - Click through and **Publish** the app
   - Choose **Application type**: `Desktop App`
   - Name it (e.g., `CalendarCleaner`)
7. After creating the OAuth client, click **Download JSON**.
8. Save this file as `credentials.json` in the **root of the project** (same directory as `pyproject.toml`).

---

## ▶️ Usage

### Run the CLI tool:

```bash
poetry run cleanup --title "PAL-LAAS biweekly"
```

You will be prompted to authenticate your Google account in the browser. A `token.pickle` file will be saved for future runs.

### Include past events as well:

```bash
poetry run cleanup --title "PAL-LAAS biweekly" --include-past
```

---

## ⚠️ Important Notes

- This tool **only deletes events with the exact title** you provide (case-sensitive).
- It works on your **primary calendar** by default.
- Only **single (non-recurring)** events are currently supported.
- Your authorization tokens are saved in `token.pickle` and reused unless expired.

---

## 🧪 Development & Code Style

Use the following tools to keep code clean:

```bash
poetry run black .
poetry run isort .
poetry run flake8
```

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for full details.

---

## 🙏 Acknowledgments

- [Google Calendar API](https://developers.google.com/calendar)
- [Poetry](https://python-poetry.org/)
- [google-api-python-client](https://github.com/googleapis/google-api-python-client)
