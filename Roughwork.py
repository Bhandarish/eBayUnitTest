
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

driver = webdriver.Chrome(executable_path="/Users/Chiranjibighimire/Downloads/chromedriver")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.ebay.ca/")
driver.implicitly_wait(10)
driver.find_element_by_xpath("//a[contains(text(),'Sign in')]").click()
driver.implicitly_wait(5)
driver.find_element_by_css_selector("#userid").send_keys("forebay852@gmail.com")
driver.implicitly_wait(5)

driver.find_element_by_xpath("//input[@id='pass']").send_keys("11nepal22")
driver.find_element_by_xpath("//button[@id='sgnBt']").click()

driver.implicitly_wait(5)
driver.find_element_by_xpath("//input[@id='gh-ac']").send_keys("Baby girl clothes")
driver.find_element_by_xpath("//input[@id='gh-btn']").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//a[contains(text(),'2PCS Toddler Kids Baby Girl Winter Clothes Floral ')]").click()

element1 = driver.find_element_by_xpath(" //select[@id='msku-sel-1']")
drp = Select(element1)
drp.select_by_value("0")




element2 = driver.find_element_by_xpath("//select[@id='msku-sel-2']")
drp = Select(element2)
drp.select_by_visible_text("3-4 Years")

driver.find_element_by_css_selector("#isCartBtn_btn").click()