from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from datetime import datetime, timezone

SCOPES = ['https://www.googleapis.com/auth/calendar']


def delete_pal_laas_biweekly_events():
    creds = None
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)

    service = build('calendar', 'v3', credentials=creds)

    # Adjust time range to search (e.g., the next year)
    time_min = datetime.now(timezone.utc).isoformat()
    events_result = service.events().list(
        calendarId='primary',
        timeMin=time_min,
        maxResults=2500,
        singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])

    for event in events:
        if event.get('summary') == 'PAL-LAAS biweekly':
            print(
                f"Deleting: {event['summary']} at {event['start'].get('dateTime', event['start'].get('date'))}")
            service.events().delete(calendarId='primary',
                                    eventId=event['id']).execute()


def main():
    delete_pal_laas_biweekly_events()


if __name__ == '__main__':
    main()
