from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException




driver = webdriver.Chrome()

driver.get("http://www.tinder.com")

time.sleep(5)
login = driver.find_element_by_xpath(("//*[text()='Log in']"))
login.click()
time.sleep(5)
withgoogle = driver.find_element_by_xpath("/html/body").click()
time.sleep(5)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(2)

email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')
email.send_keys("Your Facebook")
time.sleep(4)
password.send_keys("Facebook Password")
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)
time.sleep(5)
allow_location_button =driver.find_element(By.XPATH, "//*[@id='q-929574956']/main/div/div/div/div[3]/button[1]")
allow_location_button.click()
time.sleep(4)
notificates = driver.find_element(By.XPATH, "//*[@id='q-929574956']/main/div/div/div/div[3]/button[2]")
notificates.click() 

accept = driver.find_element(By.XPATH, "//*[@id='q798806120']/div/div[2]/div/div/div[1]/div[1]/button")
accept.click()
time.sleep(3)

darkmode = driver.find_element(By.ID, "darkModeSwitch")
darkmode.click()
time.sleep(2)
exite = driver.find_element(By.XPATH, "//*[@id='q-929574956']/main/div/div[2]/button")
exite.click()

for n in range(100):

    #Add a 1 second delay between likes.
    time.sleep(2)
    try:
        print("called")
        like_button = driver.find_element(By.XPATH, "//*[@id='q798806120']/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[4]/button")
        like_button.click()

        #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR,".itsAMatch a")
            match_popup.click()
                   
        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep()    


driver.quit()
