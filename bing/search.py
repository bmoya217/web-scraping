import os,sys,random,time,datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

search_terms = []
with open('dictionary.txt') as ifile:
	for line in ifile:
		search_terms.append("define " + line)

def search(e, p):
	now = datetime.datetime.now()
	rewards = 0
	rhold = -1
		
	# create instance of Firefox 
	driver = webdriver.Firefox()
	
	# live.com to login
	driver.get('http://www.live.com')
	time.sleep(random.uniform(2,3))

	email = driver.find_element_by_id("i0116")
	email.send_keys(e)
	email.send_keys(Keys.ENTER)
	time.sleep(random.uniform(2,3))

	password = driver.find_element_by_id("i0118")
	password.send_keys(p)
	password.send_keys(Keys.ENTER)
	time.sleep(random.uniform(2,3))
	
	# bing.com
	driver.get("http://www.bing.com")
	time.sleep(random.uniform(1,2))

	while(rewards != rhold):
		# Print current point count
		rhold = rewards
		rewards = driver.find_element_by_id('id_rc').text
		print 'Current Points: ',rewards

		# Ready search bar
		searchbar = driver.find_element_by_id('sb_form_q')
		searchbar.send_keys(Keys.CONTROL,'a')
		searchbar.send_keys(Keys.DELETE)
		time.sleep(random.uniform(4,6))
		
		# Search
		term = search_terms[random.randrange(0,len(search_terms))]
		print 'Searching for:\t', term
		searchbar.send_keys(term,Keys.ENTER)
		time.sleep(random.uniform(7,10))
	driver.quit()

emails = ['bmoya217@gmail.com']
password = 'Recursion1!'
for email in emails:
	search(email,password)