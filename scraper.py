from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time


browser = webdriver.Chrome()
url = "https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/3/da-nang.html"
browser.get(url)


with open("listings.csv", mode="w", encoding="utf-8-sig", newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["Tiêu đề", "Mô tả", "Địa chỉ", "Diện tích", "Giá"])

    while True:
        try:
            
            WebDriverWait(browser, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "content-item"))
            )

            posts = browser.find_elements(By.CLASS_NAME, "content-item")
            print(f" Đang xử lý {len(posts)} tin đăng...")

            for post in posts:
                data = {}

                try:
                    data["title"] = post.find_element(By.CSS_SELECTOR, ".ct_title a").text.strip()
                except:
                    data["title"] = ""

                try:
                    data["desc"] = post.find_element(By.XPATH, ".//div[@class='content']/div[2]").text.strip()
                except:
                    data["desc"] = ""

                try:
                    data["address"] = post.find_element(By.CLASS_NAME, "address").text.strip()
                except:
                    data["address"] = ""

                try:
                    data["area"] = post.find_element(By.CLASS_NAME, "ct_dt").text.strip()
                except:
                    data["area"] = ""

                try:
                    data["price"] = post.find_element(By.CLASS_NAME, "price").text.strip()
                except:
                    data["price"] = ""

                csv_writer.writerow([data["title"], data["desc"], data["address"], data["area"], data["price"]])

            
            try:
                next_page = browser.find_element(By.LINK_TEXT, "›")
                next_page.click()
                time.sleep(2)
            except:
                print(" Đã tới trang cuối cùng.")
                break

        except Exception as err:
            print(f" Có lỗi xảy ra: {err}")
            break


browser.quit()
print(" Dữ liệu đã được ghi vào file listings.csv")
