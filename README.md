# Python 圖片與 PDF 處理範例

這個專案提供兩個基本的 Python 腳本來示範如何用 PDF 方式處理圖片：
1. **將多張圖片合併成單一 PDF 檔案** (`image_to_pdf.py`)
2. **從現有的 PDF 檔案中提取所有圖片** (`pdf_to_image.py`)

## 安裝依賴

請確保你的系統已經安裝 Python（建議使用環境如 venv 或是 Conda）。你需要安裝 `Pillow`（處理圖片）和 `PyMuPDF`（處理 PDF 中的圖片）。請在終端機中執行：

```powershell
pip install -r requirements.txt
```

*(或者手動輸入 `pip install Pillow PyMuPDF`)*

## 1. 圖片合併成 PDF

檔案: `image_to_pdf.py`

會將當前目錄中的圖片檔案（如 `sample1.jpg`, `sample2.png`）合併，並匯出一份名為 `output_from_images.pdf` 的檔案。

**使用方法**：
打開 `image_to_pdf.py`，找到 `sample_images = ["sample1.jpg", "sample2.png"]`，改成你自己準備好的圖片檔名與路徑。
執行指令：
```powershell
python image_to_pdf.py
```

## 2. 從 PDF 提取圖片

檔案: `pdf_to_image.py`

會讀取指定的 `sample.pdf` 檔案，尋找 PDF 中的每一張內嵌圖片，並依照「頁碼_順序」的格式萃取並儲存到 `extracted_images` 資料夾中。

**使用方法**：
打開 `pdf_to_image.py`，找到 `sample_pdf = "sample.pdf"`，改成你自己真實的 PDF 檔名與路徑。
執行指令：
```powershell
python pdf_to_image.py
```
