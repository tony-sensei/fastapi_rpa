from fastapi import FastAPI
import pyautogui
import time
import os
import numpy as np
import cv2 
import subprocess
from actions import *


app = FastAPI()

@app.get("/")
def root():
    print("started")
    # Minimize all windows on Mac
    pyautogui.hotkey('option', 'command', 'm')

    # Open Google Chrome on Mac
    open_search_engine()
    new_page("youtube.com")


    

