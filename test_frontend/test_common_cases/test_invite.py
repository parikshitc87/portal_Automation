from playwright.sync_api import expect

from Helper_Modules.Test_Data import data_gen
from Page_Elements.HomePage_Elements import home_page
from test_frontend.test_homePage import test_homepage


def test_invite_new_user(login_private_person):  #
    page = login_private_person
    page.get_by_role("button", name="Profile").click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state("networkidle")
    page.get_by_role("link", name="Invite contacts").click()
    page.locator("#email input[type=\"text\"]").fill(data_gen.email())
    page.get_by_role("button", name="Send & Invite").click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state("networkidle")
    expect(page.get_by_text("Invitation sent successfully").first).to_be_visible()

