from webium import BasePage, Find, Finds
from webium.controls.link import Link
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import driver
import time


class MyRozPage(BasePage):
	login_link = Find(by = By.CSS_SELECTOR, value = ".btn-login")
	login_field = Find(by = By.ID, value = "login-form-login")
	password_field = Find(by = By.ID, value = "login-form-password")
	login_btn = Find(by = By.XPATH, value = ".//*[@id='w1']/button")
	dron_id = Find(by = By.XPATH, value = ".//*[@id='dropbox']/span/span[1]/span")
	search = Find(by = By.XPATH, value = "html/body/span/span/span[1]/input")
	test_id = Find(by = By.ID, value = "select2-flight-drone_id-result-ghpc-58")

	def login(self, user, passw):
		set_value(self.login_field, user)
		set_value(self.password_field, passw)
		self.login_btn.click()	

def visit(url):
    driver.browser.get(url)

def set_value(element, value):
	element.clear()
	element.send_keys(value)

	