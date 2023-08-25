from fastapi import FastAPI
import pyautogui
import time
import os

app = FastAPI()

@app.get("/")
def automate_chrome():
    
    os.system("open -a 'Google Chrome.app'")  
    time.sleep(2) 
    
    pyautogui.write('youtube.com')
    pyautogui.press('enter')
    time.sleep(3) 
    
    pyautogui.write('hello world')
    pyautogui.press('enter')

    return {"message": "Process Automated!"}