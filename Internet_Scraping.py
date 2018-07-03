# Module: Internet_Scraping.py
#"D:/Projects/JXM Products, llc/amazon filter/Internet_Scraping.py"
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
CHROMEDRIVER_PATH = "Drivers/chromedriver.exe"
# Set certificate errors
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
# Start chrome
driver = webdriver.Chrome("Drivers/chromedriver.exe", chrome_options=options)

#open website
driver.get("http://www.python.org")
time.sleep(4)
assert "Python" in driver.title
time.sleep(3)
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
#elem.submit()
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
print ("Get scraping and live the life")
