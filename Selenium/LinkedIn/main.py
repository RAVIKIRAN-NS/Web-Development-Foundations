from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3811742982&distance=25&f_AL=true&geoId=102713980&keywords=python%20developer&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true")


email = 'ravidavi01ns@gmail.com'
password = 'ravidavi01'

time.sleep(2)
sign_in = driver.find_element(By.LINK_TEXT,value="Sign in")
sign_in.click()

time.sleep(2)
email_field = driver.find_element(By.NAME,value="session_key")
email_field.send_keys(email)
pass_field = driver.find_element(By.NAME,value="session_password")
pass_field.send_keys(password)
pass_field.send_keys(Keys.ENTER)

time.sleep(2)
apply_button = driver.find_element(By.CLASS_NAME,value='jobs-apply-button--top-card')
apply_button.click()

time.sleep(2)
next_button = driver.find_element(By.CSS_SELECTOR,value="footer button")
while next_button == next_button:
    next_button.click()






