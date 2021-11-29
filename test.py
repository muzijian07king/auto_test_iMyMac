import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.imymac.com/mac-cleaner/')
driver.execute_script('document.documentElement.scrollTop=6000')
time.sleep(1)
driver.find_element_by_css_selector('body > div.footerBuy > div > div.flexEnd > div.text-center.productColumn.hide-visible.tipsup > div > a.btn.btn-dark.btn-buy').click()
time.sleep(2)

driver.close()