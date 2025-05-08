import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

def get_data(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    results = []

    listings = soup.select('.content-item')  # chọn thẻ chứa tin
    for listing in listings:
        title = listing.select_one('h3 a')
        description = listing.select_one('.content p')
        address = listing.select_one('.ctdt span')
        area_price = listing.select_one('.price')

        results.append({
            "Tiêu đề": title.text.strip() if title else '',
            "Mô tả": description.text.strip() if description else '',
            "Địa chỉ": address.text.strip() if address else '',
            "Diện tích": area_price.text.split('-')[0].strip() if area_price else '',
            "Giá": area_price.text.split('-')[-1].strip() if area_price else ''
        })
    return results

def crawl_all_pages(base_url, max_pages=5):
    all_data = []
    for page in range(1, max_pages + 1):
        url = f"{base_url}/p{page}.htm"
        print(f"Đang xử lý: {url}")
        all_data.extend(get_data(url))
    return all_data

def save_to_csv(data):
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join("data", "listings.csv")
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False, encoding='utf-8-sig')
    print(f"Đã lưu {len(data)} dòng vào {file_path}")

if __name__ == "__main__":
    # Ví dụ: căn hộ chung cư tại Hà Nội
    url = "https://alonhadat.com.vn/nha-dat/can-ban/can-ho-chung-cu/ha-noi"
    data = crawl_all_pages(url)
    save_to_csv(data)
