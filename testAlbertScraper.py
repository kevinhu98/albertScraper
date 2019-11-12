from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = 'https://sis.nyu.edu/psc/csprod/EMPLOYEE/SA/c/NYU_SR.NYU_CLS_SRCH.GBL'
driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_xpath('//*[@id="LINK1$378"]').click()
time.sleep(10)
#for i in range(1,100):
#try:
driver.find_element_by_id('NYU_CLS_DERIVED_TERM$37').click()
time.sleep(5)
test = driver.find_element_by_xpath('//*[@id="win0divNYU_CLS_DERIVED_HTMLAREA3$37"]/div/table/tbody/tr/td')
test2 = driver.find_element_by_xpath('//*[@id="win0divNYU_CLS_DERIVED_HTMLAREA3$38"]/div/table/tbody/tr/td')

print(test.text)
print(test2.text)

#pageHTML = driver.page_source.encode("utf-8")
#soup = BeautifulSoup(pageHTML, 'html.parser')
#rint(soup.prettify())