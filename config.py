import pytest
from selenium.webdriver import Firefox
from selenium import webdriver as wd
import driver
#import MySQLdb as mdb
from faker import Faker


@pytest.fixture()
def webdriver(request):
	driver.browser = Firefox()
	#driver.browser = wd.Chrome('/home/developer/python/chromedriver')
	request.addfinalizer(driver.browser.quit)


@pytest.fixture()
def superadmin():
	return ["superadmin", "123123"]
	

'''@pytest.fixture()
def univer(request):
	fake = Faker()
	name = fake.company()
	address = fake.address()
	exp_date = fake.date()
	limits = fake.random_int(min=0, max=9999)
	note = fake.sentence(nb_words=6, variable_nb_words=True)
	univer = {'name':name, 'address':address, 'exp_date':exp_date, 'limits':limits, 'note':note}
	def teardown():
		con = mdb.connect('fintegro.ca', '', '', 'basilisk_db');
		with con: 
			cur = con.cursor()
			cur.execute("DELETE FROM university WHERE name_ln = '" + univer['name'] + "'")
	request.addfinalizer(teardown)
	return univer
'''


