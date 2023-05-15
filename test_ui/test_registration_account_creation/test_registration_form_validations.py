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
def test_registration_form_blank_field_error_message(set_up):
	page = set_up
	page.locator(RegistrationPage.create_button).click()
	assert page.get_by_text("This field is required.").count() is 4


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
		page.wait_for_timeout(25)
		page.wait_for_load_state("domcontentloaded")
		if page.get_by_text("Please provide a valid email address.").count() == 1:
			flag += 1
		# page.wait_for_timeout(2000)
		else:
			print("Validation failed for :: " + " " + email)
	assert len(data_gen.invalid_emails) == flag


# Registration Form - Test TOS and Privacy policy links
def test_registration_form_tos_privacy_policy(set_up):
	page = set_up
	flag = False
	with page.expect_popup() as popup_info:
		page.get_by_role("link", name="terms of use").click()
	page1 = popup_info.value
	page.wait_for_url("https://portal-dev.dev.otc.workpage.io/terms-person?user=demo&password=portal")
	if page1.get_by_role("heading", name="Terms of use AVACO – Private").is_visible():
		flag = True
	page1.close()
	with page.expect_popup() as popup_info:
		page.get_by_role("link", name="privacy policy").click()
	page2 = popup_info.value
	page.wait_for_url("https://portal-dev.dev.otc.workpage.io/terms-person?user=demo&password=portal")
	if page2.get_by_role():
		return
	page2.close()
