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
           and page.locator(HomePage.InterestsBlock.red_hint_arrow).is_visible()
def
