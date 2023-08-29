import cv2
from paddleocr import PaddleOCR
import base64

def convert_image_to_base64(img):
    _, buffer = cv2.imencode(img)
    img_str = base64.b64encode(buffer).decode('utf-8')
    return img_str


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


    # for contour in contours:
    #     x, y, w, h = cv2.boundingRect(contour)

    #     icon = img[y:y+h, x:x+w]
    #     icons.append((convert_image_to_base64(icon), (x, y)))
    
    # word extraction
    ocr = PaddleOCR(use_angle_cls=True, lang="en") 
    texts = ocr.ocr(img, cls=True)

    text_data = []
    for line in texts[0]:
        text_coords = line[0]
        text_x = sum([text_coords[i][0] for i in range(4)]) / 4
        text_y = sum([text_coords[i][1] for i in range(4)]) / 4
        text = line[-1][0]
        text_data.append((text, (text_x, text_y)))
    

    return {"icons": icons, "text_data": text_data} 
