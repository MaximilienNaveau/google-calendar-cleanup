import argparse
import os.path
import pickle
from datetime import datetime, timezone

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying scopes, delete the token.pickle file
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def get_service():
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return build("calendar", "v3", credentials=creds)


def delete_events_by_title(service, title: str, include_past: bool):
    now = datetime.now(timezone.utc).isoformat()
    print(f"Fetching events after {now} with title '{title}'...")

    params = {
        "calendarId": "primary",
        "maxResults": 2500,
        "singleEvents": True,
        "orderBy": "startTime",
    }
    if not include_past:
        params["timeMin"] = datetime.now(timezone.utc).isoformat()
    events_result = service.events().list(**params).execute()
    events = events_result.get("items", [])

    deleted = 0
    for event in events:
        if event.get("summary") == title:
            print(
                f"Deleting: {event['summary']} at {event['start'].get('dateTime', event['start'].get('date'))}"
            )
            service.events().delete(calendarId="primary", eventId=event["id"]).execute()
            deleted += 1

    print(f"Deleted {deleted} event(s).")


def main():
    parser = argparse.ArgumentParser(
        description="Delete Google Calendar events by title"
    )
    parser.add_argument(
        "--title", required=True, help="Exact title of events to delete"
    )
    parser.add_argument(
        "--include-past", action="store_true", help="Include past events"
    )
    args = parser.parse_args()

    service = get_service()
    delete_events_by_title(service, args.title, args.include_past)
