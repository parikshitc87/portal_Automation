import force as force

from Helper_Modules.Test_Data.data_gen import unique_string


class Messages:
	text_box = ""
	send_button = ""
	image_attachment_button = ""
	file_attachment_button = ""
	message_burger_menu = ""
	contact_message_close_button = ""
	contact_window_minimize_element = ""
	message_center_top = ""


def send_message_to_contact(page, text): #, receiver_contact="No", file="No", image="No"):
	#page.get_by_role("heading", name="Contacts").get_by_text("Contacts").click()

	page.locator("data-test-id=MenuCaption >> text = contacts").click()
	#"data-test-id=MenuCaption >> text = contacts"
	#page.wait_for_selector(f"text = {receiver_contact} >> nth = 0")
	#page.locator(f"text = {receiver_contact} >> nth = 0").click(click_count=3)#messenger contact2
	page.wait_for_selector(".simplebar-content > .pt-1", timeout=2000).click()
	page.wait_for_selector("[placeholder = \"Enter message...\"]", timeout=2000).fill(text)
	page.keyboard.press('Enter')
	page.wait_for_timeout(5000)


def receive_message(page, text, sender_contact, file="No", image="No"):
	#page.locator(sender_contact).click()
	page.locator("data-test-id=MenuCaption >> text = contacts").click()
	#"[class=absolute] >> text = 1 >> nth = 2" for number on badge
	#check if the message appeared in the contact window
	page.wait_for_selector("[class=absolute] >> text = 1 >> nth = 2", timeout=2000).click()
	#assert in test method if message appeared in chat window
	return page.locator("").is_visible()

