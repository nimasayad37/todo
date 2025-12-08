import schedule
import time
from .autoclose_overdue import autoclose_overdue

def run_schedular(interval_seconds: int = 60):
    schedule.every(interval_seconds).seconds.do(autoclose_overdue)
    print("Running scheduled overdue-closing job...")
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("schedular stopped")
    if __name__ == "__main__":
        run_schedular(60)