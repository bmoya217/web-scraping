#ADD. MORE. DUDES.
from __future__ import print_function
import os,sys,random,time,datetime
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

# get the list of dudes
def scrape(driver, wait, email, password):
	hrefs = []
	dudes = []

	# goto facebook and login
	driver.get('https://www.facebook.com')
	element = wait.until(EC.presence_of_element_located((By.ID, "email")))
	element.send_keys(email)
	element = driver.find_element_by_id("pass")
	element.send_keys(password)
	element.send_keys(Keys.ENTER)

	# ignore notifications notification
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "layerCancel")))
	element.click()

	# profile
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "imgWrap")))
	element.click()

	# firends list
	element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Friends")))
	element.click()

	# wait to load tab
	element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='fsl fwb fcb']/a")))

	# scroll down
	phold = driver.execute_script("return document.body.scrollHeight")
	while True:
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(1)
		pos = driver.execute_script("return document.body.scrollHeight")
		if pos == phold:
			break
		phold = pos

	# get all dudes profile page links
	elements = driver.find_elements_by_xpath("//div[@class='fsl fwb fcb']/a")
	for e in elements:
		hrefs.append(e.get_attribute('href'))

	# check which are male: profile->about->basic info->gender
	for h in hrefs:
		driver.get(h)

		element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "About")))
		element.click()

		element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Contact and Basic Info")))
		element.click()

		element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='pagelet_basic']//span")))
		elements = driver.find_elements_by_xpath("//div[@id='pagelet_basic']//span")
		for e in elements:
			if e.text == "Male":
				element = driver.find_element_by_id("fb-timeline-cover-name")
				dudes.append(element.text)
				
	return dudes

def add_more(driver, wait, dudes):
	# More Dudes: The Renaissance
	driver.get('https://www.facebook.com/groups/855607817829997/')

	for d in dudes:
		element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='groupAddMemberTypeaheadBox']//input[@class='inputtext textInput']")))
		element.send_keys(d)
		element.send_keys(Keys.ENTER)
		time.sleep(1)
		element.send_keys(Keys.CONTROL,'a')
		element.send_keys(Keys.DELETE)

def main():
	driver = webdriver.Chrome()
	wait = WebDriverWait(driver,10)
	dudes = scrape(driver, wait, sys.argv[1], sys.argv[2])
	add_more(driver, wait, dudes)
	driver.quit()

if __name__ == "__main__":
    main()