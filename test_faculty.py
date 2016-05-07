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
webium.settings.wait_timeout = 15
url = "http://basilisk.fintegro.com/"

def test_add_faculty_from_list(webdriver):
	user="superadmin"
	passw = "123123"
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
	page.univer_links[10].click()
	page = UniverPage(driver = driver.browser)
	wait(lambda: page.is_element_present('add_admin'))
	page.faculty_dep.click()
	page = FacultyListPage(driver = driver.browser)
	wait(lambda: page.is_element_present('add'))
	time.sleep(1)
	page.add.click()
	time.sleep(2)
	if len(page.all_faculties) > 1:
		faculty = page.all_faculties[1].text
		page.all_faculties[1].click()
		wait(lambda: page.is_element_present('add'))
		test = False
		for i in range(len(page.univer_faculties)):
			if page.univer_faculties[i].text == faculty:
				test = True
		allure.attach("Results", driver.browser.page_source, AttachmentType.HTML)
		assert test		
	else:
		 pytest.fail("There is no more Faculties in the list")
	

def test_add_faculty_custom(webdriver):
	user="superadmin"
	passw = "123123"
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
	page.univer_links[9].click()
	page = UniverPage(driver = driver.browser)
	wait(lambda: page.is_element_present('add_admin'))
	page.faculty_dep.click()
	page = FacultyListPage(driver = driver.browser)
	wait(lambda: page.is_element_present('add'))
	time.sleep(1)
	page.add.click()
	time.sleep(2)
	page.all_faculties[0].click()
	wait(lambda: page.is_element_present('save'))
	faculty = fake.company()
	set_value(page.name, faculty)
	page.save.click()
	wait(lambda: page.is_element_present('add'))
	allure.attach("Results", driver.browser.page_source, AttachmentType.HTML)
	assert page.univer_faculties[-1].text == faculty		
	



if __name__ == '__main__':
	driver.browser = Firefox()
	test_add_faculty_custom(driver.browser)