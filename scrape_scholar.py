#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import time
from contextlib import closing
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup


page_url = 'https://scholar.google.com/'

search_term = input('Enter search term:')
related_terms = list()

with webdriver.Firefox() as browser:
	browser.get(page_url)
	search_bar = browser.find_element(By.NAME, 'q')
	for i in search_term:
		search_bar.send_keys(i)
		time.sleep(1)
		try:
			ul= browser.find_element(By.XPATH, "//input[@name='q']//following-sibling::*//ul")
			for li in ul.find_elements(By.TAG_NAME, 'li'):
				new_term = li.text.strip()
				related_terms.append(new_term)
				print(new_term)

		except Exception as e:
			print(e)

	page_source = browser.page_source

related_terms = set(related_terms)
with(open('%s.txt'%(search_term.replace(' ','_')), 'w')) as f:
	for related_term in related_terms:
		f.write(related_term+'\n')

