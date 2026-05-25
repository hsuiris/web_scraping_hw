import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from assignment01_scraper import scrape_manga

# Step 1：建立 Options 物件（反偵測設定）
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")

# 初始化 WebDriver（含反偵測設定）
driver = webdriver.Chrome(options=options)

# Step 2：開啟目標網站
driver.get("https://www.mangaz.com/book/detail/157901")

# Step 3：使用 CSS_SELECTOR 定位「免費閱讀」按鈕並點擊
button = driver.find_element(By.CSS_SELECTOR, 'button.open-viewer.book-begin.ga')
button.click()

# Step 4：切換到新開啟的視窗
driver.switch_to.window(driver.window_handles[-1])

# Step 5：點擊「すぐに読む（立即閱讀）」連結
driver.find_element(By.PARTIAL_LINK_TEXT, 'すぐに読む').click()

# Step 6：開始爬取漫畫圖片（截圖迴圈）
scrape_manga(driver)

# Step 7：關閉 WebDriver
driver.quit()