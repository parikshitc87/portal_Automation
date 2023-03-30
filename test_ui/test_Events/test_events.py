from playwright.sync_api import expect

from Helper_Modules.Test_Data import data_gen
from Page_Elements.Events_Elements.events_elements import EventsPageElements
from Page_Elements.HomePage_Elements.feed_post_elements import FeedPage


def test_public_event_creation(login_company):  # Create a Public Event
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    page.locator(FeedPage.events_link).click()
    page.wait_for_load_state("domcontentloaded")
    page.locator(EventsPageElements.new_events_button).click()
    page.wait_for_load_state("domcontentloaded")
    name = data_gen.name() + data_gen.last_name()
    page.locator(EventsPageElements.event_name).fill(name)
    page.locator(EventsPageElements.start_date).fill(data_gen.first_of_next_month())
    page.locator(EventsPageElements.start_date_hh).fill("2")
    page.locator(EventsPageElements.end_date).fill(data_gen.first_of_next_month())
    page.locator(EventsPageElements.end_date_hh).fill("3")
    page.locator(EventsPageElements.next_button).click()
    page.locator(EventsPageElements.create_button).click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_selector(EventsPageElements.event_created_success_message)
    expect(page.locator(EventsPageElements.event_created_success_message)).to_be_visible()


def test_private_event_creation(login_company):  # Create a Public Event
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    page.locator(FeedPage.events_link).click()
    page.wait_for_load_state("domcontentloaded")
    page.locator(EventsPageElements.new_events_button).click()
    page.wait_for_load_state("domcontentloaded")
    name = data_gen.name() + data_gen.last_name()
    page.locator(EventsPageElements.private_event_radio_button).click()
    page.locator(EventsPageElements.event_name).fill(name)
    page.locator(EventsPageElements.start_date).fill(data_gen.first_of_next_month())
    page.locator(EventsPageElements.start_date_hh).fill("2")
    page.locator(EventsPageElements.end_date).fill(data_gen.first_of_next_month())
    page.locator(EventsPageElements.end_date_hh).fill("3")
    page.locator(EventsPageElements.next_button).click()
    page.locator(EventsPageElements.create_button).click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_selector(EventsPageElements.event_created_success_message)
    expect(page.locator(EventsPageElements.event_created_success_message)).to_be_visible()