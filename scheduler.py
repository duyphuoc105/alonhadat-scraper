import schedule
import time
import subprocess

def job():
    print("Chạy scraper.py...")
    subprocess.run(["python", "scraper.py"])

# Đặt lịch lúc 6:00 sáng mỗi ngày
schedule.every().day.at("06:00").do(job)

print("Đang chạy lập lịch. Nhấn Ctrl+C để dừng.")
while True:
    schedule.run_pending()
    time.sleep(60)
