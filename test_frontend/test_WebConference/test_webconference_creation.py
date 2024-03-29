from Helper_Modules.Common_Functions.portal import login_with
from Helper_Modules.Test_Data import data_gen
from Page_Elements.HomePage_Elements.feed_post_elements import FeedPage
from Page_Elements.WebConferencePage_Elements.webconference_page_elements import ConferencePage


def test_create_conference_buttons_presence(set_up):  # verifying page elements
	page = set_up
	login_with(page, data_gen.webconf_creator)
	flag = 0
	page.wait_for_load_state("domcontentloaded")
	page.get_by_role("link", name="Web conferences").click()
	page.wait_for_load_state("domcontentloaded")
	page.locator("[data-test-id=\"PageNavMenu\"] [data-test-id=\"Btn\"]").click()
	page.locator("header:has-text(\"Create a web conference\")").get_by_role("button").click()
	flag += 1
	page.locator("[data-test-id=\"PageOverview\"]").get_by_role("button", name="New conference").click()
	page.get_by_role("heading", name="Create a web conference").click()
	page.locator("header:has-text(\"Create a web conference\")").get_by_role("button").click()
	flag += 1
	assert (flag == 2)


def test_public_webconference_creation(set_up):  # Create a Public Webconference
	page = set_up
	login_with(page, data_gen.webconf_creator)
	page.wait_for_load_state("domcontentloaded")
	page.get_by_role("link", name="Web conferences").click()
	page.wait_for_load_state("domcontentloaded")
	page.locator(ConferencePage.conference_rooms_tab).click()
	page.wait_for_load_state("domcontentloaded")
	page.locator("[data-test-id=\"EntityItem\"]").get_by_text("Standard conference room").click()
	page.wait_for_load_state("domcontentloaded")
	page.get_by_role("link", name="Create web conference").click()
	page.locator(ConferencePage.conference_name).fill(data_gen.name() + " " + data_gen.unique_string())
	page.locator(ConferencePage.date).fill(data_gen.first_of_next_month())
	page.locator(ConferencePage.hh).fill("2")
	page.locator(ConferencePage.next_button).click()
	page.locator(ConferencePage.next_button).click()
	page.locator(ConferencePage.create_button).click()
	page.wait_for_selector(ConferencePage.conference_creation_success_message)
	assert page.locator(ConferencePage.conference_creation_success_message).is_visible()


def test_private_webconference_creation(set_up):  # Create a Closed Webconference
	page = set_up
	login_with(page, data_gen.webconf_creator)
	page.wait_for_load_state("domcontentloaded")
	page.get_by_role("link", name="Web conferences").click()
	page.wait_for_load_state("domcontentloaded")
	page.locator(ConferencePage.conference_rooms_tab).click()
	page.wait_for_load_state("domcontentloaded")
	page.locator("[data-test-id=\"EntityItem\"]").get_by_text("Standard conference room").click()
	page.wait_for_load_state("domcontentloaded")
	page.get_by_role("link", name="Create web conference").click()
	page.locator(ConferencePage.conference_name).fill(data_gen.name() + " " + data_gen.unique_string())
	page.locator(ConferencePage.date).fill(data_gen.first_of_next_month())
	page.locator(ConferencePage.hh).fill("2")
	page.locator(ConferencePage.next_button).click()
	page.locator(ConferencePage.closed_conference_radio_button).click()
	page.locator(ConferencePage.next_button).click()
	page.locator(ConferencePage.create_button).click()
	page.wait_for_selector(ConferencePage.conference_creation_success_message)
	assert page.locator(ConferencePage.conference_creation_success_message).is_visible()
	#//span[text() = "Copper 0305202317064657"]//parent::span//parent::main//parent::article//parent::div//parent::div//parent::article//child::div[@class='hidden ml-2 md:block']
	#//*[text() = "📎 File"]
	#U+1F4CE