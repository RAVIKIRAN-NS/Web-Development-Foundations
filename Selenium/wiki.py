from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)
article_count.click()

all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
all_portals.click()

search = driver.find_element(By.NAME,value="search")
search.send_keys("Python",Keys.ENTER)

driver.get("https://secure-retreat-92358.herokuapp.com/")
fname= driver.find_element(By.NAME,value="fName")
fname.send_keys("Ravi")
lname = driver.find_element(By.NAME,value="lName")
lname.send_keys("kiran")
email = driver.find_element(By.NAME,value="email")
email.send_keys("ravidavi01ns@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR,value=".form-signin button")
submit.click()


driver.quit()








# binarySequence = "111001001011101010010110011"
#
# seq = ['001','010','011','101','110']
# alpha = ['c','g','a','t','u']
#
# three = []
# n = 3
# for i in range(0,len(binarySequence), n):
#     three.append(binarySequence[i:i+n])
# result = []
# three.pop(0)
#
# if binarySequence.startswith("111") or binarySequence.startswith("000"):
#     for i in three:
#         if i in seq:
#             pos = seq.index(i)
#             print(f"{alpha[pos]}")



