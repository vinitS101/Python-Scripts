# A script to automatically login to the BIT Placement portal.
# Can be used as a reference to create login scripts for other websites
import webbrowser, time
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://placement.bitmesra.ac.in/')

elem1 = browser.find_element_by_css_selector('#txtUsername')
elem2 = browser.find_element_by_css_selector('#txtPassword')
elem3 = browser.find_element_by_css_selector('#imgSubmit')

elem1.send_keys('Enter your login id/email here')
elem2.send_keys('Enter your password here')
elem3.click()
