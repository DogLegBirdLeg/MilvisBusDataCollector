from data import schedules as schedules
import time
from datetime import datetime
from logic.schedule_finder import producer


def run():
    while True:
        current_time = datetime.now()
        schedule = schedules.get(current_time.strftime('%H:%M'))
        if schedule is not None:
            print(f"============schedule({schedule}) push ===============")
            producer.call_producer(schedule)
        time.sleep(60)


if __name__ == '__main__':
    run()
