from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://localhost:5000")

# Fill form
driver.find_element(By.NAME, "name").send_keys("Vivaan")
driver.find_element(By.NAME, "email").send_keys("test@gmail.com")

# Submit
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(2)

# Validate
page = driver.page_source

if "Registration Successful" in page:
    print("Flask Test Passed")
else:
    print("Flask Test Failed")

driver.quit()