from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


PROMESED_DOWN = 150
PROMESED_UP = 10
twitter_email = ""
twitter_password =""

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up =0
        self.down =0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(10)
        go_button = self.driver.find_element(By.XPATH , "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a")
        go_button.click()
        time.sleep(60)

        self.up = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text()
        self.down = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text()

        self.driver.quit()

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")
        time.sleep(4)
        email = self.driver.find_element(By.NAME, "text")
        email.send_keys("Your Email or Username")
        time.sleep(3)
        email.send_keys(Keys.ENTER)
        time.sleep(2)
        passwd = self.driver.find_element(By.NAME, "password")
        passwd.send_keys("Your Password")
        time.sleep(2)
        passwd.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        tweet_compose.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMESED_DOWN}down/{PROMESED_UP}up?")
        time.sleep(3)

        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]')
        tweet_button.click()
        time.sleep(2)

        self.driver.quit()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()    
