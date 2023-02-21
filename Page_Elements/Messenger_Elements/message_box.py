class Messages:
	text_box = ""
	send_button = ""
	image_attachment_button = ""
	file_attachment_button = ""
	message_burger_menu = ""
	contact_message_close_button = ""
	contact_window_minimize_element = ""
	message_center_top = ""


def send_message_to_contact(page, message_text): #, receiver_contact="No", file="No", image="No"):
	page.locator("data-test-id=MenuCaption >> text = contacts").click()
	page.wait_for_selector(".simplebar-content > .pt-1", timeout=2000).click()
	page.wait_for_selector("[placeholder = \"Enter message...\"]", timeout=2000).fill(message_text)
	page.keyboard.press('Enter')
	page.wait_for_timeout(5000)


def checked_if_message_received(page, message_text, file="No"): #sender_contact,
	# clicking on contacts chat popup window
	page.locator("data-test-id=MenuCaption >> text = contacts").click()
	# clicking on contact to open chat window to see received message
	page.wait_for_selector(f"data-test-id=Entity >> text = {message_text}", timeout=2000).click()

