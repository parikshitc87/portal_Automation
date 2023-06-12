from playwright.sync_api import expect

from Helper_Modules.Test_Data import data_gen
from Page_Elements.Groups_Elements.group_page_elements import GroupPage
from Page_Elements.Groups_Elements.groups_tab_elements import GroupsTab
from Page_Elements.HomePage_Elements.feed_post_elements import FeedPage
from Page_Elements.ProfilePage_Elements.profile_page import ProfilePage
from test_frontend.test_Groups.test_groups_creation import create_group


def test_text_post_creation(login_private_person):  # Create a post with post button
	page = login_private_person
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


def test_delete_post(login_private_person):  # delete a post
	page = login_private_person
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
def test_share_post(login_private_person):
	page = login_private_person
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
def test_create_comment(login_private_person):
	page = login_private_person
	# page.locator(FeedPage.cross_on_homepage_video_popup).nth(1).click()
	feed_post_text = data_gen.post_text()
	page.locator(FeedPage.post_textbox).fill(feed_post_text)
	page.keyboard.press('Control+Enter')
	page.wait_for_load_state("networkidle")
	page.wait_for_load_state("domcontentloaded")


# Verify Image post creation
def test_image_post_creation(login_private_person):
	page = login_private_person
	# page.locator(FeedPage.cross_on_homepage_video_popup).nth(1).click()
	post_text = 'Image post' + ' ' + data_gen.unique_string()
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
	expect(page.locator(f"text = {post_text}")).to_be_visible()


# verify File post creation
def test_file_post_creation(login_private_person):
	page = login_private_person
	# page.locator(FeedPage.cross_on_homepage_video_popup).nth(1).click()
	post_text = 'File post' + ' ' + data_gen.unique_string()
	with page.expect_file_chooser() as fc_info:
		page.click(FeedPage.attach_files)
	file_chooser = fc_info.value
	file_chooser.set_files("Helper_Modules/Test_Files/sample_pdf.pdf")  # using a very small  size pdf
	page.locator(FeedPage.post_textbox).fill(post_text)
	page.keyboard.press('Control+Enter')
	page.wait_for_load_state("networkidle")
	page.wait_for_load_state("domcontentloaded")
	assert page.locator(f"text = {post_text}").is_enabled()


# create a post from own profile page
def test_post_creation_from_own_profile(login_private_person):
	page = login_private_person
	page.wait_for_load_state("networkidle")
	page.wait_for_load_state("domcontentloaded")
	# page.locator(HomePage.profile_icon_top_right).click()
	click_own_profile_left_xy(page)
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


def test_post_creation_on_group_wall(login_private_person):  # to be done after changing group test py
	page = login_private_person
	page.wait_for_load_state("networkidle")
	page.wait_for_load_state("domcontentloaded")
	page.locator(FeedPage.groups_link).click()
	page.wait_for_load_state("domcontentloaded")
	page.locator(GroupsTab.new_group_button).click()
	page.wait_for_load_state("domcontentloaded")
	page.locator(GroupsTab.group_create_popup_next_button).click()
	page.wait_for_load_state("domcontentloaded")
	group_name = data_gen.time_stamp_formatted()
	page.locator(GroupsTab.group_name_caption_field).fill(group_name)
	page.locator(GroupsTab.group_create_button).click()
	page.wait_for_load_state("networkidle")
	page.wait_for_load_state("domcontentloaded")
	page.wait_for_selector(GroupsTab.group_created_successfully_popup_open_button, timeout=5000)
	page.locator(GroupsTab.group_created_successfully_popup_open_button).click()
	page.wait_for_load_state("networkidle")
	page.wait_for_load_state("domcontentloaded")
	post_text = data_gen.time_stamp_formatted()
	page.locator(GroupPage.post_textbox).fill(post_text)
	page.keyboard.press('Control+Enter')
	expect(page.locator(f"text = {post_text}")).to_be_enabled()


def test_abusive_post_creation_home_wall(login_private_person):
	page = login_private_person
	create_post(page, "bitch")
	expect(page.locator(
		"span:has-text(\"Post denied The post was denied by the language filter.\") svg").first).to_be_visible()


def test_abusive_post_creation_group_wall(login_private_person):
	page = login_private_person
	create_group(page)
	create_post(page, "bitch")
	expect(page.locator(
		"span:has-text(\"Post denied The post was denied by the language filter.\") svg").first).to_be_visible()


def test_post_large_file_upload_error(login_private_person):
	page = login_private_person
	create_post(page, data_gen.unique_string(), data_gen.heavy_file_location)
	expect(page.locator(FeedPage.post_textbox_file_too_big_error)).to_be_visible()


def test_post_large_image_upload_error(login_private_person):
	page = login_private_person
	create_post(page, data_gen.unique_string(), image_location=data_gen.heavy_image_location)
	expect(page.locator(FeedPage.post_textbox_image_too_big_error)).to_be_visible()


def test_blank_text_post_creation_error(login_private_person):
	page = login_private_person
	page.get_by_role("button", name="Post").click()
	assert page.locator(FeedPage.no_text_entered_error).is_visible()


def test_conference_post_creation(login_business_person):
	page = login_business_person
	feed_post_text = data_gen.unique_string()
	create_post(page, feed_post_text, conference=True)
	expect(page.locator(f"text = {feed_post_text}")).to_be_visible()


def test_emoji_text_post(login_business_person):
	page = login_business_person
	page.locator(FeedPage.feed_post_emoji_button).click()
	page.get_by_text("😄").click()
	feed_post_text = data_gen.unique_string()
	page.locator(FeedPage.post_textbox).click()
	page.keyboard.type(feed_post_text)
	page.get_by_role("button", name="Post").click()
	expect(page.locator(f"text = 😄{feed_post_text}")).to_be_visible()


def test_feed_post_tooltip(login_business_person):
	page = login_business_person
	page.get_by_role("button", name="Create post").locator("[data-test-id=\"Btn\"]").click()
	flag1 = FeedPage.post_settings_tooltip_elements_are_visible(page)
	page.locator("header:has-text(\"Post Settings\")").get_by_role("button").click()
	flag2 = FeedPage.post_settings_tooltip_elements_are_visible(page)
	assert flag1 is True and flag2 is False


def test_conference_post_tooltip(login_business_person):
	page = login_business_person
	page.get_by_role("button", name="Web conference").locator("[data-test-id=\"Btn\"]").click()
	flag1 = FeedPage.conference_post_tooltip_elements_are_visible(page)
	page.locator("header:has-text(\"Web conferences\")").get_by_role("button").click()
	flag2 = FeedPage.conference_post_tooltip_elements_are_visible(page)
	assert flag1 is True and flag2 is False


def create_post(page, feed_post_text, file_location=None, image_location=None, ad_hoc=False, conference=False):
	page.locator(FeedPage.post_textbox).fill(feed_post_text)

	if file_location is not None:
		page.wait_for_selector(FeedPage.attach_files)
		with page.expect_file_chooser() as fc_info:
			page.click(FeedPage.attach_files)
		file_chooser = fc_info.value
		file_chooser.set_files(file_location)

	if image_location is not None:
		page.wait_for_selector(FeedPage.attach_images)
		with page.expect_file_chooser() as fc_info:
			page.click(FeedPage.attach_images)
		file_chooser = fc_info.value
		file_chooser.set_files(image_location)

	if ad_hoc is not False:
		page.wait_for_selector(FeedPage.adhoc_switch).is_checked()

	if conference is not False:
		page.wait_for_selector(FeedPage.conference_post_tab).click()

	# page.wait_for_load_state("networkidle")
	page.get_by_role("button", name="Post").click()
	page.wait_for_load_state("domcontentloaded")
	page.wait_for_load_state('networkidle')


def click_own_profile_left_xy(page):
	page.mouse.click(100, 100, click_count=3, delay=1000)
