from playwright.sync_api import expect

from Helper_Modules.Common_Functions.portal import login_with
from Helper_Modules.Test_Data import data_gen
from Page_Elements.Registration_Pages_Elements import registration_page_elements
from Page_Elements.Registration_Pages_Elements.registration_page_elements import RegistrationPage
from Page_Elements.login_page_elements import LoginPage


def test_registration_form_element_presence(set_up):  # Registration Form - Test if the elements are loaded on the Registration form
	page = set_up
	flag = True
	page.locator(RegistrationPage.email_input_field).fill("test")
	for element in RegistrationPage.page_elements:
		if page.locator(element).is_hidden():
			flag = False
	assert (flag == True)


# @pytest.mark.regression
def test_registration_form_validations_1(set_up):  # Registration Form - Tests the presence of error messages on page
	page = set_up
	page.get_by_role("button", name="Create account").click()
	assert page.get_by_text("This field is required.").count() == 4


def test_email_field_3(set_up):  # Registration Form - Email field - test set of valid emails
	page = set_up
	flag = 0
	for email in data_gen.valid_emails:
		page.get_by_placeholder("Email").fill(email)
		if page.get_by_text("Please provide a valid email address.").count() == 0:
			flag += 1
		else:
			assert False
	assert len(data_gen.valid_emails) == flag


def test_email_field_invalid_emails(set_up):  # Registration form - Email field - test set of invalid emails
	page = set_up
	flag = 0
	for email in data_gen.invalid_emails:
		page.get_by_placeholder("Email").fill(email)
		page.keyboard.press("Shift+Tab")
		page.wait_for_timeout(25)
		page.wait_for_load_state("domcontentloaded")
		if page.get_by_text("Please provide a valid email address.").count() == 1:
			flag += 1
		# page.wait_for_timeout(2000)
		else:
			print("Validation failed for :: " + " " + email)
	assert len(data_gen.invalid_emails) == flag
