import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Account_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_account(self):
        user = "rhymetime"
        pwd = "team3!"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/login/")
        # time.sleep(10)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        # time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/ul/li[1]/a").click()
        # time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form[1]/button").click()
        # time.sleep(5)
        elem2 = driver.find_element_by_id("id_first_name")
        elem2.clear()
        elem2.send_keys("new test")
        # time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div/input").click()

    def test_account_page(self):
        user = "rhymetime"
        pwd = "team3!"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/login/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        # time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/ul/li[1]/a").click()
        # time.sleep(5)

    def test_upgrade(self):
        user = "rhymetime"
        pwd = "team3!"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/login/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        # time.sleep(5)

        subject = "rhymetime"
        Email = "ebuettner5@gmail.com"
        message = "This is a selenium test"
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[4]/a").click()
        elem = driver.find_element_by_id("id_subject")
        elem.send_keys(subject)

        # time.sleep(5)
        elem = driver.find_element_by_id("id_email_address")
        elem.send_keys(Email)
        # time.sleep(5)

        elem = driver.find_element_by_id("id_message")
        elem.send_keys(message)
        # time.sleep(5)

        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[4]/input").click()



        # time.sleep(10)

    def test_blog(self):
        user = "rhymetime"
        pwd = "team3!"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/login/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        # time.sleep(5)

    def test_logout(self):
        user = "rhymetime"
        pwd = "team3!"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/login/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        # time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/ul/li[2]/a").click()
        assert "Logged Out"
        # time.sleep(5)
        driver.get("http://127.0.0.1:8000")
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        # time.sleep(5)

    def test_Nursery(self):
        user = "rhymetime"
        pwd = "team3!"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/login/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        # time.sleep(5)

    def testAudio(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/hickoryDock")
        # time.sleep(2)
        x = driver.find_element_by_xpath("html/body/div/div/div/div/audio/source[contains(@src, 'hickory.mp4')]")
        x.execute

    def testNav(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/home/")
        # time.sleep(2)
        x = driver.find_element_by_xpath("html/body/nav/div/div[2]/ul/li[2]/a")
        x.click()
        # time.sleep(2)
        x = driver.find_element_by_xpath("html/body/div/div/div/div/a[6]/h3")
        x.click()
        # time.sleep(1)
        x = driver.find_element_by_xpath("html/body/div/div/div/div/a/span")
        x.click()
        # time.sleep(5)
        x = driver.find_element_by_xpath("html/body/div/div/div/div[2]/a[2]/span")
        x.click()
        # time.sleep(3)
        x = driver.find_element_by_xpath("html/body/div/div/div/div/a/h3")
        x.click()
        # time.sleep(2)
        x = driver.find_element_by_xpath("html/body/div/div/div/div/a/span")
        x.click()
        # time.sleep(3)
        x = driver.find_element_by_xpath("html/body/div/div/div/div[2]/a/span")
        x.click()
        # time.sleep(2)

    def test_signup(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Contact Us'])[1]/following::span[1]").click()
        driver.find_element_by_link_text("Sign Up").click()
        driver.find_element_by_id("id_first_name").click()
        driver.find_element_by_id("id_first_name").clear()
        driver.find_element_by_id("id_first_name").send_keys("Gary")
        driver.find_element_by_id("id_last_name").clear()
        driver.find_element_by_id("id_last_name").send_keys("Peters")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("gary@gmail.com")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("gpeters")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("gary")
        driver.find_element_by_id("id_password_repeat").clear()
        driver.find_element_by_id("id_password_repeat").send_keys("gary")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Confirm password:'])[1]/following::input[2]").click()

    def test_upgrade(self):
        user = "rhymetime"
        pwd = "team3!"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/login/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        # time.sleep(5)

        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[3]/a").click()
        # time.sleep(10)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

