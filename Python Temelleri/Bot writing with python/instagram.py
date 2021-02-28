# instagram giriş yapıp takipçileri görüntüleme.
from selenium import webdriver
from instagramUserInfo import username, password
from selenium.webdriver.common.keys import Keys
import time


class İnstagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def SingIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        usernameInput = self.browser.find_element_by_xpath(
            "//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath(
            "//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(10)

    def getfollowes(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(10)

        followerslink = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
        followerslink.click()


instgrm = İnstagram(username, password)
instgrm.SingIn()
instgrm.getfollowes()
