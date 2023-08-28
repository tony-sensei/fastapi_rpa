import cv2
from paddleocr import PaddleOCR

def get_elements(img):
    """
    Process the screenshot and extract elements
    """
    # image preprocessing
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

    # icon extraction
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    icons = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        icon = img[y:y+h, x:x+w]
        icons.append((icon, (x, y)))
    
    # word extraction
    ocr = PaddleOCR.OCR(lang="en") 
    texts = ocr.ocr(img)
    text_data = [(line[-1][0], line[-1][-1]) for line in texts] 
    return {"icons": icons, "text_data": text_data}
