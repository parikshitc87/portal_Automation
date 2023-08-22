from Page_Elements.HomePage_Elements.home_page import HomePage


def test_interests_blank_panel(login_business_person):
    page = login_business_person
    page.locator(HomePage.InterestsBlock.red_hint_arrow).click()
    assert HomePage.InterestsBlock.interests_settings_gear_button(page).is_visible() \
           and HomePage.InterestsBlock.interests_tooltip_button(page).is_visible() \
           and page.locator(HomePage.InterestsBlock.red_hint_arrow).is_visible() \
           and page.locator(HomePage.InterestsBlock.section_title).is_visible() \
           and page.locator(HomePage.InterestsBlock.default_text_title).is_visible() \
           and page.locator(HomePage.InterestsBlock.default_text_paragraph).is_visible() \




def test_interests_block_tooltip(login_business_person):
    page = login_business_person
    HomePage.InterestsBlock.interests_tooltip_button(page).click()
    assert    page.get_by_role("heading", name="What are interests?").is_visible() \
    and page.get_by_text("As is so often the case, the principle here is: just try it out!").is_visible()



def test_interests_settings_navigation(login_business_person):
    page = login_business_person
    HomePage.InterestsBlock.interests_settings_gear_button(page).click()
    page.wait_for_load_state('domcontentloaded')
    page.wait_for_load_state('networkidle')
    page.locator("[data-test-id=\"FormCheckboxButton\"]").get_by_role("button").click()
    assert page.get_by_text("Interests settings").is_visible() \
           and page.locator("[data-test-id=\"FormCheckboxButton\"]").get_by_role("button").is_visible()