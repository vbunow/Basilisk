from selenium.webdriver import Firefox
from webium.wait import wait
from basilisk import *
import pytest
from allure.constants import AttachmentType
import allure
import time
from config import *
import webium.settings
from faker import Faker
fake = Faker()
webium.settings.wait_timeout = 10
url = "http://basilisk.fintegro.com/"

def test_addadmin1(webdriver):
	user="superadmin"
	passw = "123123"
	name = fake.first_name()
	lname = fake.last_name() 
	uname = fake.user_name() 
	passwa = fake.password() 
	email = fake.email()
	visit(url)
	#driver.browser.maximize_window()
	page = BasiliskPage(driver = driver.browser)
	page.login_link.click()
	wait(lambda: page.is_element_present('log_btn'))
	page.login(user, passw)
	wait(lambda: page.is_element_present('log_menu'))
	page.university.click()
	page = UniversityListPage(driver = driver.browser)
	wait(lambda: page.is_element_present('univer_add'))
	page.univer_add.click()
	page = UniverPage(driver = driver.browser)
	wait(lambda: page.is_element_present('add_admin'))
	time.sleep(3)
	page.add_admin.click()
	page = UniverAdminPage(driver = driver.browser)
	wait(lambda: page.is_element_present('name'))
	page.add_uadmin(name, lname, uname, email, passwa, passwa)
	page = UniverPage(driver = driver.browser)
	wait(lambda: page.is_element_present('add_admin'))
	time.sleep(3)
	allure.attach("Results", driver.browser.page_source, AttachmentType.HTML)
	assert email == page.email_list[0].text
	

def test_addadmin2(webdriver):
	user="superadmin"
	passw = "123123"
	'''name = "Mihail"
	lname = "Cherniavskiy"
	uname = "mihaadmin24"
	email = "mihaadmin24@ukr.net"'''
	name = fake.first_name()
	lname = fake.last_name() 
	uname = fake.user_name() 
	passwa = fake.password() 
	email = fake.email()
	visit(url)
	#driver.browser.maximize_window()
	page = BasiliskPage(driver = driver.browser)
	page.login_link.click()
	wait(lambda: page.is_element_present('log_btn'))
	page.login(user, passw)
	wait(lambda: page.is_element_present('log_menu'))
	page.university.click()
	page = UniversityListPage(driver = driver.browser)
	wait(lambda: page.is_element_present('univer_add'))
	page.univer_links[5].click()
	page = UniverPage(driver = driver.browser)
	wait(lambda: page.is_element_present('add_admin'))
	time.sleep(3)
	page.add_admin.click()
	page = UniverAdminPage(driver = driver.browser)
	wait(lambda: page.is_element_present('name'))
	page.add_uadmin(name, lname, uname, email, passwa, passwa)
	page = UniverPage(driver = driver.browser)
	wait(lambda: page.is_element_present('add_admin'))
	time.sleep(3)
	allure.attach("Results", driver.browser.page_source, AttachmentType.HTML)
	assert email == page.email_list[-1].text
	

	


if __name__ == '__main__':
	driver.browser = Firefox()
	test_addadmin1(driver.browser)