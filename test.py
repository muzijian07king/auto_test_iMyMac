from selenium import webdriver
from selenium.webdriver.common.by import By
import win32gui
import win32con
import time

driver = webdriver.Chrome()
driver.get('https://www.imymac.com/faqs.html')
d = driver.find_element(By.CSS_SELECTOR, 'div.close-tag')
if d:
    d.click()
time.sleep(5)
driver.close()