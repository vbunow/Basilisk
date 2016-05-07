from selenium.webdriver import Firefox
from webium.wait import wait
from basilisk import *
import pytest
from allure.constants import AttachmentType
import allure
from config import *
import time
import webium.settings
webium.settings.wait_timeout = 5
url = "http://basilisk.fintegro.com/"

def test_search1(webdriver):
	user="superadmin"
	passw = "123123"
	text = "Mc"
	visit(url)
	page = BasiliskPage(driver = driver.browser)
	page.login_link.click()
	wait(lambda: page.is_element_present('log_btn'))
	page.login(user, passw)
	wait(lambda: page.is_element_present('log_menu'))
	page.university.click()
	page = UniversityListPage(driver = driver.browser)
	wait(lambda: page.is_element_present('search_field'))
	page.search(text)
	time.sleep(1)
	page = UniversityListPage(driver = driver.browser)
	allure.attach("Results", driver.browser.page_source, AttachmentType.HTML)
	assert text in page.univer_list[0].text
	

def test_search2(webdriver):
	user="superadmin"
	passw = "123123"
	text = "Mcerwreqwr"
	visit(url)
	page = BasiliskPage(driver = driver.browser)
	page.login_link.click()
	wait(lambda: page.is_element_present('log_btn'))
	page.login(user, passw)
	wait(lambda: page.is_element_present('log_menu'))
	page.university.click()
	page = UniversityListPage(driver = driver.browser)
	wait(lambda: page.is_element_present('search_field'))
	page.search(text)
	time.sleep(1)
	page = UniversityListPage(driver = driver.browser)
	allure.attach("Results", driver.browser.page_source, AttachmentType.HTML)
	assert len(page.univer_list) == 0
	
	

if __name__ == '__main__':
	driver.browser = Firefox()
	test_search2(driver.browser)