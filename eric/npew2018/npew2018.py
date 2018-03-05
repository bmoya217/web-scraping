#!/usr/bin/python
import os, sys, random, time, datetime
from unidecode import unidecode
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

hrefs = []
company=""
booth=""
website=""
location=""
description=""
categories=""

# open chrome and set explicit wait time
driver = webdriver.Chrome()
wait = WebDriverWait(driver,5)

# go to natural products expo west 2018 event map
driver.get('https://www.expowest.com/ew18/Public/EventMap.aspx?')

# wait for it to load
time.sleep(5)

# click on list exhibitor list
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "abtn-ExhibitorList")))
element.click()

time.sleep(2)

# file = open('npew.csv', 'a')

# get hrefs
element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "exhibitorName")))
elements = driver.find_elements_by_class_name("exhibitorName")
for e in elements:
	hrefs.append(e.get_attribute('href'))


print len(hrefs)

file = open('npew2018.csv', 'a')

# scrape info from each href [company name, ]
for h in hrefs:
	driver.get(h)

	categories=""
	brands=""

	# company name
	try:
		element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "content-title")))
		company = element.text
	except:
		company=""
	
	# booth: remove "Booth: " from front
	try:
		element = driver.find_element_by_class_name("aa-mapIt")
		booth = element.text[7:]
	except:
		booth=""

	# website
	try:
		element = driver.find_element_by_class_name("pes-external-link-gate")
		website = element.text
	except:
		website=""

	# location
	try:
		elements = driver.find_elements_by_xpath("//ul[@class='list-unstyled']/li")
		location = elements[0].text + ", " + elements[1].text
	except:
		location=""

	# description
	try:
		element = driver.find_element_by_class_name("BoothPrintProfile")
		description = element.text
	except:
		description=""

	# categories
	try:
		elements = driver.find_elements_by_xpath("//div[@class='ProductCategoryContainer']/li")
		for e in elements:
			categories += e.text + ", "
		categories = categories[:-2]
	except:
		categories=""

	# brands
	try:
		element = driver.find_element_by_class_name("BoothBrands")
		brands = element.text[8:]
	except:
		brands=""

	line = "\"" + company+"\", \""+booth+"\", \""+website+"\", \""+location+"\", \""+description+"\", \""+categories+"\", \""+brands+"\"\n"
	line = unidecode(line)
	line = line.replace('\"','\'')

	file.write(line)

file.close()
driver.quit()