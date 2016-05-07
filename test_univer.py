from selenium.webdriver import Firefox
from webium.wait import wait
from allure.constants import AttachmentType
import allure
import time
from basilisk import *
import pytest
from config import *
from faker import Faker
fake = Faker()

url = "http://basilisk.fintegro.com/"
user = "superadmin" 
passw =  "123123"

def test_add_univer(webdriver, univer):
	visit(url)
	page = BasiliskPage(driver = driver.browser)
	page.login_link.click()
	wait(lambda: page.is_element_present('log_btn'))
	page.login(user, passw)
	wait(lambda: page.is_element_present('university'))
	page.university.click()
	page = UniversityListPage(driver = driver.browser)
	wait(lambda: page.is_element_present('univer_add'))
	page.univer_add.click()
	page = UniverPage(driver = driver.browser)
	wait(lambda: page.is_element_present('save_btn'))
	page.add_univer(univer)
	page = UniversityListPage(driver = driver.browser)
	wait(lambda: page.is_element_present('univer_add'))
	allure.attach("Results", driver.browser.page_source, AttachmentType.HTML)
	assert univer['name'] == page.univer_list[-1].text

'''def test_edit_univer(webdriver):
	visit(url)
	page = BasiliskPage(driver = driver.browser)
	page.login_link.click()
	wait(lambda: page.is_element_present('log_btn'))
	page.login(user, passw)
	wait(lambda: page.is_element_present('university'))
	page.university.click()
	page = UniversityListPage(driver = driver.browser)
	wait(lambda: page.is_element_present('univer_add'))
	page.univer_links[5].click()
	page = UniverPage(driver = driver.browser)
	wait(lambda: page.is_element_present('add_admin'))
	name = page.name.get_attribute('value') 
	set_value(page.name, name + ' edited')
	page.save_btn.click()
	page = UniversityListPage(driver = driver.browser)
	wait(lambda: page.is_element_present('univer_add'))
	page.univer_links[5].click()
	page = UniverPage(driver = driver.browser)
	wait(lambda: page.is_element_present('name'))
	if page.name.get_attribute('value') == name + ' edited':
		set_value(page.name, name)
		page.save_btn.click()
	else:
		pytest.fail("Wrong edited name")
'''



if __name__ == '__main__':
	name = fake.company()
	address = fake.address()
	exp_date = fake.date()
	limits = fake.random_int(min=0, max=9999)
	note = fake.sentence(nb_words=6, variable_nb_words=True)
	univer = {'name':name, 'address':address, 'exp_date':exp_date, 'limits':limits, 'note':note}
	driver.browser = Firefox()
	test_add_univer(driver.browser, univer)
	