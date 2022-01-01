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

WAIT_TIME = 2

# ブラウザエンジンでHTMLを生成させる
CHROME_DRIVER_PATH = "./chromedriver.exe"
chrome_service = fs.Service(executable_path=CHROME_DRIVER_PATH)
browser = webdriver.Chrome(service=chrome_service)
browser.get('https://www.instagram.com/stories/guardpassers/2740897169182593518/')
sleep(WAIT_TIME)
phoneElement = browser.find_element_by_name("username")
phoneElement.send_keys("kita50k")
passElement = browser.find_element_by_name("password")
passElement.send_keys("kaito0830")
# Pythonでログイン
elem_login_btn = browser.find_element_by_css_selector('.sqdOP.L3NKy.y3zKF')
elem_login_btn.click()
sleep(WAIT_TIME)
elem_after_btn = browser.find_element_by_css_selector(".sqdOP.yWX7d.y3zKF")
elem_after_btn.click()
sleep(WAIT_TIME)
elem_watchStory_btn = browser.find_element_by_css_selector(".sqdOP.L3NKy.y1rQx.cB_4K")
elem_watchStory_btn.click()
sleep(0.5)
elem_video = browser.find_element_by_css_selector(".y-yJ5.OFkrO")
elem_tag_video = browser.find_element_by_css_selector("video > source:first-child")
url = elem_tag_video.get_attribute("src")
print(url)
print(elem_tag_video)
"""
print(elem_video)
htmlSource = browser.page_source.encode("utf-8")
ssl._create_default_https_context = ssl._create_unverified_context
soup = BeautifulSoup(htmlSource, "html.parser")
"""
