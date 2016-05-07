from selenium.webdriver import Firefox
from webium.wait import wait
from selenium.webdriver.common.keys import Keys
import time
from myroz import *
import pytest
from config import *
import webium.settings
webium.settings.wait_timeout = 5
url = "http://myroz.com/"
user="testsoft55555@gmail.com"
passw = "111111"

def test_login(webdriver):
	visit(url)
	driver.browser.maximize_window()
	page = MyRozPage(driver = driver.browser)
	page.login_link.click()
	wait(lambda: page.is_element_present('login_btn'))
	page.login(user, passw)
	time.sleep(3)
	visit('http://myroz.com/add-flight')
	time.sleep(3)
	page.dron_id.click()
	page.search.send_keys('test')
	page.search.send_keys(Keys.ENTER)
	#time.sleep(3)
	#page.test_id.click()


if __name__ == '__main__':
	driver.browser = Firefox()
	test_login(driver.browser)
	