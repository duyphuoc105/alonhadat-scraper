import schedule
import time
import subprocess
from datetime import datetime

def job():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] Đang chạy scraper.py...")

    try:
        result = subprocess.run(["python", "scraper.py"], check=True)
        print(f"[{now}] scraper.py đã chạy xong.")
    except subprocess.CalledProcessError as e:
        print(f"[{now}] Lỗi khi chạy scraper.py: {e}")


schedule.every().day.at("06:00").do(job)

print("Đang chạy lập lịch. Nhấn Ctrl+C để dừng.")
while True:
    schedule.run_pending()
    time.sleep(60)
