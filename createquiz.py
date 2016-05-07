from selenium.webdriver import Firefox
from webium.wait import wait
import time
from basilisk import *
import pytest
from allure.constants import AttachmentType
import allure
from config import *
import webium.settings
from faker import Faker
fake = Faker()
webium.settings.wait_timeout = 5
url = "http://basilisk.fintegro.com/"

def test_create_quiz(webdriver):
	user="mihac"
	passw = "789789"
	visit(url)
	driver.browser.maximize_window()
	page = BasiliskPage(driver = driver.browser)
	page.login_link.click()
	wait(lambda: page.is_element_present('log_btn'))
	page.login(user, passw)
	wait(lambda: page.is_element_present('log_menu'))
	page.create_quiz.click()
	page = CreateQuizPage(driver = driver.browser)
	#time.sleep(1)
	wait(lambda: page.is_element_present('publish'))
	page.create_quiz(25, 0)
	'''page.publish.click()
	page = PublishQuizPage(driver = driver.browser)
	wait(lambda: page.is_element_present('name'))
	page.publish('AutoQuiz', 'Department 1', "a", '50')'''

	
if __name__ == '__main__':
	driver.browser = Firefox()
	test_create_quiz(driver.browser)