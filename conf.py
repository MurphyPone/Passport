from datetime import datetime 
from datetime import timezone

DISCORD_KEY = "NzcxODcwMDc2MjY5ODg3NTA4.X5yaBg.b5t1dDGZAtnpsXu9jYphwgmo--I"
EVENT_NAME = "VTHacks 8"
TIMEZONE = "EST"
TIMEFMT = f'%-b %d %-I:%-M %p %Z' # TODO look into %z for timezone
FIREBASE_CONFIG = { 
    "apiKey": "AIzaSyCZu1LBPVWeCDACjNkpsYUN8BD6EVV0A2Q",
    "authDomain": "passport-1486a.firebaseapp.com",
    "databaseURL": "https://passport-1486a.firebaseio.com",
    "projectId": "passport-1486a",
    "storageBucket": "passport-1486a.appspot.com",
    "messagingSenderId": "191029995931",
    "appId": "1:191029995931:web:be1a8411996024b3a8993e",
    "measurementId": "G-659FV12QRL"
}

WORKSHOP_SCHEDULE = {
    "01 Intro to Python": {
        "start_time": datetime(2020, 11, 5, 12, 20).strftime(TIMEFMT),
        "duration": "1 hour",
        "attended": 'False'  
    },
    "02 Intermediate Python": {
        "start_time": datetime(2020, 11, 5, 12, 20).strftime(TIMEFMT),
        "duration": "1 hour",
        "attended": 'False'
    },
    "03 Advanced Python": {
        "start_time": datetime(2020, 11, 5, 12, 20).strftime(TIMEFMT),
        "duration": "1 hour",
        "attended": 'False'  
    },
    "04 MLH Bob Ross": {
        "start_time": datetime(2020, 11, 5, 12, 20).strftime(TIMEFMT),
        "duration": "1 hour",
        "attended": 'False'  
    },
    "05 MLH CTF": {
        "start_time": datetime(2020, 11, 5, 12, 20).strftime(TIMEFMT),
        "duration": "1 hour",
        "attended": 'False'  
    }
}

DEVPOST_URL = "https://vthacks7.devpost.com/"
RULES = f"""{EVENT_NAME} Rules:
1. No lying
2. No cheating
3. No violence
4. no tolerating those who do
5. give homage to Blahåj
"""

LIVESITE_URL = "https://uottahack.live"