from playwright.sync_api import expect

from Helper_Modules.Test_Data import data_gen
from Page_Elements.Registration_Pages_Elements.registration_page_elements import RegistrationPage


# Registration Form - Test if the elements are loaded on the Registration form
def test_registration_form_element_presence(set_up):
	page = set_up
	flag = True
	page.locator(RegistrationPage.email_input_field).fill("test")
	for element in RegistrationPage.page_elements:
		if page.locator(element).is_hidden():
			flag = False
	assert flag is True


# Registration Form - Test the presence of error messages on page
def test_registration_form_blank_field_error_message_contracted(set_up):
	page = set_up
	page.locator(RegistrationPage.create_button).click()
	assert page.get_by_text("This field is required.").count() is 4


def test_registration_form_blank_field_error_message_expanded(set_up):
	page = set_up
	page.locator(RegistrationPage.email_input_field).fill("..")
	page.locator(RegistrationPage.create_button).click()
	assert page.get_by_text("This field is required.").count() is 3


# Registration Form - Email field - test set of valid emails
def test_email_field_valid_emails(set_up):
	page = set_up
	flag = 0
	for email in data_gen.valid_emails:
		page.get_by_placeholder("Email").fill(email)
		if page.get_by_text("Please provide a valid email address.").count() == 0:
			flag += 1
		else:
			print("Validation failed for ::" + " " + email)
	assert len(data_gen.valid_emails) == flag


# Registration form - Email field - test set of invalid emails
def test_email_field_invalid_emails(set_up):
	page = set_up
	flag = 0
	for email in data_gen.invalid_emails:
		page.get_by_placeholder("Email").fill(email)
		page.keyboard.press("Shift+Tab")
		page.wait_for_selector()
		page.wait_for_timeout(25)
		if page.get_by_text("Please provide a valid email address.").count() == 1:
			flag += 1
		# page.wait_for_timeout(2000)
		else:
			print("Validation failed for :: " + " " + email)
	assert len(data_gen.invalid_emails) == flag


# Registration Form - Test TOS and Privacy policy links
def test_registration_form_tos(set_up):
	page = set_up
	flag = False
	page.locator(RegistrationPage.email_input_field).fill('..')
	with page.expect_popup() as popup_info:
		page.get_by_role("link", name="terms of use").click()
	page1 = popup_info.value
	expect(page1.get_by_role("heading", name="Terms of use AVACO – Private")).to_be_visible()


def test_registration_form_privacy_policy(set_up):
	page = set_up
	flag = False
	page.locator(RegistrationPage.email_input_field).fill('..')
	with page.expect_popup() as popup_info:
		page.locator("//a[text()=\"privacy policy\"]").click()
	page1 = popup_info.value
	expect(page1.get_by_role("heading", name="1. How does our network work and what is a so-called platform?")).to_be_visible()


def test_password_tooltip(set_up):
	page = set_up
	flag = False
	page.locator(RegistrationPage.password_input_field).fill('..')
	assert RegistrationPage.is_tooltip_displayed(page)


def test_password_mismatch_error_message(set_up):
	page = set_up
	flag = False
	page.locator(RegistrationPage.password_input_field).fill(data_gen.get_random_name()+data_gen.get_random_name()+data_gen.get_random_name())
	page.locator(RegistrationPage.confirm_password_input_field).fill(data_gen.get_random_name())
	assert RegistrationPage.is_password_mismatch_error_displayed(page)


def test_password_min_eight_char_error(set_up):
	page = set_up
	page.locator(RegistrationPage.password_input_field).fill('..')
	page.wait_for_timeout(25)
	flag1 = RegistrationPage.is_password_should_be_eight_char_error_displayed(page)
	page.locator(RegistrationPage.password_input_field).fill('........')
	page.wait_for_timeout(25)
	flag2 = RegistrationPage.is_password_should_be_eight_char_error_displayed(page)
	assert flag1 is True and flag2 is False
