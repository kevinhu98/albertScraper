from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = 'https://sis.nyu.edu/psc/csprod/EMPLOYEE/SA/c/NYU_SR.NYU_CLS_SRCH.GBL'
driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_id('LINK2$367').click()
time.sleep(10)
pageHTML = driver.page_source.encode("utf-8")
soup = BeautifulSoup(pageHTML, 'html.parser')
print(soup.prettify())