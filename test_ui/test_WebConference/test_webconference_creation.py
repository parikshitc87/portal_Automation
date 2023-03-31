from Helper_Modules.Test_Data import data_gen
from Page_Elements.HomePage_Elements.feed_post_elements import FeedPage
from Page_Elements.WebConferencePage_Elements.webconference_page_elements import ConferencePage


def test_public_webconference_creation(login_company):  # Create a Public Webconference
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    # page.locator(FeedPage.web_conference_link).click()
    page.get_by_role("link", name="Web conferences").click()
    page.wait_for_load_state("domcontentloaded")
    #page.locator(ConferencePage.cross_on_conference_help_popup).click()
    # page.locator(ConferencePage.new_conference_button).click()
    # page.locator(ConferencePage.create_conf_popup_room_selector).click()
    # page.locator(ConferencePage.create_conf_popup_room_selector).select_text("Standard conference room")
    # page.locator(ConferencePage.create_conf_popup_room_selector).press("ArrowDown")
    # page.locator(ConferencePage.create_conf_popup_room_selector).press("Enter")
    page.locator(ConferencePage.conference_rooms_tab).click()
    page.wait_for_load_state("domcontentloaded")
    page.locator("[data-test-id=\"EntityItem\"]").get_by_text("Standard conference room").click()
    page.wait_for_load_state("domcontentloaded")
    page.locator(ConferencePage.standard_conf_room_new_conf_button).click()
    page.locator(ConferencePage.conference_name).fill(data_gen.name())
    page.locator(ConferencePage.date).fill(data_gen.first_of_next_month())
    page.locator(ConferencePage.hh).fill("2")
    page.locator(ConferencePage.next_button).click()
    page.locator(ConferencePage.next_button).click()
    page.locator(ConferencePage.create_button).click()
    page.wait_for_selector(ConferencePage.conference_creation_success_message)
    assert page.locator(ConferencePage.conference_creation_success_message).is_visible()


def test_private_webconference_creation(login_company):  # Create a Closed Webconference
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    page.get_by_role("link", name="Web conferences").click()
    page.wait_for_load_state("domcontentloaded")
#    page.locator(ConferencePage.cross_on_conference_help_popup).click()
    # page.locator(ConferencePage.new_conference_button).click()
    # page.locator(ConferencePage.create_conf_popup_room_selector).click()
    # page.locator(ConferencePage.create_conf_popup_room_selector).select_text("Standard conference room")
    # page.locator(ConferencePage.create_conf_popup_room_selector).press("ArrowDown")
    # page.locator(ConferencePage.create_conf_popup_room_selector).press("Enter")
    page.locator(ConferencePage.conference_rooms_tab).click()
    page.wait_for_load_state("domcontentloaded")
    page.locator("[data-test-id=\"EntityItem\"]").get_by_text("Standard conference room").click()
    page.wait_for_load_state("domcontentloaded")
    page.locator(ConferencePage.standard_conf_room_new_conf_button).click()
    page.locator(ConferencePage.conference_name).fill(data_gen.name())
    page.locator(ConferencePage.date).fill(data_gen.first_of_next_month())
    page.locator(ConferencePage.hh).fill("2")
    page.locator(ConferencePage.next_button).click()
    page.locator(ConferencePage.closed_conference_radio_button).click()
    page.locator(ConferencePage.next_button).click()
    page.locator(ConferencePage.create_button).click()
    page.wait_for_selector(ConferencePage.conference_creation_success_message)
    assert page.locator(ConferencePage.conference_creation_success_message).is_visible()
