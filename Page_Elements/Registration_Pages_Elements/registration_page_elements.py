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
	page_elements = [
		form_heading, create_button, first_name_label,
		first_name_input_field, last_name_label, last_name_input_field, email_label, email_input_field,
		password_label, password_input_field, confirm_password_label, confirm_password_input_field,
		terms_of_use_checkbox, already_have_an_account_login
	]
