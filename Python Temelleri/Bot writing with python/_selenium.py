from selenium import webdriver
from githubUserInfo import username, password

# butonları çalıştırmak için örneğin:enter
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
url = "https://github.com"
driver.get(url)
time.sleep(2)  # 2 saniye bekle
print(driver.title)  # başlığı yazdır.
driver.maximize_window()  # açılan ekranı 2 saniye sonra tam ekran yap.

# github sayfasının ana ekranını ekler.
# driver.save_screenshot("Github.com-homepage.png")

searchInput = driver.find_element_by_name("q")
time.sleep(1)
searchInput.send_keys("python")  # arama kısmına pythonu arar.
time.sleep(2)  # 2 saniye bekle
searchInput.send_keys(Keys.ENTER)  # entere basar
time.sleep(2)
result = driver.page_source  # githubdaki kaynak kodları gösterir.
print(result)
driver.close()  # 2 saniye bekledikten sonra kapat


# Github takipçi listesi örneği.


class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def singIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)
        self.browser.find_element_by_xpath(
            "//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath(
            "//*[@id='password']").send_keys(self.password)
        time.sleep(20)

        self.browser.find_element_by_xpath(
            "//*[@id='login']/div[4]/form/input[14]").click()

    def getfollowers(self):
        self.browser.get("https://github.com/Ayseekinci?tab=followers")
        time.sleep(2)

        items = self.browser.find_elements_by_css_selector(
            ".d-table.table-fixed")

        for i in items:
            self.followers.append(
                i.find_element_by_css_selector(".Link--primary").text)


github = Github(username, password)
github.singIn()
github.getfollowers()
print(github.followers)
