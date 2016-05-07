from selenium.webdriver import Firefox
from webium.wait import wait
import time
from datetime import datetime
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

def test_create_quiz_1(webdriver):
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
	wait(lambda: page.is_element_present('publish'))
	page.create_quiz(50, 2)
	page.publish.click()
	page = PublishQuizPage(driver = driver.browser)
	wait(lambda: page.is_element_present('name'))
	page.publish("Quiz_50 " + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), 'Create Quiz', "c1", '5')
	page.publish_btn.click()
	allure.attach("Results", driver.browser.page_source, AttachmentType.HTML)
	time.sleep(1)
	assert page.is_element_present('success_msg')

if __name__ == '__main__':
	driver.browser = Firefox()
	test_create_quiz_1(driver.browser)