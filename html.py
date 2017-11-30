# get the html of any web page
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = ""
driver = webdriver.Firefox()
driver.get(url)

##############################################
element = driver.find_element_by_xpath("//*")#
html = element.get_attribute("innerHTML")	 #
file = open('html.txt','w')					 #
file.write(html.encode('utf-8'))			 #
file.close()								 #
##############################################

driver.close()