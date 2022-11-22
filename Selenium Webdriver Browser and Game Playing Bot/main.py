from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = "Your Email"
ACCOUNT_PASSWORD = "Your Password"
PHONE = "Phone Number"

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=marketing%20intern&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

time.sleep(2)
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(5)
email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(15)

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    #Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(15)
        
        #If phone field is empty, then fill your phone number.
        # phone = driver.find_element_by_class_name("fb-single-line-text__input")
        # if phone.text == "":
        #     phone.send_keys(PHONE)

        submit_button = driver.find_element_by_css_selector("footer button")

        #If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()
    
        #Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    #If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
 
#            ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"  Selenium Webdriver Browser and Game Playing Bot :↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓    

        # from selenium import webdriver
        # from selenium.webdriver.common.keys import Keys
        # driver = webdriver.Chrome()
        # from selenium.webdriver.support.ui import WebDriverWait
        # from selenium.webdriver.support import expected_conditions as EC
        # from selenium.webdriver.common.by import By


        # fname = driver.find_element_by_name("fName")
        # lname = driver.find_element_by_name("lName")
        # email = driver.find_element_by_name("email")

        # fname.send_keys("")
        # lname.send_keys("")
        # email.send_keys("")
        # email.send_keys(Keys.ENTER)
        # cookie = driver.find_element_by_id("cookie")

        # Get upgrade item ids.
        # items = driver.find_elements_by_css_selector("#store div")
        # item_ids = [item.get_attribute("id") for item in items]

        # timeout = time.time() + 5
        # five_min = time.time() + 60*5 # 5minutes

        # while True:
        #     cookie.click()

        #     #Every 5 seconds:
        #     if time.time() > timeout:

        #         #Get all upgrade <b> tags
        #         all_prices = driver.find_elements_by_css_selector("#store b")
        #         item_prices = []

        #         #Convert <b> text into an integer price.
        #         for price in all_prices:
        #             element_text = price.text
        #             if element_text != "":
        #                 cost = int(element_text.split("-")[1].strip().replace(",", ""))
        #                 item_prices.append(cost)

        #         #Create dictionary of store items and prices
        #         cookie_upgrades = {}
        #         for n in range(len(item_prices)):
        #             cookie_upgrades[item_prices[n]] = item_ids[n]

        #         #Get current cookie count
        #         money_element = driver.find_element_by_id("money").text
        #         if "," in money_element:
        #             money_element = money_element.replace(",", "")
        #         cookie_count = int(money_element)

        #         #Find upgrades that we can currently afford
        #         affordable_upgrades = {}
        #         for cost, id in cookie_upgrades.items():
        #             if cookie_count > cost:
        #                  affordable_upgrades[cost] = id

        #         #Purchase the most expensive affordable upgrade
        #         highest_price_affordable_upgrade = max(affordable_upgrades)
        #         print(highest_price_affordable_upgrade)
        #         to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        #         driver.find_element_by_id(to_purchase_id).click()
                
        #         #Add another 5 seconds until the next check
        #         timeout = time.time() + 5

        #     #After 5 minutes stop the bot and check the cookies per second count.
        #     if time.time() > five_min:
        #         cookie_per_s = driver.find_element_by_id("cps").text
        #         print(cookie_per_s)
        #         break


