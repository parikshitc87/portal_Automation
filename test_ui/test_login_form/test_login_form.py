from playwright.sync_api import expect

from Helper_Modules.Test_Data import data_gen
from Page_Elements.Registration_Pages_Elements.registration_page_elements import RegistrationPage


def test_incorrect_email_format(set_up):
	page = set_up
	page.locator(RegistrationPage.login_button)