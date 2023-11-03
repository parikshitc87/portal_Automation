class LoginPage:
    login_button = ":nth-match(:text('Log in'), 2)"
    company_user_radio_button = "text = Use of special corporate"
    person_user_radio_button = "text = create a profile for business as well as personal usage"
    first_name = "[placeholder=\"First name\"]"
    last_name = "[placeholder=\"Last name\"]"
    email_id = "[placeholder=\"Email\"]"
    repeat_email = "[placeholder=\"Repeat email\"]"
    submit_button = "text = Submit >> type = button"
    company_name = "[placeholder=\"Company name\"]"
    password = "[placeholder=\"Password\"]"
    repeat_password = "[placeholder=\"Repeat password\"]"
    terms_and_condition_check_box = 'text = I accept'
    right_to_register_company_checkbox = 'text = I have the right to register this company.'
    register_button = 'text = Register'
    register_button_company = "button:has-text(\"Register\")"
    registration_success_message = 'text = Registration succeeded'

