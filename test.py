from selenium import webdriver
import win32gui
import win32con
import os, platform

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.quit()