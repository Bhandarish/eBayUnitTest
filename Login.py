
class LoginPage():

    def __init__(self,driver):
        self.driver = driver

#Theser are three locators in this page

        self.signin_button_xpath = "//a[contains(text(),'Sign in')]"
        self.username_textbox_xpath = "//input[@id='userid']"
        self.password_textbox_xpath = "//input[@id='pass']"
        self.login_button_xpath = "//button[@id='sgnBt']"




    def signin_button(self):
        self.driver.find_element_by_xpath(self.signin_button_xpath).click()

    def enter_username(self, username):

        self.driver.find_element_by_xpath(self.username_textbox_xpath).clear
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    def enter_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()



