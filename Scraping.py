from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.chrome.options import Options
from time import sleep
import ssl
from bs4 import BeautifulSoup
from urllib import request
import saveMovie
import sys
import os
WAIT_TIME = 2
class Scraping:
    def __init__(self):
        self.isSuccess = False
        self.password = ""
        self.username = ""
        self.url = ""

    def getUserName(self, username):
        self.username = username
    
    def getPassWord(self, password):
        self.password = password

    def getUrl(self, url):
        self.url = url

    def getMovie(self, instaUrl, filePath):
        INSTA_PASSWORD = self.password
        INSTA_USERNAME = self.username
        options = Options()
        options.add_argument('--headless')
        CHROME_DRIVER_PATH = "./chromedriver.exe"
        chrome_service = fs.Service(executable_path=CHROME_DRIVER_PATH)
        browser = webdriver.Chrome(service=chrome_service, options = options)
        try:
            browser.get(instaUrl)
            sleep(WAIT_TIME)
            phoneElement = browser.find_element_by_name("username")
            phoneElement.send_keys(INSTA_USERNAME)
            #phoneElement.send_keys(os.environ["INSTA_USERNAME"])
            passElement = browser.find_element_by_name("password")
            passElement.send_keys(INSTA_PASSWORD)
            #passElement.send_keys(os.environ["INSTA_PASSWORD"])
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
        except:
            browser.close()
            return False
        # スクレイピング終了
        browser.close()
        if(saveMovie.saveMovie(url, filePath) == False):
            return False
            

