from playwright.sync_api import expect

from Helper_Modules.Test_Data import data_gen
from Page_Elements.Registration_Pages_Elements.registration_page_elements import RegistrationPage


def test_incorrect_email_format(set_up):
	page = set_up
	with page.expect_popup() as popup_info:
		page.locator(RegistrationPage.login_button_top).click()
	page1 = popup_info.value
	page1.locator("//input[@id='login-email']").fill("test space@pk.avaco.io")
	page1.get_by_label("Password").fill("Avaco000")
	page1.locator("//button[@class='btn btn-black']").click()
	expect(page1.get_by_text("The email/password you entered is incorrect.")).to_be_visible()