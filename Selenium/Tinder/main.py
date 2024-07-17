from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://tinder.com/')

sleep(2)
decline = driver.find_element(By.XPATH,value='//*[@id="c315867768"]/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]')
decline.click()

sleep(2)
login = driver.find_element(By.XPATH, value='//*[@id="c315867768"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]')
login.click()

sleep(2)
google_log = driver.find_element(By.XPATH,value='//*[@id="c1320596969"]')
google_log.click()

email = 'rowdybadboy904@gmail.com'
password= 'Ra'