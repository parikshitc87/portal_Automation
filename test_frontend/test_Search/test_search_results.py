from playwright.sync_api import expect

from Helper_Modules.Test_Data import data_gen
from Page_Elements.HomePage_Elements.home_page import HomePage
from test_frontend.test_FeedPost.test_feed_post import create_post
from test_frontend.test_Groups.test_groups_creation import create_group


# def random_context():
#     context = [login_private_person, login_company]
#     return context[0]


# Search  a private person
def test_private_person_search(login_private_person):
    page = login_private_person
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state("networkidle")
    assert_results(page, data_gen.search_string_private_person)


# Search a private person with search filter
def test_filtered_private_person_search(login_private_person):
    page = login_private_person
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state("networkidle")
    search_results_filter(page, "Private Persons", data_gen.search_string_private_person)


# Search a business user
def test_business_person_search(login_private_person):
    page = login_private_person
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state("networkidle")
    assert_results(page, data_gen.search_string_business_person)


# Search a business user using search filter
def test_filtered_business_person_search(login_company):
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state("networkidle")
    search_results_filter(page, "Business Persons", data_gen.search_string_business_person)


#Search a company account
def test_company_search(login_private_person):
    page = login_private_person
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state("networkidle")
    assert_results(page, data_gen.search_string_company)


#Search company with search filter
def test_filtered_company_search(login_private_person):
    page = login_private_person
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state("networkidle")
    search_results_filter(page, "Companies", data_gen.search_string_company)


#Search a group
def test_groups_search(login_private_person):
    page = login_private_person
    search_string = create_group(page, "public")
    assert_results(page, search_string)


#Search groups with group filter
def test_filtered_groups_search(login_private_person):
    page = login_private_person
    search_string = "00001000020000aqz"
    search_results_filter(page, "Groups", search_string)


#Search including location search
def test_search_incl_location(login_private_person):
    page = login_private_person
    page.get_by_role("textbox", name="Search Portal").fill("nike6")
    page.get_by_role("textbox", name="Search Portal").press("Tab")
    page.get_by_role("textbox", name="Place").fill("koln")
    page.get_by_role("textbox", name="Place").press("Enter")
    expect(page.get_by_role("link", name="nike6")).to_be_visible()


#Test feedpost search results
def test_feedpost_search(login_private_person):
    page = login_private_person
    post_text = data_gen.unique_string()
    create_post(page, post_text)
    page.wait_for_selector(f"text = {post_text}").is_visible()
    page.get_by_role("textbox", name="Search Portal").fill(post_text)
    page.get_by_role("textbox", name="Place").press("Enter")
    expect(page.get_by_role("link", name=post_text)).to_be_visible()



# def test_events_search(login_company):
#
# def test_adhoc_post_search(login_company):
#
# def test_content_search(login_company):

# def test_no_results (login_company)

# def search using psudonym

def assert_results(page, search_string):
    page.locator(HomePage.search_box).fill(search_string)
    page.keyboard.press("Enter")
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(2000)
    # expect(page.locator(Page_Elements.SearchResultsPage_Elements.search_results_page_elements
    #                     .search_results_target(search_term))).to_be_visible()
    expect(page.locator(f"text = {search_string}")).to_be_visible()
    # expect(page.locator(f"text = {search_string}")).not_to_be_visible()


def search_results_filter(page, filter_locator, search_string):
    page.locator(HomePage.search_box).fill(search_string)
    page.keyboard.press("Enter")
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(2000)
    if filter_locator == "Companies":
        page.get_by_role("link", name="Companies").nth(1).click()
    elif filter_locator == "Groups":
        page.locator(f"text ={filter_locator} >> nth = 2").click()
    else:
        page.locator(f"text ={filter_locator}").click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state("networkidle")
    # expect(page.locator(Page_Elements.SearchResultsPage_Elements.search_results_page_elements
    #                     .search_results_target(search_term))).to_be_visible()
    expect(page.locator(f"text = {search_string}")).to_be_visible()