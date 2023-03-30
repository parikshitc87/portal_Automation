from playwright.sync_api import expect

from Helper_Modules.Test_Data import data_gen
from Page_Elements.Groups_Elements.group_page_elements import GroupPage
from Page_Elements.Groups_Elements.groups_tab_elements import GroupsTab
from Page_Elements.HomePage_Elements.feed_post_elements import FeedPage
from Page_Elements.ProfilePage_Elements.profile_page import ProfilePage


def test_text_post_creation(login_person):  # Create a post with post button
    page = login_person
    feed_post_text = data_gen.post_text()
    page.locator(FeedPage.post_textbox).fill(feed_post_text)
    # page.keyboard.press('Control+Enter')
    page.locator(FeedPage.post_button_person_profile).click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state('networkidle')
    assert page.locator(f"text = {feed_post_text}").is_enabled()


def test_company_text_post_creation(login_company):
    page = login_company
    feed_post_text = data_gen.post_text()
    page.locator(FeedPage.post_textbox).fill(feed_post_text)
    # page.keyboard.press('Control+Enter')
    page.locator(FeedPage.post_button_company_profile).click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state('networkidle')
    assert page.locator(f"text = {feed_post_text}").is_enabled()


def test_delete_post(login_person):  # delete a post
    page = login_person
    # page.locator(FeedPage.cross_on_homepage_video_popup).nth(1).click()
    feed_post_text = data_gen.post_text()
    page.locator(FeedPage.post_textbox).fill(feed_post_text)
    page.keyboard.press('Control+Enter')
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    page.locator(FeedPage.top_post_kebab_menu_button).click()
    page.locator(FeedPage.top_post_delete_option).click()
    page.locator(FeedPage.delete_pop_up_confirmation_yes).click()
    assert page.locator(FeedPage.operational_notification_post_deleted_success).is_enabled()


# Verify post share
def test_share_post(login_person):
    page = login_person
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    feed_post_text = data_gen.post_text()
    page.locator(FeedPage.post_textbox).fill(feed_post_text)
    page.keyboard.press('Control+Enter')
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    page.locator(FeedPage.top_post_share_button).click()
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_selector(FeedPage.share_popup_share_button)
    page.locator(FeedPage.share_popup_share_button).click()
    expect(page.locator(FeedPage.share_success_operational_notification)).to_be_visible()


# Verify comment creation
def test_create_comment(login_person):
    page = login_person
    # page.locator(FeedPage.cross_on_homepage_video_popup).nth(1).click()
    feed_post_text = data_gen.post_text()
    page.locator(FeedPage.post_textbox).fill(feed_post_text)
    page.keyboard.press('Control+Enter')
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")


# Verify Image post creation
def test_image_post_creation(login_person):
    page = login_person
    # page.locator(FeedPage.cross_on_homepage_video_popup).nth(1).click()
    post_text = 'Image post' + ' ' + data_gen.hh_mm_ss()
    # page.set_input_files(FeedPage.attach_images, 'Helper_Modules/Test_Files/test_image.jpeg')
    with page.expect_file_chooser() as fc_info:
        page.click(FeedPage.attach_images)
    file_chooser = fc_info.value
    file_chooser.set_files("Helper_Modules/Test_Files/test_image.jpeg")  # using a very small image
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    page.locator(FeedPage.post_textbox).fill(post_text)
    page.keyboard.press('Control+Enter')
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    #   page.wait_for_load_state("networkidle")
    assert page.locator(f"text = {post_text}").is_enabled()


# verify File post creation
def test_file_post_creation(login_person):
    page = login_person
    # page.locator(FeedPage.cross_on_homepage_video_popup).nth(1).click()
    post_text = 'File post' + ' ' + data_gen.hh_mm_ss()
    with page.expect_file_chooser() as fc_info:
        page.click(FeedPage.attach_files)
    file_chooser = fc_info.value
    file_chooser.set_files("Helper_Modules/Test_Files/sample_pdf.pdf")  # using a very small  size pdf
    page.locator(FeedPage.post_textbox).fill(post_text)
    page.keyboard.press('Control+Enter')
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    assert page.locator(f"text = {post_text}").is_enabled()
    # assert page.locator(f"text = {post_text}").is_disabled()


# create a post from own profile page
def test_post_creation_from_own_profile(login_person):
    page = login_person
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    # page.locator(HomePage.profile_icon_top_right).click()
    page.mouse.click(100, 100, click_count=3, delay=1000)
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(timeout=2000)
    post_text = data_gen.time_stamp_formatted()
    page.locator(ProfilePage.post_textbox).fill(post_text)
    page.keyboard.press('Control+Enter')
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(timeout=2000)
    assert page.locator(f"text = {post_text}").is_visible()


def test_post_creation_on_group_wall(login_person):  # to be done after changing group test py
    page = login_person
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    # page.locator(HomePage.profile_icon_top_right).click()
    page.locator(FeedPage.groups_link).click()
    page.wait_for_load_state("domcontentloaded")
    page.locator(GroupsTab.new_group_button).click()
    page.wait_for_load_state("domcontentloaded")
    page.locator(GroupsTab.group_create_popup_next_button).click()
    # page.wait_for_load_state("contentedness")
    page.wait_for_load_state("domcontentloaded")
    group_name = data_gen.time_stamp_formatted()
    page.locator(GroupsTab.group_name_caption_field).fill(group_name)
    page.locator(GroupsTab.group_create_button).click()
    page.wait_for_timeout(timeout=1500)
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    page.locator(GroupsTab.group_created_successfully_popup_open_button).click()
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    post_text = data_gen.time_stamp_formatted()
    page.locator(GroupPage.post_textbox).fill(post_text)
    page.keyboard.press('Control+Enter')
    # page.wait_for_timeout(timeout=3000) # this was removed when assert was replaced by  expect below
    expect(page.locator(f"text = {post_text}")).to_be_enabled()
