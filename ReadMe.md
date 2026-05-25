# Assignment 01: 動態網頁爬蟲實作 - マンガ図書館Z

## 🎯 任務說明

請修改並完成老師提供的範本檔 `Assignment01_動態爬蟲案例_mangaz_練習版`，實作一個動態爬蟲程式，將指定漫畫的圖片完整下載至本機端。

---

## 🏆 評分標準與要求

### ✅基礎目標 (80 分條件)
1. **使用 Selenium**：必須使用 Selenium 進行動態網頁資料爬取。
2. **完成程式碼填空**：修改並補齊 `Assignment01_動態爬蟲案例_mangaz_練習版` 中的程式碼。
3. **建立資料夾存檔**：程式執行時，必須能自動（或手動）新增一個資料夾，用以存放爬取下來的漫畫圖片。
4. **錄製執行結果影片**：
   * 錄製一段影片，展示您將下載下來的漫畫圖片以「投影片」或「圖片瀏覽器」方式播放的過程。
   * **不需要**展示程式碼，也**不需要**邊寫邊執行，只需展示最終下載成功的漫畫閱讀畫面。
   * 將影片上傳至 YouTube 或 Google Drive（請確認共用權限設定為「知道連結的人均可觀看」）。

### ✅進階目標 (100 分條件)
*必須先滿足所有 80 分條件，並追加以下要求：*

1. **程式碼模組化**：將老師提供的程式碼邏輯包裝成 `def` (函式)，並整理輸出為一個標準的 `.py` 檔案。
2. **專案結構要求**：使用 GitHub 平台來提交作業。您的 Repository 內至少需要包含：
   * `project_gutenberg` 資料夾
   * 您的 `.py` 或 `.ipynb` 執行檔
   * 本 `README.md` 說明文件
3. **提交作業**：將 **GitHub Repo 連結** 以及 **影片連結** 透過 Email 寄給老師。

---

## 📂 專案資料夾結構

```text
web_scraping_hw/
│
├── project_mangaz/
│   ├── Assignment01_動態爬蟲案例_mangaz_練習版.ipynb  # 教師提供的範本檔（作業起點）
│   ├── assignment01_scarper_mangaz.py                  # 將老師程式碼邏輯包裝成 def 的模組
│   └── requirements.txt                               # 相依套件清單
│
├── assignment01_scraper.py   # 漫畫 scraper 函式
├── downloaded_manga/         # 程式執行後存放漫畫圖片的資料夾（名稱可自訂）
└── README.md                 # 專案說明文件
```

---

## 🛠️ 環境設置

> 建議使用 Python 3.12 虛擬環境，避免套件版本衝突。

**1. 建立並啟動虛擬環境**

```bat
py -3.12 -m venv .venv
.\.venv\Scripts\activate.bat
python.exe -m pip install --upgrade pip
```

**2. 安裝相依套件**

```bat
cd project_mangaz
pip install -r requirements.txt
```

**3. 將虛擬環境註冊為 Jupyter Kernel（於 Notebook 中選用此環境）**

```bat
python -m ipykernel install --user --name=.venv --display-name="WebScraping(venv)"
```

完成後，開啟 Jupyter Notebook 時即可在 Kernel 選單中選擇 `WebScraping(venv)` 執行本作業。
