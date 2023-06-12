from playwright.sync_api import expect

from Helper_Modules.Test_Data import data_gen
from Page_Elements.Groups_Elements import group_page_elements
from Page_Elements.Groups_Elements.group_page_elements import GroupPage
from Page_Elements.HomePage_Elements.feed_post_elements import FeedPage
from Page_Elements.HomePage_Elements.home_page import HomePage
from test_frontend.test_Groups.test_groups_creation import create_group

public_group_link = 'https://portal-dev.dev.otc.workpage.io/group/1005-e1603ba1-618a-42e2-af7c-1bb41a4325b4/overview'
closed_group_link = 'https://portal-dev.dev.otc.workpage.io/group/1005-c31494a5-f46e-481e-ab71-9c937c868425/overview'
private_group_link = 'https://portal-dev.dev.otc.workpage.io/group/1005-c4b3f302-fd02-415a-93d3-a256575c0e3c/overview'


def test_owner_view_public_group(login_business_person):
	page = login_business_person
	page.wait_for_selector(FeedPage.post_textbox, timeout=3000)
	page.goto(public_group_link)
	page.wait_for_load_state("networkidle")
	page.wait_for_load_state("domcontentloaded")
	flag = 0
	for element in GroupPage.owner_view_elements_public:
		page.wait_for_selector(element, timeout=3000)
		if page.locator(element).is_visible(timeout=2000):
			flag += 1
	assert flag is len(GroupPage.owner_view_elements_public)


def test_owner_view_closed_group(login_business_person):
	page = login_business_person
	page.wait_for_selector(FeedPage.post_textbox, timeout=3000)
	page.goto(closed_group_link)
	page.wait_for_load_state("networkidle")
	page.wait_for_load_state("domcontentloaded")
	flag = 0
	for element in GroupPage.owner_view_elements_closed:
		page.wait_for_selector(element, timeout=3000)
		if page.locator(element).is_visible(timeout=2000):
			flag += 1
	assert flag is len(GroupPage.owner_view_elements_closed)


def test_owner_view_private_group(login_business_person):
	page = login_business_person
	page.wait_for_selector(FeedPage.post_textbox, timeout=3000)
	page.goto(private_group_link)
	page.wait_for_load_state("networkidle")
	page.wait_for_load_state("domcontentloaded")
	flag = 0
	for element in GroupPage.owner_view_elements_private:
		page.wait_for_selector(element, timeout=3000)
		if page.locator(element).is_visible(timeout=2000):
			flag += 1
	assert flag is len(GroupPage.owner_view_elements_private)


def test_visitor_view_public_group(login_private_person):
	page = login_private_person
	page.wait_for_selector(FeedPage.post_textbox, timeout=3000)
	page.goto(public_group_link)
	page.wait_for_load_state("networkidle")
	page.wait_for_load_state("domcontentloaded")
	flag = 0
	page.wait_for_selector(GroupPage.interact_with_group_text, timeout=3000)
	for element in GroupPage.owner_view_elements_public:
		if page.locator(element).is_visible(timeout=2000):
			flag += 1
	if page.locator(GroupPage.interact_with_group_text).is_visible():
		flag += 1
	assert flag is 4


def test_visitor_view_closed_group(login_private_person):
	page = login_private_person
	page.wait_for_selector(FeedPage.post_textbox, timeout=3000)
	page.goto(closed_group_link, wait_until="domcontentloaded")
	page.wait_for_load_state("networkidle")
	page.wait_for_load_state("domcontentloaded")
	flag = 0
	page.wait_for_selector(GroupPage.closed_group_default_text, timeout=3000, state='visible')
	for element in GroupPage.owner_view_elements_public:
		if page.locator(element).is_visible(timeout=2000):
			flag += 1
	assert flag is 0 and page.locator(GroupPage.closed_group_default_text).is_enabled()



def test_visitor_view_private_group(login_private_person):
	page = login_private_person
	page.wait_for_selector(FeedPage.post_textbox, timeout=3000)
	page.goto(private_group_link, wait_until="domcontentloaded")
	page.wait_for_load_state("networkidle")
	page.wait_for_load_state("domcontentloaded")
	flag = 0
	page.wait_for_selector(GroupPage.closed_group_default_text, timeout=3000, state='visible')
	for element in GroupPage.owner_view_elements_public:
		if page.locator(element).is_visible(timeout=2000):
			flag += 1
	assert flag is 0 and page.locator(GroupPage.closed_group_default_text).is_enabled()


def test_member_view_public_group(set_up):
	page = set_up


def test_member_view_private_group(set_up):
	page = set_up




