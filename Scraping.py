

from selenium import webdriver
from time import sleep
import ssl
from bs4 import BeautifulSoup
from urllib import request
class Scraping:
    def __init__(self):
        None

    def sampleSoup(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        url = 'https://techacademy.jp/magazine/22805/'
        response = request.urlopen(url)
        soup = BeautifulSoup(response,"html.parser")
        sample = soup.find("a")
        response.close()
        print(self.getValue())

    def getValue(self):
        driver = webdriver.Chrome("./chromedriver.exe")
        driver.get('https://www.instagram.com/stories/guardpassers/2740897169182593518/')
        value = driver.find_element_by_id('zoomWindow')
        return value