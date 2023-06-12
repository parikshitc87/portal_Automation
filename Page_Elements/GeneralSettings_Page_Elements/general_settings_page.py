class GeneralSettingsPage:

	def are_elements_present(page):
		return page.get_by_role("link", name="General Settings for e-mail, password, language and account").is_visible() \
		and page.get_by_role("link", name="Interests Manage the display of interests results").is_visible() \
		and page.get_by_role("link", name="Ad-hoc offers Manage the display of ad-hoc offers").is_visible() \
		and page.get_by_role("link", name="Visibility of your profile How can one find your profile?").is_visible() \
		and page.get_by_role("link", name="Notifications How do you want to be notified?").is_visible() \
		and page.get_by_text("Select Language").is_visible()




