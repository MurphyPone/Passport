# sandbox for playing with time confs
from datetime import datetime 
from datetime import timezone

SCHEDULE = {
    "Intro to Python": {
        "start_time": datetime(2020, 11, 5, 12, tzinfo=timezone.utc),
        "duration": "1 hour",
        "attended": False  
    },
    "Intermediate Python": {
        "start_time": datetime(2020, 11, 5, 14, tzinfo=timezone.utc),
        "duration": "1 hour",
        "attended": False  
    }
}

print(SCHEDULE['Intermediate Python']['start_time'] - SCHEDULE['Intro to Python']['start_time'])