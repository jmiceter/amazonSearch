# Module: Internet_Scraping.py
#"D:/Projects/JXM Products, llc/amazon filter/Internet_Scraping.py"
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
CHROMEDRIVER_PATH = "Drivers/chromedriver.exe"
# Set certificate errors
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
# Start chrome
driver = webdriver.Chrome("Drivers/chromedriver.exe", chrome_options=options)

#open website
driver.get("https://www.cox.com/residential")
time.sleep(3)
assert "Cox" in driver.title

#open drop down and sign in
driver.find_element_by_id("pf-signin-trigger").click()
print('flag 1')
elem = driver.find_element_by_id("pf-password")
time.sleep(1)
elem.send_keys("password")
print('flag 2')
elem = driver.find_element_by_id("pf-username")
time.sleep(1)
elem.send_keys("jmiceter1")
#elem.submit()
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source 

#open drop down and sign in
driver.get("https://www.cox.com/ibill/make-payment.cox")
#driver.close()
print ("Get scraping and live the life")
