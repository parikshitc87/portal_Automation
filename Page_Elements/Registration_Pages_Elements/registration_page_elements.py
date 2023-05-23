class RegistrationPage:

	form_heading = 'text = Create account >> nth = 0'
	create_button = 'text = Create account >> nth = 1'
	first_name_label = 'text = First name'
	first_name_input_field = "[placeholder=\"First name\"]"
	last_name_label = 'text = Last name'
	last_name_input_field = "[placeholder=\"Last name\"]"
	email_label = '//span[text() = \"Email\"]'
	email_input_field = "[placeholder = \"Email\"]"
	password_label = "//span[text() = \"Password\"]"
	password_input_field = "[placeholder = \"Password\"]"
	confirm_password_label = 'text = Confirm Password'
	confirm_password_input_field = "[placeholder = \"Repeat password\"]"
	terms_of_use_checkbox = "[data-test-id=\"FormCheckboxButton\"]"
	already_have_an_account_login = "text = Already have an account ?Log in"
	login_button_top = "text = Log in >> nth = 1"
	login_button_below_form = "text = Log in >> nth = 2"
	page_elements = [
		form_heading, create_button, first_name_label,
		first_name_input_field, last_name_label, last_name_input_field, email_label, email_input_field,
		password_label, password_input_field, confirm_password_label, confirm_password_input_field,
		terms_of_use_checkbox, already_have_an_account_login, login_button_top, login_button_below_form
	]
	pass_field_must_have_eight_char_error = "text = The password field must be at least 8 characters"

	def is_tooltip_displayed(page):
		return page.get_by_role("complementary").get_by_text(
			"password: Min. 8 characters Min. one upper and one lower case letter Min. one nu").is_visible()

	def is_password_mismatch_error_displayed(page):
		return page.get_by_text("The inputs do not match.").nth(1).is_visible()

	password_error_no_lowercase_letter = "text = The input does not have a lowercase letter"
	password_error_no_capital_letter = "text = The input does not have a capital letter"
	password_error_no_number = "text = The input does not have a number."


