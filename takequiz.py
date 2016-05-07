from selenium.webdriver import Firefox
from webium.wait import wait
import time
from basilisk import *
import pytest
from allure.constants import AttachmentType
import allure
from config import *
import random

url = "http://basilisk.fintegro.com/"

def test_take_quiz(webdriver):
	user="mihac"
	passw = "789789"
	visit(url)
	driver.browser.maximize_window()
	page = BasiliskPage(driver = driver.browser)
	page.login_link.click()
	wait(lambda: page.is_element_present('log_btn'))
	page.login(user, passw)
	wait(lambda: page.is_element_present('log_menu'))
	page.explore.click()
	wait(lambda: page.is_element_present('quizes'))
	page.quizes.click()
	wait(lambda: page.is_element_present('quiz_fac'))
	time.sleep(1)
	page.quiz_fac.click()	
	wait(lambda: page.is_element_present('take_quiz'))
	time.sleep(1)
	page.take_quiz.click()
	wait(lambda: page.is_element_present('quiz_header'))
	time.sleep(1)
	if len(page.quiz_list) !=0:
		page.quiz_list[1].click()
		page.start_quiz.click()
		page = TakeQuizPage(driver = driver.browser)
		wait(lambda: page.is_element_present('next_question'))
		for i in range(3):
			k = i*4 
			page.variants[k].click()
			page.next_question.click()


def test_take_quiz(webdriver, q):
	file = open('users_1.txt', 'r')
	data = file.readlines()
	visit(url)
	driver.browser.maximize_window()
	page = BasiliskPage(driver = driver.browser)
	for u in range(len(data)):
		user = data[u].split()
		page.login_link.click()
		wait(lambda: page.is_element_present('log_btn'))
		page.login(user[0], user[1])
		wait(lambda: page.is_element_present('log_menu'))
		page.explore.click()
		wait(lambda: page.is_element_present('quizes'))
		page.quizes.click()
		wait(lambda: page.is_element_present('quiz_fac'))
		time.sleep(1)
		page.quiz_fac.click()	
		wait(lambda: page.is_element_present('create_dep'))
		time.sleep(1)
		page.create_dep.click()
		wait(lambda: page.is_element_present('quiz_header'))
		time.sleep(1)
		if len(page.quiz_list) !=0:
			page.quiz_list[-1].click()
			page.start_quiz.click()
			page = TakeQuizPage(driver = driver.browser)
			wait(lambda: page.is_element_present('next_question'))
			r = int(user[2])
			for i in range(q):
				k = i*2
				if r !=0 :
					page.variants[k].click()
					page.next_question.click()
					r -= 1
				elif i < q:
					page.variants[k+1].click()
					page.next_question.click()
		time.sleep(5)
		if u < len(data) - 1:
			page.login_link.click()
			page.logout.click()

def test_take_quiz_random(webdriver, q):
	file = open('users_1.txt', 'r')
	data = file.readlines()
	visit(url)
	driver.browser.maximize_window()
	page = BasiliskPage(driver = driver.browser)
	for u in range(len(data)):
		user = data[u].split()
		page.login_link.click()
		wait(lambda: page.is_element_present('log_btn'))
		page.login(user[0], user[1])
		wait(lambda: page.is_element_present('log_menu'))
		page.explore.click()
		wait(lambda: page.is_element_present('quizes'))
		page.quizes.click()
		wait(lambda: page.is_element_present('quiz_fac'))
		time.sleep(1)
		page.quiz_fac.click()	
		wait(lambda: page.is_element_present('take_dep'))
		time.sleep(1)
		page.take_dep.click()
		wait(lambda: page.is_element_present('quiz_header'))
		time.sleep(1)
		if len(page.quiz_list) !=0:
			page.quiz_list[-1].click()
			page.start_quiz.click()
			page = TakeQuizPage(driver = driver.browser)
			wait(lambda: page.is_element_present('next_question'))
			for i in range(q):
				#r = random.choice([0,1])
				r = random.randrange(0, 2)
				page.variants[r].click()
				page.next_question.click()
		time.sleep(5)
		if u < len(data) - 1:
			page.login_link.click()
			page.logout.click()

def users():
	file = open('users_3.txt', 'r')
	user = file.readlines()
	print len(user)
	
if __name__ == '__main__':
	driver.browser = Firefox()
	test_take_quiz_random(driver.browser, 5)
	#users()