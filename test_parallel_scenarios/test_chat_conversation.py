import time

from playwright.sync_api import expect

from Helper_Modules.Common_Functions.file_handler import copy_file, delete_file
from Helper_Modules.Common_Functions.portal import login_with
from Helper_Modules.Test_Data.data_gen import contact_messenger_emails, unique_string
from Page_Elements.Messenger_Elements.message_box import send_text_message_to_contact, \
	send_file_message_in_chat, check_text_message_received


# testing delivery of text message
def test_text_message_delivered(pre_test_setup):
	page1, page2 = pre_test_setup
	login_with(page2, contact_messenger_emails["receiver"])
	login_with(page1, contact_messenger_emails["sender"])
	page1.wait_for_load_state("domcontentloaded")
	#page1.set_default_timeout(5000)
	page1.wait_for_load_state('networkidle')
	message_text = unique_string()
	send_text_message_to_contact(page1, message_text)
	check_text_message_received(page2, message_text)  # , contact_messenger_emails["sender"].split('@')[0])
	expect(page2.locator(f"data-test-id=LinkRenderer >> text = {message_text}")).to_be_visible()


# testing delivery of file message
def test_file_message_delivered(pre_test_setup):
	page1, page2 = pre_test_setup
	login_with(page1, contact_messenger_emails["sender"])
	login_with(page2, contact_messenger_emails["receiver"])
	page1.wait_for_load_state("domcontentloaded")
	#page1.set_default_timeout(5000)
	page1.wait_for_load_state('networkidle')
	unique_file_name = unique_string()[::-1][:6] + ".pdf"
	unique_file_name_location = "Helper_Modules/Test_Files/"+unique_file_name
	copy_file("Helper_Modules/Test_Files/sample_pdf.pdf", unique_file_name_location)
	send_file_message_in_chat(page2, unique_file_name_location, unique_file_name)
	page2.wait_for_load_state("domcontentloaded")
	page2.wait_for_load_state("networkidle")
	delete_file(unique_file_name_location)
	page2.close()
	expect(page1.locator(f"text = {unique_file_name}")).to_be_visible()

