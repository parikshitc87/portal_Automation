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
	page.locator("data-test-id=MenuCaption >> text = contacts").click()
	page.wait_for_selector(".simplebar-content > .pt-1", timeout=2000).click()
	page.wait_for_selector("[placeholder = \"Enter message...\"]", timeout=2000).fill(text)
	page.keyboard.press('Enter')
	page.wait_for_timeout(5000)


def checked_if_message_received(page, text, file="No"): #sender_contact,
	page.locator("data-test-id=MenuCaption >> text = contacts").click()
	page.wait_for_selector("[class=absolute] >> text = 1 >> nth = 2", timeout=2000).click()

