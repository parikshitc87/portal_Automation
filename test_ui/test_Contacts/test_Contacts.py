from Helper_Modules.Test_Data import data_gen
from Page_Elements.HomePage_Elements.feed_post_elements import FeedPage
from Page_Elements.HomePage_Elements.home_page import HomePage
from Page_Elements.ProfilePage_Elements.profile_page import ProfilePage
from Page_Elements.SearchResultsPage_Elements.search_results_page_elements import SearchPage


def test_send_contact_request_one(login_company):  #
	page = login_company
	page.wait_for_load_state("domcontentloaded")
	page.wait_for_load_state("networkidle")
	page.locator(HomePage.search_box).fill(data_gen.search_string_contact1)  # change this data
	page.keyboard.press("Enter")
	page.wait_for_load_state("domcontentloaded")
	page.wait_for_load_state("networkidle")
	page.locator(SearchPage.search_result_test_contact1).click()
	page.wait_for_load_state("domcontentloaded")
	page.wait_for_load_state("networkidle")
	try:
		page.locator(ProfilePage.add_contact_button).click()
	except:
		page.locator(ProfilePage.contact_sent_request_button).click()
		page.wait_for_load_state("domcontentloaded")
		page.locator(ProfilePage.contact_cancel_request_confirmation).click()


def test_send_contact_request_two(login_company):  #
	page = login_company
	page.wait_for_load_state("domcontentloaded")
	page.wait_for_load_state("networkidle")
	page.locator(HomePage.search_box).fill(data_gen.search_string_contact1)
	page.keyboard.press("Enter")
	page.wait_for_load_state("domcontentloaded")
	page.wait_for_load_state("networkidle")
	page.locator(SearchPage.search_result_test_contact1).click()
	page.wait_for_load_state("domcontentloaded")
	page.wait_for_load_state("networkidle")
	try:
		page.locator(ProfilePage.add_contact_button).click()
	except:
		page.locator(ProfilePage.contact_sent_request_button).click()
		page.wait_for_load_state("domcontentloaded")
		page.locator(ProfilePage.contact_cancel_request_confirmation).click()
		page.wait_for_load_state("domcontentloaded")
		page.wait_for_load_state("networkidle")
		page.locator(ProfilePage.add_contact_button).click()
	page.wait_for_load_state("domcontentloaded")
	page.wait_for_load_state("networkidle")
	page.locator(FeedPage.contacts_link).click()
