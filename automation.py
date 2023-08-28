import pyautogui
import cv2
import os
import time
from paddleocr import PaddleOCR, draw_ocr
import subprocess
import requests

def open_search_engine():
    """
    Open a new search engine, Google Chrome here (MacOS)
    """
    subprocess.run(["open", "-a", "Google Chrome"])
    pyautogui.hotkey('ctrl', 'command', 'f')
    time.sleep(1)
    return

def new_page(url):
    """
    Open a new page in Google Chrome
    """
    pyautogui.hotkey('command', 't')
    time.sleep(1)

    # Type the text
    pyautogui.write(url)
    pyautogui.press('enter')
    time.sleep(2)
    return

def main():
    print("Automation started")
    # Minimize all windows on Mac
    pyautogui.hotkey('option', 'command', 'm')

    # Open Google Chrome on Mac
    open_search_engine()
    new_page("youtube.com")

    # Take a screenshot
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.png')

    # Send the screenshot to the FastAPI application
    with open('screenshot.png', 'rb') as file:
        response = requests.post('http://127.0.0.1:8000/process-screenshot', files={'file': file})

    print(response.json())

if __name__ == '__main__':
    main()
