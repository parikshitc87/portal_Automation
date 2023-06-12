from playwright.sync_api import expect

from Helper_Modules.Test_Data import data_gen
from Page_Elements.HomePage_Elements.home_page import HomePage


def test_contact_support_form_validations(login_private_person):
	page = login_private_person
	page.get_by_role("button", name="Help").click()
	page.get_by_role("button", name="Contact support").click()
	page.get_by_role("button", name="Submit issue").click()
	assert page.locator('text = This field is required.').count() is 2


def test_contact_support_funtionality(login_private_person):
	page = login_private_person
	page.get_by_role("button", name="Help").click()
	page.get_by_role("button", name="Contact support").click()
	subject = data_gen.unique_string()
	page.get_by_placeholder("Subject").fill(subject)
	details = data_gen.unique_string()
	page.get_by_placeholder("e.g. Account issues, Report user, ...").fill(details)
	page.get_by_role("button", name="Submit issue").click()
	expect (page.get_by_text("Your support request has been submitted successfully.")).to_be_visible() \
		and (page.get_by_text("Request sent")).to_be_visible()


def test_contact_support_character_length(login_private_person):
	page = login_private_person
	page.get_by_role("button", name="Help").click()
	page.get_by_role("button", name="Contact support").click()
	subject = data_gen.unique_string()
	flag1 = page.get_by_text("0 / 50").is_visible()
	page.get_by_placeholder("Subject").fill('1')
	flag2 = page.get_by_text("0 / 50").is_hidden() and page.get_by_text("1 / 50")
	page.get_by_placeholder("Subject").fill('11111111111111111111111111111111111111111111111111')
	flag3 =  page.get_by_text("50 / 50").is_visible()
	assert flag1 and flag2 and flag3


def test_contact_support_confirmation_popup(login_private_person):
	page = login_private_person
	page.get_by_role("button", name="Help").click()
	page.get_by_role("button", name="Contact support").click()
	subject = data_gen.unique_string()
	page.get_by_placeholder("Subject").fill(subject)
	page.get_by_role("button", name="Cancel").click()
	flag1 = page.get_by_role("heading", name="Notice").is_visible() \
	        and page.get_by_text("When the pop-up is closed, all entries are lost!").is_visible()
	page.get_by_role("button", name="Close").click()
	flag2 = page.get_by_role("button", name="Submit issue").is_hidden()
	page.get_by_role("button", name="Help").click()
	page.get_by_role("button", name="Contact support").click()
	page.get_by_placeholder("Subject").fill(subject)
	page.locator("header:has-text(\"Contact support\")").get_by_role("button").click()
	page.get_by_role("button", name="Back").click()
	flag3 = page.get_by_role("button", name="Submit issue").is_visible()
	assert flag1 and flag2 and flag3