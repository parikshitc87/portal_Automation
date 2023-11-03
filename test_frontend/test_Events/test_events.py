from playwright.sync_api import expect

from Helper_Modules.Common_Functions.portal import global_search
from Helper_Modules.Test_Data import data_gen
from Page_Elements.Events_Elements.events_elements import CreateEventsPageElements, EventsDetailsPage, \
    InvitePersonsPopup, EventEditPage
from Page_Elements.HomePage_Elements.feed_post_elements import FeedPage


# Create a public event
def test_public_event_creation(login_company):  # Create a Public Event
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    page.locator(FeedPage.events_link).click()
    page.wait_for_load_state("domcontentloaded")
    page.locator(CreateEventsPageElements.new_events_button).click()
    page.wait_for_load_state("domcontentloaded")
    name = data_gen.name() + data_gen.last_name()
    page.locator(CreateEventsPageElements.event_name).fill(name)
    page.locator(CreateEventsPageElements.start_date).fill(data_gen.first_of_next_month())
    page.locator("#time div:has-text(\"HH 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23\") select").select_option("02")
    page.locator(CreateEventsPageElements.end_date).fill(data_gen.first_of_next_month())
    page.locator("#endTime div:has-text(\"HH 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23\") select").select_option("03")
    page.locator(CreateEventsPageElements.next_button).click()
    page.locator(CreateEventsPageElements.create_button).click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_selector(CreateEventsPageElements.event_created_success_message)
    expect(page.locator(CreateEventsPageElements.event_created_success_message)).to_be_visible()


# Create a private event
def test_private_event_creation(login_company):  # Create a Public Event
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    page.locator(FeedPage.events_link).click()
    page.wait_for_load_state("domcontentloaded")
    page.locator(CreateEventsPageElements.new_events_button).click()
    page.wait_for_load_state("domcontentloaded")
    name = data_gen.name() + data_gen.last_name()
    page.locator(CreateEventsPageElements.private_event_radio_button).click()
    page.locator(CreateEventsPageElements.event_name).fill(name)
    page.locator(CreateEventsPageElements.start_date).fill(data_gen.first_of_next_month())
    page.locator("#time div:has-text(\"HH 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23\") select").select_option("02")
    page.locator(CreateEventsPageElements.end_date).fill(data_gen.first_of_next_month())
    page.locator("#endTime div:has-text(\"HH 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23\") select").select_option("03")
    page.locator(CreateEventsPageElements.next_button).click()
    page.locator(CreateEventsPageElements.create_button).click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_selector(CreateEventsPageElements.event_created_success_message)
    expect(page.locator(CreateEventsPageElements.event_created_success_message)).to_be_visible()


def test_create_event_form_validations_tab1(login_company):
    page = login_company
    flag = 0
    page.wait_for_load_state("domcontentloaded")
    page.locator(FeedPage.events_link).click()
    page.wait_for_load_state("domcontentloaded")
    page.locator(CreateEventsPageElements.new_events_button).click()
    page.locator(CreateEventsPageElements.maximum_participants_button).click()
    page.locator(CreateEventsPageElements.maximum_participants_text_field).fill("10000")
    if page.locator("text=Additionaloptional The maximum number of participants of 10000 is already preset").is_visible():
        flag += 1
    page.locator(CreateEventsPageElements.maximum_participants_text_field).fill("10001")
    if page.locator("text=Maximum participant number allowed is 10000").is_visible():
        flag += 1
    page.locator(CreateEventsPageElements.location_button).click()
    page.locator(CreateEventsPageElements.floor_textfield).fill("2")
    if page.get_by_text("Please add a location.").is_visible():
        flag += 1
    assert flag == 3


#Verify the entered description and keyword on Event details page
def test_event_keyword_description(login_company):
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    event_name = "Event"+data_gen.unique_string()
    description = "Description" + data_gen.unique_string()
    keyword = "Keyword" + data_gen.unique_string()
    create_event(page, event_name, description, keyword)
    page.get_by_role("button", name="Open").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    assert page.locator(EventsDetailsPage.description).text_content().strip() == description \
           and page.locator(EventsDetailsPage.keywords).text_content().strip() == keyword


#Verify event invitation sending to a user
def test_event_invite_person_popup_elements(login_company):
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    event_title = "Event"+data_gen.unique_string()
    create_event(page, event_title)
    page.get_by_role("button", name="Open").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_selector(EventsDetailsPage.invite_persons_button, timeout=5000)
    page.locator(EventsDetailsPage.invite_persons_button).click()
    page.wait_for_load_state("domcontentloaded")
    expect(page.locator(InvitePersonsPopup.invite_persons_popup_title).text_content().strip() == "Invite persons" and \
           page.locator(InvitePersonsPopup.cross_button).is_enabled() and \
           page.locator(InvitePersonsPopup.invite_persons_to_this_event_text).text_content().strip() == "Invite persons to this event" and \
           page.locator(InvitePersonsPopup.search_profile_field).is_enabled() and \
           page.locator(InvitePersonsPopup.invite_button).is_enabled() and \
           page.locator(InvitePersonsPopup.invited_persons).text_content().strip() == "Invited persons" and \
           page.locator(InvitePersonsPopup.no_persons_invited_text == "No persons invited"))


def test_event_invitation_search_invite(login_company):
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    event_title = "Event" + data_gen.unique_string()
    create_event(page, event_title)
    page.get_by_role("button", name="Open").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_selector(EventsDetailsPage.invite_persons_button, timeout=5000)
    page.locator(EventsDetailsPage.invite_persons_button).click()
    page.wait_for_load_state("domcontentloaded")
    page.locator(InvitePersonsPopup.search_profile_field).fill("vimeo")
    page.get_by_text("vimeo").click()
    page.get_by_role("button", name="Invite").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_selector("text = Invite sent", timeout=2000)
    expect(page.get_by_role("link", name="vimeo Company") and \
           page.get_by_text("Invite sent") and \
           page.get_by_text("The invite has been sent.") and \
           page.locator("[data-test-id=\"Tag\"]") and \
           page.locator("//span[@class = 'flex-auto block' and text() = 'Invited']")).to_be_visible()



def test_event_remove_invitation(login_company):
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    event_title = "Event" + data_gen.unique_string()
    create_event(page, event_title)
    page.get_by_role("button", name="Open").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_selector(EventsDetailsPage.invite_persons_button, timeout=5000)
    page.locator(EventsDetailsPage.invite_persons_button).click()
    page.wait_for_load_state("domcontentloaded")
    page.locator(InvitePersonsPopup.search_profile_field).fill("vimeo")
    page.get_by_text("vimeo").click()
    page.get_by_role("button", name="Invite").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    page.reload()
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    page.get_by_role("button", name="Invite persons").click()
    delete_invitation_button(page, "vimeo")
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    expect(page.locator("//p[contains(text(),'No persons invited')]")).to_be_visible()


def test_event_edit_title(login_company):
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    event_title = "Event" + data_gen.unique_string()
    create_event(page, event_title)
    page.get_by_role("button", name="Open").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    event_title_new = "Event"+data_gen.unique_string()
    page.locator(EventsDetailsPage.event_edit_button).click()
    page.get_by_placeholder("Caption").fill(event_title_new)
    page.get_by_role("button", name="Save").click()
    #page.wait_for_timeout(2000)
    #assert page.locator(EventsDetailsPage.event_title).text_content(timeout=2000).strip() == event_title_new
    expect(page.locator(EventsDetailsPage.event_title)).to_contain_text(event_title_new, timeout=2500)


def test_edit_event_type_public_to_private(login_company):
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    event_title = "Event" + data_gen.unique_string()
    create_event(page, event_title)
    page.get_by_role("button", name="Open").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    event_title_new = "Event" + data_gen.unique_string()
    page.locator(EventsDetailsPage.event_edit_button).click()
    page.get_by_text("Private event").click()
    page.get_by_role("button", name="Save").click()
    #assert page.locator(EventsDetailsPage.event_type_label).text_content().strip() == "Private event"
    #print("Success")
    expect(page.locator(EventsDetailsPage.event_type_label)).to_contain_text("Private")


def test_edit_event_type_private_to_public(login_company):
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    event_title = "Event" + data_gen.unique_string()
    create_event(page, event_title, is_private=True)
    page.get_by_role("button", name="Open").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    page.locator(EventsDetailsPage.event_edit_button).click()
    page.get_by_text("Public event").click()
    page.get_by_role("button", name="Save").click()
    # assert page.locator(EventsDetailsPage.event_type_label).text_content().strip() == "Private event"
    # print("Success")
    expect(page.locator(EventsDetailsPage.event_type_label)).to_contain_text("Public")


def test_edit_event_keyword_1(login_company):
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    event_title = "Event" + data_gen.unique_string()
    keyword = data_gen.unique_string()
    create_event(page, event_title)
    page.get_by_role("button", name="Open").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    page.locator(EventsDetailsPage.event_edit_button).click()
    page.get_by_placeholder("Add some keywords").fill(keyword)
    page.get_by_placeholder("Add some keywords").press("Tab")
    page.get_by_role("button", name="Save").click()
    expect(page.locator(EventsDetailsPage.keywords)).to_contain_text(keyword)



def test_edit_event_keyword_2(login_company):
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    event_title = "Event" + data_gen.unique_string()
    keyword1 = data_gen.unique_string()
    keyword2 = int(keyword1)
    keyword2 += 1
    keyword2 = str(keyword2)
    create_event(page, event_title=event_title, keyword = keyword1)
    page.get_by_role("button", name="Open").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    page.locator(EventsDetailsPage.event_edit_button).click()
    keyword_cross_button_click(page, keyword1)
    page.locator(EventEditPage.keyword_textfield).fill(keyword2)
    page.get_by_placeholder("Add some keywords").press("Tab")
    page.get_by_role("button", name="Save").click()
    expect(page.locator(EventsDetailsPage.keywords)).to_contain_text(keyword2)


def test_event_edit_start_time(login_company):
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    event_title = "Event" + data_gen.unique_string()
    create_event(page, event_title)
    page.get_by_role("button", name="Open").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    page.locator(EventsDetailsPage.event_edit_button).click()
    page.locator("#time div:has-text(\"HH 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23\") select").select_option("01")
    page.locator("#time div:has-text(\"MM 00 15 30 45\") select").select_option("15")
    page.get_by_placeholder("Add some keywords").press("Tab")
    page.get_by_role("button", name="Save").click()
    page.wait_for_load_state("domcontentloaded")
   # page.wait_for_selector("//h4[contains(text(), '01:15 AM')]", timeout=2000)
    expect(page.locator("//p[contains(text(), '01:15 AM to')]")).to_be_visible()


def test_event_edit_end_time(login_company):
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    event_title = "Event" + data_gen.unique_string()
    create_event(page, event_title)
    page.get_by_role("button", name="Open").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    page.locator(EventsDetailsPage.event_edit_button).click()
    page.locator("#endTime div:has-text(\"HH 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23\") select").select_option("04")
    page.locator("#endTime div:has-text(\"MM 00 15 30 45\") select").select_option("15")
    page.get_by_placeholder("Add some keywords").press("Tab")
    page.get_by_role("button", name="Save").click()
    page.wait_for_load_state("domcontentloaded")
   # page.wait_for_selector("//h4[contains(text(), '01:15 AM')]", timeout=2000)
    expect(page.locator("//p[contains(text(), 'to 04:15 AM')]")).to_be_visible()


def test_event_edit_description_popup_validations(login_company):
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    event_title = "Event" + data_gen.unique_string()
    create_event(page, event_title)
    page.get_by_role("button", name="Open").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    page.locator(EventsDetailsPage.edit_details_button).click()
    expect(page.locator("header:has-text(\"Edit description\")").get_by_role("figure").locator("svg") and
           page.get_by_role("heading", name="Edit description") and
           page.locator("[data-test-id=\"FormLabel\"]").get_by_text("Description") and
           page.get_by_text("optional") and
           page.get_by_placeholder("Write about the event ...") and
           page.get_by_text("Please make some changes.") and
           page.locator("header:has-text(\"Edit description\")").get_by_role("button") and
           page.get_by_role("button", name="Save")
           ).to_be_visible()


def test_edit_event_add_description(login_company):
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    event_title = "Event" + data_gen.unique_string()
    description = "Description" + data_gen.unique_string()
    create_event(page, event_title)
    page.get_by_role("button", name="Open").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    page.locator(EventsDetailsPage.edit_details_button).click()
    page.get_by_placeholder("Write about the event ...").fill(description)
    page.get_by_role("button", name="Save").click()
    expect(page.locator(f"//p[contains(text(),{description})]"))


def test_edit_event_edit_description(login_company):
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    event_title = "Event" + data_gen.unique_string()
    description1 = "Description1" + data_gen.unique_string()
    description2 = "Description2"+data_gen.unique_string()
    create_event(page, event_title, description=description1)
    page.get_by_role("button", name="Open").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    page.locator(EventsDetailsPage.edit_details_button).click()
    page.get_by_placeholder("Write about the event ...").fill(description2)
    page.get_by_role("button", name="Save").click()
    expect(page.locator(f"//p[contains(text(),{description2})]"))


def test_share_popup_validations(login_company):
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    event_title = "Event" + data_gen.unique_string()
    create_event(page, event_title)
    page.get_by_role("button", name="Open").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    page.locator(EventsDetailsPage.share_button).click()
    expect(page.get_by_role("heading", name="Share") and
           page.get_by_text("Share within the portal") and
           page.get_by_placeholder("Write something...") and
           page.locator("//button[@class='button button--small']") and
           page.locator("//span[contains(text(),'Share') and @class='flex-auto block']")
           ).to_be_visible()


def test_event_share_without_text(login_company):
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    event_title = "Event" + data_gen.unique_string()
    create_event(page, event_title)
    page.get_by_role("button", name="Open").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    page.locator(EventsDetailsPage.share_button).click()
    page.get_by_role("button", name="Share").click()
    assert page.locator("//p[@class='m-0 font-semibold']").text_content().strip() == "Event shared" and \
           page.locator("//p[@class='m-0 mt-2']").text_content().strip() == "The event has been shared."


def test_event_share_with_text(login_company):
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    event_title = "Event" + data_gen.unique_string()
    create_event(page, event_title)
    page.get_by_role("button", name="Open").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    page.locator(EventsDetailsPage.share_button).click()
    page.get_by_placeholder("Write something...").fill('temp')
    page.get_by_role("button", name="Share").click()
    #expect(page.get_by_text("Event shared") and
     #      page.get_by_text("The event has been shared.")).to_be_visible()
    assert page.locator("//p[@class='m-0 font-semibold']").text_content().strip() == "Event shared" and \
        page.locator("//p[@class='m-0 mt-2']").text_content().strip() == "The event has been shared."


def test_event_search_with_keyword(login_company):
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    event_title = "Event" + data_gen.unique_string()
    keyword = "Keyword" + data_gen.unique_string()
    create_event(page, event_title, keyword=keyword)
    #page.locator("//div[@class='py-4 overflow-hidden px-box']/child::div//child::h1", timeout=4000).click(2)
    page.get_by_role("button", name="Open").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    global_search(page, keyword)
    expect(page.locator("//div[@class='flex flex-wrap flew-row']/child::div[1]/child::a")).to_contain_text(event_title)
    # //div[@class='flex flex-wrap flew-row']/child::div[1]/child::a
    #talk to Rajveer


def test_event_self_rsvp_going(login_company):
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    event_title = "Event" + data_gen.unique_string()
    create_event(page, event_title)
    # page.locator("//div[@class='py-4 overflow-hidden px-box']/child::div//child::h1", timeout=4000).click(2)
    page.get_by_role("button", name="Open").click()
    page.wait_for_load_state("networkidle", timeout=2000)
    page.wait_for_load_state("domcontentloaded")
    page.locator(EventsDetailsPage.rsvp_dropdown).click()
    page.locator(EventsDetailsPage.rsvp_dropdown_option_going).click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state("networkidle", timeout=2000)
    expect(page.locator(EventsDetailsPage.rsvp_dropdown_current_state_going) and
           page.locator(EventsDetailsPage.rsvp_op_notification_text_title_going) and
           page.locator(EventsDetailsPage.rsvp_op_notification_text_subtitle_going)).to_be_visible()


def test_event_self_rsvp_interested(login_company):
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    event_title = "Event" + data_gen.unique_string()
    create_event(page, event_title)
    # page.locator("//div[@class='py-4 overflow-hidden px-box']/child::div//child::h1", timeout=4000).click(2)
    page.get_by_role("button", name="Open").click()
    page.wait_for_load_state("networkidle", timeout=2000)
    page.wait_for_load_state("domcontentloaded")
    page.locator(EventsDetailsPage.rsvp_dropdown).click()
    page.locator(EventsDetailsPage.rsvp_dropdown_option_interested).click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state("networkidle", timeout=2000)
    expect(page.locator(EventsDetailsPage.rsvp_dropdown_current_state_interested) and
           page.locator(EventsDetailsPage.rsvp_op_notification_text_title_interested) and
           page.locator(EventsDetailsPage.rsvp_op_notification_text_subtitle_interested)).to_be_visible()


def test_event_self_rsvp_not_interested(login_company):
    page = login_company
    page.wait_for_load_state("domcontentloaded")
    event_title = "Event" + data_gen.unique_string()
    create_event(page, event_title)
    # page.locator("//div[@class='py-4 overflow-hidden px-box']/child::div//child::h1", timeout=4000).click(2)
    page.get_by_role("button", name="Open").click()
    page.wait_for_load_state("networkidle", timeout=2000)
    page.wait_for_load_state("domcontentloaded")
    page.locator(EventsDetailsPage.rsvp_dropdown).click()
    page.locator(EventsDetailsPage.rsvp_dropdown_option_not_interested).click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state("networkidle", timeout=2000)
    expect(page.locator(EventsDetailsPage.rsvp_dropdown_current_state_not_interested) and
           page.locator(EventsDetailsPage.rsvp_op_notification_text_title_not_interested) and
           page.locator(EventsDetailsPage.rsvp_op_notification_text_subtitle_not_interested)).to_be_visible()

def create_event(page, event_title, description = None, keyword = None, is_private = False):
    page.wait_for_load_state("domcontentloaded")
    page.locator(FeedPage.events_link).click()
    page.wait_for_load_state("domcontentloaded")
    page.locator(CreateEventsPageElements.new_events_button).click()
    page.wait_for_load_state("domcontentloaded")
    page.locator(CreateEventsPageElements.event_name).fill(event_title)
    page.locator(CreateEventsPageElements.start_date).fill(data_gen.first_of_next_month())
    page.locator(CreateEventsPageElements.start_time_hh).select_option("02")
    page.locator(CreateEventsPageElements.end_date).fill(data_gen.first_of_next_month())
    page.locator(CreateEventsPageElements.end_time_hh).select_option("03")
    if is_private is True:
        page.locator("//strong[@class='block font-semibold' and contains(text(), 'Private')]").click()
    page.locator(CreateEventsPageElements.next_button).click()
    if description is not None:
        page.locator(CreateEventsPageElements.description_textbox).fill(description)
    if keyword is not None:
        page.locator(CreateEventsPageElements.keyword_textbox).fill(keyword)
    page.locator(CreateEventsPageElements.create_button).click()
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
    return True


def delete_invitation_button(page, user_name):
    page.locator(f"//span[contains(text(),{user_name})]//ancestor::article//child::div[@class='hidden ml-2 md:block']").click()
    return True


def keyword_cross_button_click(page, keyword):
    page.locator(f"//span[text() = {keyword}]//following-sibling::span").click()
    page.wait_for_load_state("domcontentloaded")
    return True