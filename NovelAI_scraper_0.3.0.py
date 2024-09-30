import selenium
import subprocess
import multiprocessing
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QTableWidget

tags = []
disable_tags = []
times_number = []
num = 0

app = QApplication([])

window = QMainWindow()
window.setWindowTitle('NovelAI cmd')

central = QWidget()
window.setCentralWidget(central)

layout = QVBoxLayout()
central.setLayout(layout)

def kaishi():
    cmd = r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9876'
    subprocess.run(cmd)
    time.sleep(5)

def mainpart():
    options = Options()

    # specify the address and port number of the opened browser
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9876")

    ser = Service(r"C:\Users\30222\Desktop\python test\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=ser)

    # open the target website
    driver.get("https://novelai.net/image")

    time.sleep(5)

    elements = driver.find_elements(By.XPATH, "//div[@class='sc-2750d5a6-0 cMHbKm']")

    # enter the tag to be used
    input_label = QLabel('使用的tag:')
    layout.addWidget(input_label)
    tag_input = QLineEdit()
    layout.addWidget(tag_input)
    tag_button = QPushButton('输入')

    def read_text():
        text = tag_input.text()
        tags.clear()
        tags.append(text)
        tags_str = ", ".join(tags)
        for element in elements:
            textarea = element.find_element(By.XPATH, ".//textarea[@placeholder='在此处写下您的提示。使用标签来塑造您的输出。' and contains(@class, 'sc-a2d0901c-45 kyIdtk')]")
            textarea.clear()
            textarea.send_keys(tags_str)
    
    tag_button.clicked.connect(read_text)
    layout.addWidget(tag_button)

    # enter a disabled tag
    disable_label = QLabel('禁用的tag:')
    layout.addWidget(disable_label)
    dtag_input = QLineEdit()
    layout.addWidget(dtag_input)
    dtag_button = QPushButton('输入')

    def dread_text():
        text = dtag_input.text()
        disable_tags.clear()
        disable_tags.append(text)
        dtags_str = ", ".join(disable_tags)
        for element in elements:
            textarea = element.find_element(By.XPATH, ".//textarea[@placeholder='写下您希望从这一代中剔除的内容。' and contains(@class, 'sc-a2d0901c-45 kyIdtk')]")
            textarea.clear()
            textarea.send_keys(dtags_str)
    
    dtag_button.clicked.connect(dread_text)
    layout.addWidget(dtag_button)

    # enter the number of loops
    times_label = QLabel('循环次数:')
    layout.addWidget(times_label)
    times_input = QLineEdit()
    layout.addWidget(times_input)
    times_button = QPushButton('输入')

    def random_times():
        text = times_input.text()
        times_number.clear()
        times_number.append(text)
        global num
        num = int(times_number[0])

    times_button.clicked.connect(random_times)
    layout.addWidget(times_button)

    # click the Start button
    hajimeru = QPushButton('开始')

    def start():
        for element in elements:
            search = element.find_element(By.XPATH, ".//button[contains(@class, 'sc-d72450af-1') and @disabled]")
            for x in range(0 , num):
                search.click()

    hajimeru.clicked.connect(start)
    layout.addWidget(hajimeru)

# Use multiprocessing instead of threading
process1 = multiprocessing.Process(target=kaishi)
process2 = multiprocessing.Process(target=mainpart)

process1.start()
process2.start()

process1.join()
process2.join()

window.setLayout(layout)
window.show()

app.exec_()
