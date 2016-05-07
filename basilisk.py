from webium import BasePage, Find, Finds
from webium.controls.link import Link
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure
import driver
import time
from faker import Faker
fake = Faker()

class BasiliskPage(BasePage):
	login_link = Find(Link, By.XPATH, ".//*[@id='w1']/li/a")
	logout = Find(Link, By.XPATH, ".//*[@id='w2']/li[4]/a")
	reg_link = Find(by = By.CSS_SELECTOR, value = ".login-link.signUpModal-btn>mark")
	university = Find(Link, By.XPATH, "//a[contains(text(), 'Univer')]")
	login_field = Find(by = By.XPATH, value = ".//*[@id='login-form-login']")
	password_field = Find(by = By.XPATH, value = ".//*[@id='login-form-password']")
	log_btn = Find(by = By.CSS_SELECTOR, value = ".btn.btn-primary.btn-block.btn-login")

	create_quiz = Find(by = By.CSS_SELECTOR, value = ".circule-btn.quize-create-link")
	explore = Find(Link, By.XPATH, "//a[contains(text(), 'Explore')]")

	quizes = Find(by = By.XPATH, value = ".//td[contains(text(), 'Quizes')]")
	quiz_fac = Find(by = By.XPATH, value = ".//*/table/tbody/tr/td[1]") 
	take_dep = Find(by = By.XPATH, value = ".//*/table/tbody/tr[2]/td[1]")
	create_dep = Find(by = By.XPATH, value = ".//td[contains(text(),'Create')] ")
	quiz_header = Find(by = By.XPATH, value = ".//span[contains(text(), 'Quizes')]") 

	quiz_list = Finds(by = By.XPATH, value = ".//tr[@class = 'start-quiz']")
	start_quiz = Find(by = By.ID, value = "start-quiz-ok")

	log_menu = Find(by = By.CSS_SELECTOR, value = ".dropdown-toggle")
	title = Find(by = By.CSS_SELECTOR, value = ".title")

	users = Find(by = By.XPATH, value = ".//a[contains(text(), 'Users')]")

	on = Find(by = By.CSS_SELECTOR, value = ".bootstrap-switch-handle-on.bootstrap-switch-success")
	off = Find(by = By.CSS_SELECTOR, value = ".bootstrap-switch-handle-off.bootstrap-switch-danger")
	status = Find(by = By.ID, value = "university-status")
	disable_pass = Find(by = By.ID, value = "js-confirm-disable-pass")
	change = Find(by = By.ID, value = "modal-change")

	@allure.step('Login')
	def login(self, user, passw):
		set_value(self.login_field, user)
		set_value(self.password_field, passw)
		self.log_btn.click()	


class RegistrationPage(BasiliskPage):
	firstname = Find(by = By.ID, value = "register-form-first_name")
	lastname = Find(by = By.ID, value = "register-form-last_name")
	login = Find(by = By.ID, value = "register-form-username")
	password = Find(by = By.ID, value = "register-form-password")
	confirm_passw = Find(by = By.ID, value = "register-form-confirmpassword")
	email_address = Find(by = By.ID, value = "register-form-email")
	promo = Find(by = By.ID, value = "promo")
	univer = Find(by = By.ID, value = "univ-autocomplete-field")
	button_reg = Find(by = By.CSS_SELECTOR, value = ".btn.btn-success.btn-block.btn-sign-up")
	success_msg = Find(by = By.CSS_SELECTOR, value = ".alert.alert-info")
	
	@allure.step('Registration')
	def register(self, fname, lname, login, passw, confirm_passw, email, promo, univer):
		set_value(self.firstname, fname)
		set_value(self.lastname, lname)
		set_value(self.login, login)
		set_value(self.password, passw)
		set_value(self.confirm_passw, confirm_passw)
		set_value(self.email_address, email)
		set_value(self.promo, promo)
		set_value(self.univer, univer)
		time.sleep(1)
		self.univer.send_keys(Keys.ARROW_DOWN)
		self.univer.send_keys(Keys.TAB)
		self.button_reg.click()

class UniverPage(BasiliskPage):
	name = Find(by = By.ID, value = "university-name_ln")
	address = Find(by = By.ID, value = "university-address")
	exp_date = Find(by = By.ID, value = "university-accaunt_expiry_dt")
	limits = Find(by = By.ID, value = "university-students_limmit")
	note = Find(by = By.ID, value = "university-note")
	save_btn = Find(by = By.ID, value = "createUniv")
	add_admin = Find(by = By.CSS_SELECTOR, value = ".btn.link.btn-add")
	email_list = Finds(by = By.XPATH, value = ".//a//div[2]")
	faculty_dep = Find(by = By.ID, value = "university-facultiesanddepartmentscount")

	
	@allure.step('Add Univer')
	def add_univer(self, univer):
		set_value(self.name, univer['name'])
		set_value(self.address, univer['address'])
		set_value(self.exp_date, univer['exp_date'])
		set_value(self.limits, univer['limits'])
		set_value(self.note, univer['note'])
		self.save_btn.click()

class UniverAdminPage(BasiliskPage):
	name = Find(by = By.ID, value = "user-first_name")
	lastname = Find(by = By.ID, value = "user-last_name")
	username = Find(by = By.ID, value = "user-username")
	email = Find(by = By.ID, value = "user-email")
	passw = Find(by = By.ID, value = "user-password")
	confirm_passw = Find(by = By.ID, value = "user-confirmpassword")
	save = Find(by = By.ID, value = "save-univAdmin")
	

	@allure.step('Add Univer Admin')
	def add_uadmin(self, name, lname, uname, email, passw, confirm_passw):
		set_value(self.name, name)
		set_value(self.lastname, lname)
		set_value(self.username, uname)
		set_value(self.email, email)
		set_value(self.passw, passw)
		set_value(self.confirm_passw, confirm_passw)
		self.save.click()


class UniversityListPage(BasiliskPage):
	univer_add = Find(by = By.CSS_SELECTOR, value = ".btn.btn-add.link.uni-create")
	univer_list = Finds(by = By.XPATH, value = ".//tr[@class='link']/td[1]")
	univer_links = Finds(by = By.XPATH, value = ".//tr[@class = 'link']")
	search_field = Find(by = By.ID, value = "search-input")


	@allure.step('Search Univer')
	def search(self, text):
		set_value(self.search_field, text)
		self.search_field.send_keys(Keys.RETURN)

class TeachersListPage(BasiliskPage):
	add_teacher = Find(by = By.CSS_SELECTOR, value = ".btn.btn-add.link")
	teachers_list = Finds(by = By.XPATH, value = ".//tr/td")
	links = Finds(by = By.XPATH, value = ".//tr[@class = 'link']")

class TeacherPage(BasiliskPage):
	name = Find(by = By.ID, value = "user-first_name")
	username = Find(by = By.ID, value = "user-username")
	teacher_email = Find(by = By.ID, value = "user-email")
	passw = Find(by = By.ID, value = "user-password")
	confirm_passw = Find(by = By.ID, value = "user-confirmpassword")
	save = Find(by = By.CSS_SELECTOR, value = ".btn.create-teacher-btn.univ-main.center")

	@allure.step('Add Teacher')
	def add_teacher(self, name, uname, email, passw, confirm_passw):
		set_value(self.name, name)
		set_value(self.username, uname)
		set_value(self.teacher_email, email)
		set_value(self.passw, passw)
		set_value(self.confirm_passw, confirm_passw)
		self.save.click()

class FacultyListPage(BasiliskPage):
	add = Find(by = By.CSS_SELECTOR, value = ".btn.btn-add.link")
	name = Find(by = By.ID, value = "faculty-name")
	save = Find(by = By.XPATH, value = ".//*[@id='faculty_create']//button")
	univer_faculties = Finds(by = By.XPATH, value = ".//tr/td[1]")
	all_faculties = Finds(by = By.XPATH, value = ".//*[@id='ui-id-1']/li")

class CreateQuizPage(BasiliskPage):
	question = Finds(by = By.XPATH, value = ".//*/div[1]/div/div/textarea")
	variants = Finds(by = By.XPATH, value = ".//*/div[2]/div[1]/div/textarea")
	tag = Finds(by = By.XPATH, value = ".//table[1]//td[2]/input")
	add_tag = Finds(by = By.XPATH, value = ".//table[1]//td[3]/a/span")
	question_new = Find(by = By.ID, value = "add-question-button")
	publish = Find(by = By.CSS_SELECTOR, value = ".quize--exit") 
	media = Find(by = By.ID, value = "uploadform-questionmedia") 

	def create_quiz(self, n, q):
		for j in range(n):
			set_value(self.question[j], str(j+1) + " " +  fake.text())
			set_value(self.tag[j], fake.word())
			self.add_tag[j].click()
			for i in range(q):
				k = j*4 + i
				set_value(self.variants[k], fake.sentences(nb=3))
			if j != n-1:
				self.question_new.click()
				time.sleep(1)

class PublishQuizPage(BasiliskPage):
	name = Find(by = By.ID, value = "quizes-quiz_name")
	department = Find(by = By.XPATH, value = ".//*[@id='quiz-publish-form']/div[2]/div[1]/input")
	course_code = Find(by = By.ID, value = "quizes-course_code")
	istimed = Find(by = By.ID, value = "quizes-istimed")
	timer_value = Find(by = By.ID, value = "quizes-timer_value")
	publish_btn = Find(by = By.XPATH, value = ".//*[@id='quiz-publish-form']/div[5]/div/button")
	success_msg = Find(by = By.CSS_SELECTOR, value = ".alert.alert-success") 
	
	def publish(self, name, dep, code, timer):
		set_value(self.name, name)
		set_value(self.department, dep)
		time.sleep(1)
		self.department.send_keys(Keys.ARROW_DOWN)
		self.department.send_keys(Keys.TAB)
		set_value(self.course_code, code)
		self.istimed.click()
		set_value(self.timer_value, timer)
		#self.publish_btn.click()

class TakeQuizPage(BasiliskPage):
	variants = Finds(by = By.XPATH, value = ".//*[@class='custom-col input-dublicate variant-text']")
	next_question = Find(by = By.ID, value = "next-question")

@allure.step('Open the site Basilisk')
def visit(url):
    driver.browser.get(url)

@allure.step('Set Value')
def set_value(element, value):
	element.clear()
	element.send_keys(value)