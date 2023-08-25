from fastapi import FastAPI
import pyautogui
import time
import os
import numpy as np
import cv2 

app = FastAPI()

@app.get("/")
def automate_chrome():
    search_query = "OpenAI GPT-4"
    google = locate_on_screen('google.jpg')   
    pyautogui.doubleClick(google)
    time.sleep(1)   
    hanyu = locate_on_screen('hanyu.jpg')
    pyautogui.click(hanyu)
    pyautogui.press('enter')
    pyautogui.write(search_query)
    pyautogui.press('enter')


def locate_on_screen(template_path):
    # Take a screenshot of the entire screen
    screenshot = pyautogui.screenshot()
    
    screenshot_np = np.array(screenshot)
    screen_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
    
    # Read the template image
    template = cv2.imread(template_path, 0)
    w, h = template.shape[::-1]


    # Use template matching to find the template in the screenshot
    res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.6
    loc = np.where(res >= threshold)
    
    for pt in zip(*loc[::-1]):
        center_x = pt[0] + w // 2
        center_y = pt[1] + h // 2
        return (center_x, center_y)