from playwright.sync_api import expect
from Helper_Modules.Common_Functions import portal
from Helper_Modules.Test_Data import data_gen
from Page_Elements.Groups_Elements.groups_tab_elements import GroupsTab
from Page_Elements.HomePage_Elements.feed_post_elements import FeedPage


def test_public_group_creation(set_up):
    page = set_up
    portal.login_with(page, data_gen.groupcreator)
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
    page.wait_for_load_state("domcontentloaded")
    expect(page.locator(f"h2:has-text('{group_name}')")).to_be_visible()



def test_closed_group_creation(set_up):
    page = set_up
    portal.login_with(page, data_gen.groupcreator)
    page.locator(FeedPage.groups_link).click()
    page.wait_for_load_state("domcontentloaded")
    page.locator(GroupsTab.new_group_button).click()
    page.wait_for_load_state("domcontentloaded")
    page.locator(GroupsTab.group_creation_popup_closed_radio_button).click()
    page.locator(GroupsTab.group_create_popup_next_button).click()
    # page.wait_for_load_state("contentedness")
    page.wait_for_load_state("domcontentloaded")
    group_name = data_gen.name() + data_gen.hh_mm_ss()
    page.locator(GroupsTab.group_name_caption_field).fill(group_name)
    page.locator(GroupsTab.group_create_button).click()
    page.wait_for_load_state("domcontentloaded")
    assert page.locator(f"h2:has-text('{group_name}')").is_visible()



def test_private_group_creation(login_private_person):
    page = login_private_person
    page.locator(FeedPage.groups_link).click()
    page.wait_for_load_state("domcontentloaded")
    page.locator(GroupsTab.new_group_button).click()
    page.wait_for_load_state("domcontentloaded")
    page.locator(GroupsTab.group_creation_popup_private_radio_button).click()
    page.locator(GroupsTab.group_create_popup_next_button).click()
    # page.wait_for_load_state("contentedness")
    page.wait_for_load_state("domcontentloaded")
    group_name = "grp" + data_gen.time_stamp_formatted()
    page.locator(GroupsTab.group_name_caption_field).fill(group_name)
    page.locator(GroupsTab.group_create_button).click()
    page.wait_for_load_state("domcontentloaded")
    expect(page.locator(f"h2:has-text('{group_name}')")).to_be_visible()



def test_group_invitation_search(login_company):
    page = login_company
    group_name = 'PublicGrp'+data_gen.unique_string()
    create_group(page, group_name)
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Open").click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state("networkidle")
    page.wait_for_selector("//input[@placeholder='Invite members']")
    page.locator("//input[@placeholder='Invite members']").fill("vimeo")
    expect(page.locator("//span[@class='line-clamp-1' and text() = 'vimeo']")).to_be_visible()


def test_group_invitation_field_functionality(login_company):
    page = login_company
    group_name = 'PublicGrp' + data_gen.unique_string()
    create_group(page, group_name)
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Open").click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state("networkidle")
    page.wait_for_selector("//input[@placeholder='Invite members']")
    page.locator("//input[@placeholder='Invite members']").fill("vimeo")
    page.locator("//span[@class='line-clamp-1' and text() = 'vimeo']").click()
    expect(page.locator("//span[@class='title-box--title']//child::span[text() = 'vimeo']")).to_be_visible(timeout=500)
    page.locator(".ml-2 > line:nth-child(2)").click()
    expect(page.locator("//span[@class='title-box--title']//child::span[text() = 'vimeo']")).to_be_hidden(timeout=500)



def test_group_invitation_send(login_company):
    page = login_company
    group_name = 'PublicGrp' + data_gen.unique_string()
    create_group(page, group_name)
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Open").click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state("networkidle")
    page.wait_for_selector("//input[@placeholder='Invite members']")
    page.locator("//input[@placeholder='Invite members']").fill("vimeo")
    page.locator("//span[@class='line-clamp-1' and text() = 'vimeo']").click()
    page.get_by_role("button", name="Invite").click()
    expect(page.locator("//p[@class='m-0 font-semibold' and text()='Invite sent']")
           and page.locator("//p[@class='m-0 mt-2' and text()='The invite has been sent.']")).to_be_visible(timeout=2000)




def test_group_invitation_removal(login_company):
     page = login_company
     group_name = 'PublicGrp' + data_gen.unique_string()
     create_group(page, group_name)
     page.wait_for_load_state("domcontentloaded")
     page.wait_for_load_state("networkidle")
     page.get_by_role("button", name="Open").click()
     page.wait_for_load_state("domcontentloaded")
     page.wait_for_load_state("networkidle")
     page.wait_for_selector("//input[@placeholder='Invite members']")
     page.locator("//input[@placeholder='Invite members']").fill("vimeo")
     page.locator("//span[@class='line-clamp-1' and text() = 'vimeo']").click()
     page.get_by_role("button", name="Invite").click()



def create_group(page, group_name, description="", group_type="public"):
    page.get_by_role("link", name="Groups").click()
    page.wait_for_load_state("domcontentloaded")
    page.locator(GroupsTab.new_group_button).click()
    page.wait_for_load_state("domcontentloaded")
    if group_type == "private":
        page.locator(GroupsTab.group_creation_popup_private_radio_button).click()
    elif group_type == "closed":
        page.locator(GroupsTab.group_creation_popup_closed_radio_button).click()
    page.locator(GroupsTab.group_create_popup_next_button).click()
    page.get_by_placeholder("Caption").fill(group_name)
    page.locator(GroupsTab.group_description).fill(description)
    page.wait_for_load_state("domcontentloaded")
    group_name = group_type + data_gen.time_stamp_formatted()
    page.locator(GroupsTab.group_name_caption_field).fill(group_name)
    page.locator(GroupsTab.group_create_button).click()
    page.wait_for_load_state("domcontentloaded")
    page.get_by_role("button", name="Open").click()
    page.wait_for_load_state("domcontentloaded")
    return True
