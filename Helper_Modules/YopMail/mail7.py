class Mail7:
	url = "https://www.mail7.io/"
	refresh_button = ""
	def go_to_inbox(page, email_id):
		page.locator(
			"form:has-text(\"@mail7.io Go to inbox or Try our pro plan with private inbox for free Try Pro Fe\") input[name=\"username\"]").fill(email_id.split('@')[0])
		page.locator(
			"form:has-text(\"@mail7.io Go to inbox or Try our pro plan with private inbox for free Try Pro Fe\") input[name=\"username\"]").press(
			"Enter")

#class Inbox:

