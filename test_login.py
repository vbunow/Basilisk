from selenium.webdriver import Firefox
from webium.wait import wait
import time
from basilisk import *
import pytest
from allure.constants import AttachmentType
import allure
from config import *
import webium.settings
webium.settings.wait_timeout = 5
url = "http://basilisk.fintegro.com/"

def test_login_valid(webdriver, superadmin):
	#user="superadmin"
	#passw = "123123"
	visit(url)
	driver.browser.maximize_window()
	page = BasiliskPage(driver = driver.browser)
	page.login_link.click()
	wait(lambda: page.is_element_present('log_btn'))
	page.login(superadmin[0], superadmin[1])
	wait(lambda: page.is_element_present('log_menu'))
	allure.attach("Results", driver.browser.page_source, AttachmentType.HTML)
	assert page.is_element_present('log_menu')

@pytest.mark.xfail
def test_login_invalid(webdriver):
	user= "superadmin"
	passw = "123124"
	visit(url)
	page = BasiliskPage(driver = driver.browser)
	page.login_link.click()
	wait(lambda: page.is_element_present('log_btn'))
	page.login(user, passw)
	wait(lambda: page.is_element_present('login_link'))
	time.sleep(1)
	allure.attach("Results", driver.browser.page_source, AttachmentType.HTML)
	assert page.is_element_present('log_menu')
	#assert page.is_element_present('log_menu') is False
	



if __name__ == '__main__':
	driver.browser = Firefox()
	test_login_valid(driver.browser, ["superadmin", "123123"])
	