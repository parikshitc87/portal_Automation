import time

from Helper_Modules.Common_Functions.portal import login_with
from Helper_Modules.Test_Data.data_gen import contact_messenger_emails, unique_string
from Page_Elements.Messenger_Elements.message_box import send_message_to_contact, checked_if_message_received


def test_chat_message_delivered_successfully(pre_test_setup):
	page1, page2 = pre_test_setup
	login_with(page1, contact_messenger_emails["sender"])
	#login_with(page2, contact_messenger_emails["receiver"])
	page1.wait_for_load_state("domcontentloaded")
	page1.set_default_timeout(5000)
	page1.wait_for_load_state('networkidle')
	message_text = unique_string()
	send_message_to_contact(page1, message_text)
	checked_if_message_received(page2, message_text) #, contact_messenger_emails["sender"].split('@')[0])

