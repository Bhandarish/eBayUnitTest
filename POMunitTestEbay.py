
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import HtmlTestRunner
from HtmlTestRunner import HTMLTestRunner

from Pages.Login import LoginPage
from Pages.AddtoCart import AddtoCart2




class EbayTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/Chiranjibighimire/Downloads/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        self.driver.get("https://www.ebay.ca/")

        login = LoginPage(driver)
        login.signin_button()
        login.enter_username("forebay852@gmail.com")
        login.enter_password("11nepal22")
        login.enter_login()

        AddtoCart = AddtoCart2(driver)
        AddtoCart.search_item("Baby girl clothes")
        AddtoCart.addtocart()
        AddtoCart.logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()



if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/Chiranjibighimire/Downloads"), verbosity=2)







