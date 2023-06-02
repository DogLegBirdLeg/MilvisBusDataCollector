from data import schedules, schedules_holiday
import time
from datetime import datetime
from logic.schedule_finder import producer
from util.holiday_checker import is_holiday


def run():
    while True:
        current_time = datetime.now()
        schedule = get_schedule(current_time)

        if schedule is not None:
            print(f"============schedule({schedule}) push ===============")
            producer.call_producer(schedule)
        time.sleep(60)


def get_schedule(current_time):
    if is_holiday(current_time):
        return schedules_holiday.get(current_time.strftime('%H:%M'))
    return schedules.get(current_time.strftime('%H:%M'))


if __name__ == '__main__':
    run()
