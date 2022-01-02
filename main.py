"""import Scraping
sampleScraping = Scraping.Scraping()
sampleScraping.sampleSoup()
while(True):
    None
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs
from time import sleep
import ssl
from bs4 import BeautifulSoup
from urllib import request
import saveMovie
import sys

WAIT_TIME = 2

def stop():
    while True:
        None

# ブラウザエンジンでHTMLを生成させる

instaUrl = sys.argv[1]
CHROME_DRIVER_PATH = "./chromedriver.exe"
chrome_service = fs.Service(executable_path=CHROME_DRIVER_PATH)
browser = webdriver.Chrome(service=chrome_service)
browser.get(instaUrl)
sleep(WAIT_TIME)
phoneElement = browser.find_element_by_name("username")
phoneElement.send_keys("kita50k")
passElement = browser.find_element_by_name("password")
passElement.send_keys("kaito0830")
sleep(WAIT_TIME)
# Pythonでログイン
elem_login_btn = browser.find_element_by_css_selector('.sqdOP.L3NKy.y3zKF')
elem_login_btn.click()
sleep(WAIT_TIME)
elem_after_btn = browser.find_element_by_css_selector(".sqdOP.yWX7d.y3zKF")
elem_after_btn.click()
sleep(WAIT_TIME)
elem_watchStory_btn = browser.find_element_by_css_selector(".sqdOP.L3NKy.y1rQx.cB_4K")
elem_watchStory_btn.click()
sleep(WAIT_TIME * 0.5)
elem_tag_video = browser.find_element_by_css_selector("video > source:first-child")
url = elem_tag_video.get_attribute("src")
print(url)
saveMovie.saveMovie(url)
browser.close()

