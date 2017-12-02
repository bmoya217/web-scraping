#ADD. MORE. DUDES.
import os,sys,random,time,datetime
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

# open firefox and set explicit wait time
driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)

# variables
email = sys.argv[1]
password = sys.argv[2]
hrefs = []
friends = []

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

# scroll down until all friends are loaded
phold = driver.execute_script("return document.body.scrollHeight")
while True:
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(1)
	pos = driver.execute_script("return document.body.scrollHeight")
	if pos == phold:
		break
	phold = pos

# get all friends
elements = driver.find_elements_by_xpath("//div[@class='fsl fwb fcb']/a")
for e in elements:
	hrefs.append(e.get_attribute('href'))

print "Checking " + str(len(hrefs)) + " friends."

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
			friends.append(element.text)

	if len(friends) > 6:
		break 

# More Dudes: The Renaissance
driver.get('https://www.facebook.com/groups/855607817829997/')

# add more dudes
for f in friends:
	element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='groupAddMemberTypeaheadBox']//input[@class='inputtext textInput']")))
	element.send_keys(f)
	element.send_keys(Keys.ENTER)
	time.sleep(1)
	element.send_keys(Keys.CONTROL,'a')
	element.send_keys(Keys.DELETE)

driver.quit()