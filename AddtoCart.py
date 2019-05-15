class AddtoCart2():
    def __init__(self,driver):
        self.driver = driver

    #These are the three locators on this page
        self.search_box_xpath = " //input[@id='gh-ac']"
        self.search_button_xpath = " //input[@id='gh-btn']"
        self.item_xpath = "//a[contains(text(),'2PCS Toddler Kids Baby Girl Winter Clothes Floral ')]"
        self.select_item_xpath = " //select[@id='msku-sel-1']"
        self.addtoCart_button_css_selector = "#isCartBtn_btn"
        self.logout_arrow_xpath =  "//button[@id='gh-ug']"
        self.logout_button_xpath = "//a[contains(text(),'Sign out')]"

    def search_item(self,searchbox):
        self.driver.find_element_by_xpath (self.search_box_xpath).clear()
        self.driver.find_element_by_xpath(self.search_box_xpath).send_keys(searchbox)
        self.driver.find_element_by_xpath(self.search_button_xpath).click()

    def addtocart(self):
        self.driver.find_element_by_xpath(self.item_xpath).click()
        self.driver.find_element_by_xpath(self.select_item_xpath).click()
        self.driver.find_element_by_css_selector(self.addtoCart_button_css_selector).click()

    def logout(self):
        self.driver.find_element_by_xpath(self.logout_arrow_xpath).click()
        self.driver.find_element_by_xpath(self.logout_button_xpath).click()

