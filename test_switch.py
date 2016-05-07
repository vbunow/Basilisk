from selenium.webdriver import Firefox
from webium.wait import wait
from allure.constants import AttachmentType
import allure
import time
from basilisk import *
import pytest
from config import *

url = "http://basilisk.fintegro.com/"
user = "superadmin" 
passw =  "123123"


def test_switch_univer(webdriver):
	visit(url)
	page = BasiliskPage(driver = driver.browser)
	page.login_link.click()
	wait(lambda: page.is_element_present('log_btn'))
	page.login(user, passw)
	wait(lambda: page.is_element_present('university'))
	page.university.click()
	page = UniversityListPage(driver = driver.browser)
	wait(lambda: page.is_element_present('univer_add'))
	page.univer_links[0].click()
	page = UniverPage(driver = driver.browser)
	wait(lambda: page.is_element_present('add_admin'))
	if page.status.get_attribute('checked'):
		test = "on"
		page.on.click()
		set_value(page.disable_pass, "123123")
		page.change.click()
	else:
		test = "off"
		page.off.click()
	time.sleep(3)
	page.save_btn.click()
	page = UniversityListPage(driver = driver.browser)
	wait(lambda: page.is_element_present('univer_add'))
	page.univer_links[0].click()
	page = UniverPage(driver = driver.browser)
	wait(lambda: page.is_element_present('add_admin'))
	allure.attach("Results", driver.browser.page_source, AttachmentType.HTML)
	if test == "on":
		assert page.status.get_attribute('checked') == None
	elif test == "off":
		assert page.status.get_attribute('checked') == 'true'
	

if __name__ == '__main__':
	driver.browser = Firefox()
	test_switch_univer(driver.browser)