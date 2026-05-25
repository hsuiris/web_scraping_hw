import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

"""
爬取漫畫圖片並儲存到指定資料夾。
    - driver: Selenium WebDriver 物件
    - output_folder: 儲存圖片的資料夾名稱 (預設為 "downloaded_manga")
"""
def scrape_manga(driver, output_folder="downloaded_manga"):
    # 建立顯式等待物件，設定最長等待時間為 10 秒
    wait_element = WebDriverWait(driver, 10)

    # 設定全域圖片計數器（初始值為 0）
    total_image_count = 0

    # 確保資料夾存在
    output_dir = os.path.join("..", output_folder)
    os.makedirs(output_dir, exist_ok=True)

    # 進入無窮迴圈
    while True:
        # ── 步驟 A：擷取當前頁面圖片 ──────────────────────────────────────────
        # 使用 find_elements 取得當前頁面所有符合條件的圖片元素
        image_elements = driver.find_elements(By.CSS_SELECTOR, 'div.page_image img.image')

        for img_element in image_elements:
            # 只處理目前畫面上「可見」的圖片，避免抓到隱藏元素
            if img_element.is_displayed():
                file_path = os.path.join(output_dir, f"manga_page_{total_image_count}.png")

                # 對該圖片元素截圖，並儲存到 file_path
                img_element.screenshot(file_path)
                print(f"成功擷取頁面並儲存為: {file_path}")

                # 每成功儲存一張圖，將計數器加 1
                total_image_count += 1

        # ── 步驟 B：嘗試尋找並點擊「下一頁」按鈕 ─────────────────────────────
        try:
            # 使用 wait_element.until(EC.element_to_be_clickable(...))
            next_page = wait_element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.flip.flip-left')))

            # 點擊下一頁按鈕
            next_page.click()

            print("已點擊下一頁，等待畫面載入...")

            # 點擊後強制等待 2 秒，確保 DOM 與圖片載入完成
            time.sleep(2)

        # ── 步驟 C：Break Condition ────────────────────────────────────────────
        except TimeoutException:
            # 等待超過 10 秒仍找不到下一頁按鈕 → 已到達最後一頁
            print("【系統提示】找不到下一頁按鈕，已達最後一頁，結束爬取迴圈。")
            break