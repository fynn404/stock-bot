from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from core.generate_plot import plot_fear_greed_colored
from core.send_email import send_email_with_plot
from config import SCHEDULE_HOUR, SCHEDULE_MINUTE

def job():
    print(f"[{datetime.now().isoformat()}] Starting daily job...")
    plot_fear_greed_colored()
    send_email_with_plot()
    print(f"[{datetime.now().isoformat()}] Job completed.")

def start_scheduler():
    scheduler = BlockingScheduler(timezone="Asia/Shanghai")
    scheduler.add_job(job, 'cron', hour=SCHEDULE_HOUR, minute=SCHEDULE_MINUTE)
    print("[INFO] Scheduler started. Waiting for jobs...")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("[INFO] Scheduler stopped.")

if __name__ == "__main__":
    start_scheduler()
