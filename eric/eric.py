#ADD. MORE. DUDES.
import os,sys,random,time,datetime
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# open firefox and set explicit wait time
driver = webdriver.Chrome()
wait = WebDriverWait(driver,5)

# go to epa website
driver.get('https://www.epa.gov/saferchoice/products')

#expand table to 100 choices
element = Select(driver.find_element_by_xpath("//select[@name='tblData_length']"))
element.select_by_visible_text("100")

file = open('saferchoice.csv', 'a')
for p in range(24):
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "colorbox-inline")))
	elements = driver.find_elements_by_xpath("//tbody/tr/td")

	i = 1
	for e in elements:
		text = e.text.replace(u'\xae','') #registered sign
		text = text.replace(u'\u2021','') #double dagger
		text = text.replace(u'\u2122','') #trademark sign
		text = text.replace(u'\u2013','-') #endash
		text = text.replace(',','')
		
		if i%4 == 0:
			file.write(text + "\n")
		else:
			file.write(text + ", ")

		i = i+1

	element = wait.until(EC.element_to_be_clickable((By.ID, "tblData_next")))
	element.click()
	time.sleep(.5)

driver.quit()