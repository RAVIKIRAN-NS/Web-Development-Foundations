from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/7th=1")
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cent = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"{price_dollar.text}.{price_cent.text}")

driver.get("https://www.python.org/")
# search_bar =  driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documents = driver.find_element(By.CSS_SELECTOR,value=".documentation-widget a")
# print(documents.text)
# print(documents.get_attribute("href"))

#3.Xpath
# bug_link = driver.find_element(By.XPATH,value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

#Upcoming events
u_e = {}
times = driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
names = driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a")

for i in range(len(times)):
    u_e[i]= {
        "time" : times[i].text,
        "name" : names[i].text
    }
print(u_e)




driver.quit()
