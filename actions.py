import pyautogui
import cv2
import os

def get_elements(screenshot):
  
  # process screenshot using opencv
  screenshot = cv2.imread(screenshot)

  # image preprocessing
  gray_image = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
  _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

  # icon extraction
  contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  icons = []
  for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    icon = screenshot[y:y+h, x:x+w]
    icons.append((icon, (x, y)))
  
  # word extraction
  ocr = paddleocr.OCR() 
  texts = ocr.ocr(screenshot)
  text_data = [(line[-1][0], line[-1][-1]) for line in texts] 



def new_page():
  pass