
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

class EbayLoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/Chiranjibighimire/Downloads/chromedriver")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_EbaySignin(self):
        self.driver.get("https://www.ebay.ca/")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(" //a[contains(text(),'Sign in')]").click()
        self.driver.find_element_by_css_selector("#userid").send_keys("forebay852@gmail.com")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//input[@id='pass']").send_keys("11nepal22")
        self.driver.find_element_by_xpath("//button[@id='sgnBt']").click()
        x = self.driver.title
        print(x)
        self.assertEqual(x,"Electronics, Cars, Fashion, Collectibles, Coupons and More | eBay", "Webpage is not matching")
        self.driver.find_element_by_xpath("//input[@id='gh-ac']").send_keys("Baby girl clothes")
        self.driver.find_element_by_xpath("//input[@id='gh-btn']").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//a[contains(text(),'2PCS Toddler Kids Baby Girl Winter Clothes Floral ')]").click()
        self.driver.implicitly_wait(5)

        element1 = self.driver.find_element_by_xpath(" //select[@id='msku-sel-1']")
        drp = Select(element1)
        self.driver.implicitly_wait(5)
        drp.select_by_value("0")
        self.driver.implicitly_wait(5)

        element2 = self.driver.find_element_by_xpath("//select[@id='msku-sel-2']")
        drp = Select(element2)
        drp.select_by_visible_text("3-4 Years")

        self.driver.find_element_by_css_selector("#isCartBtn_btn").click()
        x = self.driver.title
        print(x)
        self.assertEqual(x,"Provide contact info", "webpage is not matching")



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ =='__main__':
    unittest.main()
