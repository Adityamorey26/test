from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("file:///C:/Users/vivaa/Desktop/testing/selenium_js/index.html")

# Enter credentials
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("1234")

# Click login
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(2)

# Validate result
result = driver.find_element(By.ID, "result").text

if result == "Login Successful":
    print("JS Test Passed ")
else:
    print("JS Test Failed ")

driver.quit()