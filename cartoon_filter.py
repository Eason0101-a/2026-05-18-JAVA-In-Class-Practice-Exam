import cv2
import numpy as np
import os

class ImageLoader:
    @staticmethod
    def load(filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"找不到圖片檔案: {filepath}")
        return cv2.imread(filepath)

class GrayConverter:
    @staticmethod
    def to_gray(image):
        # 轉換為灰階
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

class EdgeDetector:
    @staticmethod
    def detect(image):
        # 1. 影像平滑處理 (改用中值濾波器 Median Blur，去除雜訊同時保留銳利邊緣)
        blurred = cv2.medianBlur(image, 5)
        
        # 2. 自適應閾值處理 (調整 block size 和常數 C，讓線條更乾淨、不那麼雜亂)
        edges = cv2.adaptiveThreshold(
            blurred, 255, 
            cv2.ADAPTIVE_THRESH_MEAN_C, 
            cv2.THRESH_BINARY, 9, 5
        )
        return edges

class ColorQuantizer:
    @staticmethod
    def quantize(image, color_count=16):
        # 多次應用雙邊濾波器 (Bilateral Filter)，讓大區塊顏色平滑，但保留細節邊緣清晰度
        smooth_color = image
        for _ in range(3):
            smooth_color = cv2.bilateralFilter(smooth_color, 9, 75, 75)
        
        # Color quantization（顏色量化）使用 K-Means
        data = np.float32(smooth_color).reshape((-1, 3))
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)
        _, label, center = cv2.kmeans(data, color_count, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        
        center = np.uint8(center)
        result = center[label.flatten()]
        result = result.reshape(smooth_color.shape)
        
        return result

class CartoonRenderer:
    @staticmethod
    def render(color_img, edges):
        # 將邊緣(墨線)與顏色量化後的圖片合併
        return cv2.bitwise_and(color_img, color_img, mask=edges)

def main():
    input_file = "image.png"
    
    try:
        print(f"開始處理: {input_file}")
        
        # OOP Pipeline 實作 PDF 中的步驟
        img = ImageLoader.load(input_file)
        
        print("1. 轉換灰階 (GrayConverter)...")
        gray = GrayConverter.to_gray(img)
        cv2.imwrite("step1_gray.png", gray)
        
        print("2. 邊緣檢測 (EdgeDetector)...")
        edges = EdgeDetector.detect(gray)
        cv2.imwrite("step2_edges.png", edges)
        
        print("3. 顏色量化 (ColorQuantizer)...")
        quantized = ColorQuantizer.quantize(img)
        cv2.imwrite("step3_quantized.png", quantized)
        
        print("4. 卡通化渲染 (CartoonRenderer)...")
        cartoon = CartoonRenderer.render(quantized, edges)
        cv2.imwrite("step4_final_cartoon.png", cartoon)
        
        print(f"處理完成！各階段影像已分別儲存為 step1 ~ step4 的 png 檔案。")
        
    except Exception as e:
        print(f"發生錯誤: {e}")

if __name__ == "__main__":
    main()
