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


def test_addteacher(webdriver):
	user="mihaadmin12"
	passw = "123123"
	name = fake.first_name()
	uname = fake.user_name() 
	passwt = fake.password() 
	email = fake.email()
	print email
	visit(url)
	page = BasiliskPage(driver = driver.browser)
	page.login_link.click()
	wait(lambda: page.is_element_present('log_btn'))
	page.login(user, passw)
	wait(lambda: page.is_element_present('log_menu'))
	page.users.click()
	page = TeachersListPage(driver = driver.browser)
	wait(lambda: page.is_element_present('add_teacher'))
	page.add_teacher.click()
	page = TeacherPage(driver = driver.browser)
	wait(lambda: page.is_element_present('save'))
	page.add_teacher(name, uname, email, passwt, passwt)
	page = TeachersListPage(driver = driver.browser)
	wait(lambda: page.is_element_present('add_teacher'))
	#time.sleep(3)
	allure.attach("Results", driver.browser.page_source, AttachmentType.HTML)
	assert page.teachers_list[-1].text == email




if __name__ == '__main__':
	driver.browser = Firefox()
	test_addteacher(driver.browser)