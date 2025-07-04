from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from core.generate_plot import plot_fear_greed_colored
from core.send_email import send_email_with_plot

def job():
    print(f"[{datetime.now().isoformat()}] Starting daily job...")
    plot_fear_greed_colored()
    send_email_with_plot()
    print(f"[{datetime.now().isoformat()}] Job completed.")

def start_scheduler():
    scheduler = BlockingScheduler(timezone="Asia/Shanghai")  # 或改为你所在的时区
    scheduler.add_job(job, 'cron', hour=8, minute=0)  # 每天早上8点执行
    print("[INFO] Scheduler started. Waiting for jobs...")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("[INFO] Scheduler stopped.")

if __name__ == "__main__":
    start_scheduler()
