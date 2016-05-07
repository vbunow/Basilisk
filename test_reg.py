from selenium.webdriver import Firefox
from webium.wait import wait
from basilisk import *
import pytest
from allure.constants import AttachmentType
import allure
import driver
from config import *
import webium.settings
from faker import Faker
webium.settings.wait_timeout = 5
fake = Faker()
url = "http://basilisk.fintegro.com/"

fname = fake.first_name()
lname = fake.last_name() 
login = fake.user_name() 
passw = fake.password() 
email = fake.email()
univer = "Z"
promo = fake.postcode()


def test_reg_valid(webdriver):
	visit(url)
	driver.browser.maximize_window()
	page = BasiliskPage(driver = driver.browser)
	page.login_link.click()
	wait(lambda: page.is_element_present('log_btn'))
	page.reg_link.click()
	page = RegistrationPage(driver = driver.browser)
	wait(lambda: page.is_element_present('button_reg'))
	page.register(fname, lname, login, passw, passw, email, promo, univer)
	wait(lambda: page.is_element_present('success_msg'))
	f = open("users_all.txt", 'a')
	f.write('\n' + login + ' ' + passw)
	f.close()
	allure.attach("Results", driver.browser.page_source, AttachmentType.HTML)
	assert page.is_element_present('success_msg')
	

'''def test_login_new(webdriver):
	visit(url)
	page = BasiliskPage(driver = driver.browser)
	page.login_link.click()
	wait(lambda: page.is_element_present('log_btn'))
	page.login(login, passw)
	wait(lambda: page.is_element_present('log_menu'))
	allure.attach("Results", driver.browser.page_source, AttachmentType.HTML)
	assert page.is_element_present('log_menu')'''




if __name__ == '__main__':
	driver.browser = Firefox()
	test_reg_valid(driver.browser)
	