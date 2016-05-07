from selenium.webdriver import Firefox
from webium.wait import wait
import time
from basilisk import *
from config import *

url = "http://basilisk.fintegro.com/"

def test_media(webdriver):
	visit(url)
	driver.browser.maximize_window()
	page = BasiliskPage(driver = driver.browser)
	page.create_quiz.click()
	page = CreateQuizPage(driver = driver.browser)
	#time.sleep(1)
	wait(lambda: page.is_element_present('publish'))
	#page.media_image.click()
	#page.media_image.clear()
	page.media.send_keys(r"d:\barsik.jpg")


if __name__ == '__main__':
	driver.browser = Firefox()
	test_media(driver.browser)