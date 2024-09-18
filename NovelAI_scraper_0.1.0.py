#NovelAI scraper
import selenium
import subprocess
import threading
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget,QLineEdit,QTableWidget

def kaishi():
    cmd = r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9876'
    subprocess.run(cmd)
    time.sleep(5)
#open the webpage