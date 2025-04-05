# Code Citations

## License: unknown

https://github.com/RobinStGeorges/SocialPlanningWeb/tree/a82e4ba165c0a6ed2024d346dca24b0066448208/app.py

```
Z' indicates UTC time
    events_result = service.events().list(
        calendarId='primary', timeMin=now,
        maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', []
```

## License: Apache_2_0

https://github.com/NishanthSingaraju/BioHack/tree/08772e88683b3a10d4af859af7e8e718f9f51ec0/backend/calendar_api.py

```
service.events().list(
        calendarId='primary', timeMin=now,
        maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        logging.
```

