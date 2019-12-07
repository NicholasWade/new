import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class audioTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testAudio(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/hickoryDock")
        time.sleep(2)
        x = driver.find_element_by_xpath("html/body/div/div/div/div/audio/source[contains(@src, 'hickory.mp4')]")
        x.execute
