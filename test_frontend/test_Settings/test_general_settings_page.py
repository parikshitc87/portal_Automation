import string

from playwright.sync_api import expect

from Page_Elements.GeneralSettings_Page_Elements.general_settings_page import GeneralSettingsPage
from Page_Elements.HomePage_Elements.home_page import HomePage


def test_settings_page_elements(login_private_person):
	page = login_private_person
	HomePage.go_to_settings(page)
	page.wait_for_load_state('domcontentloaded')
	page.wait_for_load_state('networkidle')
	#page.wait_for_selector(page.get_by_text("Select Language"), timeout=2000, state='visible')
	page.wait_for_timeout(100)
	assert GeneralSettingsPage.are_elements_present(page)


def test_notification_setting_change_operational_notification_sanity(login_business_person):
	page = login_business_person
	#homepage_link = page.url()
	#settings_link = homepage_link.replace('home', 'settings') + '/'
	#notification_settings_link = homepage_link.replace("home", "settings/notifications")
	HomePage.go_to_settings(page)
	page.wait_for_load_state("networkidle")
	page.wait_for_load_state("domcontentloaded")
	page.get_by_role("link", name="Notifications How do you want to be notified?").click()
	page.wait_for_load_state("networkidle")
	page.wait_for_load_state("domcontentloaded")
	flag1 = page.locator("input[name=\"general-posts-portal\"]").is_checked() \
			and page.locator("input[name=\"general-posts-email\"]").is_checked()
	page.reload()
	page.wait_for_load_state("networkidle")
	page.wait_for_load_state("domcontentloaded")
	page.locator("input[name=\"general-posts-portal\"]").click()
	page.locator("input[name=\"general-posts-email\"]").click()
	flag2 = page.locator("input[name=\"general-posts-portal\"]").is_checked() is False \
	        and page.locator("input[name=\"general-posts-email\"]").is_checked() is False
	assert flag1 is True and flag2 is True
