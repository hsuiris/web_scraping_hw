import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# 建立瀏覽器（含反偵測設定），回傳 driver
def setup_driver():
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")
    return webdriver.Chrome(options=options)

# 開網站 → 點すぐに読む → 切換視窗 → 點立即閱讀
def open_manga_reader(driver, url):
    driver.get(url)
    button = driver.find_element(By.CSS_SELECTOR, 'button.open-viewer.book-begin.ga')
    button.click()
    driver.switch_to.window(driver.window_handles[-1])
    driver.find_element(By.PARTIAL_LINK_TEXT, 'すぐに読む').click()

# 截圖+翻頁直到最後一頁
def scrape_manga(driver, output_folder="downloaded_manga"):
    wait_element = WebDriverWait(driver, 10)
    total_image_count = 0
    os.makedirs(output_folder, exist_ok=True)

    while True:
        image_elements = driver.find_elements(By.CSS_SELECTOR, 'div.page_image img.image')

        for img_element in image_elements:
            if img_element.is_displayed():
                file_path = os.path.join(output_folder, f"manga_page_{total_image_count}.png")
                img_element.screenshot(file_path)
                print(f"成功擷取頁面並儲存為: {file_path}")
                total_image_count += 1

        try:
            next_page = wait_element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.flip.flip-left')))
            next_page.click()
            print("已點擊下一頁，等待畫面載入...")
            time.sleep(2)

        except TimeoutException:
            print("【系統提示】找不到下一頁按鈕，已達最後一頁，結束爬取迴圈。")
            break


def main(url):
    driver = setup_driver()
    try:
        open_manga_reader(driver, url)
        scrape_manga(driver)
    finally:
        driver.quit()


if __name__ == "__main__":
    main("https://www.mangaz.com/book/detail/157901")
