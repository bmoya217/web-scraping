# pulls all of trumps tweets since 11/08/2017
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
url = "https://twitter.com/realDonaldTrump"
browser.get(url)

#scroll to bottom of page
phold = browser.execute_script("return document.body.scrollHeight")
while True:
	browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(2)
	pos = browser.execute_script("return document.body.scrollHeight")
	if pos == phold:
		break
	phold = pos

#get all tweets
tweets = browser.find_elements_by_class_name("tweet-text")

print len(tweets)
for tweet in tweets:
	print(tweet.text)

browser.close()