from logic.schedule_finder.schedule_finder import get_schedule
from datetime import datetime


date = datetime.strptime('2023-06-05T07:18:00', '%Y-%m-%dT%H:%M:%S')
print(get_schedule(date))

