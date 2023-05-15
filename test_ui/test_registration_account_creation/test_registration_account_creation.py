from playwright.sync_api import expect

from Helper_Modules.Common_Functions.portal import login_with
from Helper_Modules.Test_Data import data_gen
from Page_Elements.login_page_elements import LoginPage


# @pytest.mark.regression
def test_registration_form_1(set_up):  # Registers a person account
	page = set_up
	register(page, "person")
	expect(page.locator(LoginPage.registration_success_message)).to_be_visible()


def test_register_and_activate(set_up):  # registers Person and confirms registration from email
	page = set_up
	mail7_email = data_gen.time_stamp_formatted() + "@mail7.io"
	account_activation(page, "person", mail7_email)
	expect(page.get_by_role("heading", name="Your account has been activated!")).to_be_visible()


def test_create_business_person_profile_cc(set_up):  # test Business person profile creation
	page = set_up
	mail7_email = data_gen.time_stamp_formatted() + "@mail7.io"
	account_activation(page, "person", mail7_email)
	login_with(page, mail7_email)
	#create_profile_person(page, {"profile_type": "Business", "email": mail7_email})
	#expect(page.get_by_text("HITS BY INTERESTS")).to_be_visible()


def test_create_private_person_profile(set_up):  # test Private person profile creation
	page = set_up
	mail7_email = data_gen.time_stamp_formatted() + "@mail7.io"
	create_profile_person(page, {"profile_type": "Private", "email": mail7_email})
	expect(page.get_by_text("HITS BY INTERESTS")).to_be_visible()


def test_create_company_sepa(set_up):
	page = set_up
	mail7_email = data_gen.time_stamp_formatted() + "@mail7.io"
	create_profile_company(page, {"profile_type": "comp_sepa", "email": mail7_email})
	expect(page.get_by_role("heading", name="Your subscription has been activated")).to_be_visible()


def test_create_company_cc(set_up):
	page = set_up
	mail7_email = data_gen.time_stamp_formatted() + "@mail7.io"
	create_profile_company(page, {"profile_type": "comp_credit_card", "email": mail7_email})
	expect(page.get_by_role("heading", name="Your subscription has been activated")).to_be_visible()


def register(page, profile_type, email="any"):
	# if profile_type == "person":
	# 	page.get_by_role("button", name="Person Connect with friends and business partners Free to use").click()
	# else:
	# 	page.get_by_role("button", name="Company Create a page to extend your business 30 days free trial").click()
	# 	page.locator(LoginPage.company_name).fill(data_gen.name())
	page.locator(LoginPage.first_name).fill(data_gen.name())
	page.locator(LoginPage.last_name).fill(data_gen.last_name())
	if email == "any":
		email = data_gen.time_stamp_formatted() + "@mail7.io"
	page.locator(LoginPage.email_id).fill(email)
	# page.locator(LoginPage.repeat_email).fill(email)
	page.locator(LoginPage.password).fill(data_gen.password)
	page.locator(LoginPage.repeat_password).fill(data_gen.password)
	page.locator(LoginPage.terms_and_condition_check_box).click()
	# if profile_type == "company":
	#	page.locator(LoginPage.right_to_register_company_checkbox).click()
	page.get_by_role("button", name="Create account").click()
	page.wait_for_timeout(4000)
	return True


def account_activation(page, profile_type, mail7_email):
	register(page, profile_type, mail7_email)
	page.goto("https://www.mail7.io/")
	page.locator("input[name=\"username\"] >> nth = 0").fill(mail7_email.split("@")[0])
	page.keyboard.press("Enter")
	page.wait_for_url("https://console.mail7.io/admin/inbox/inbox")
	page.wait_for_timeout(2000)
	page.get_by_text("Confirm registration").click()
	page.wait_for_timeout(2000)
	activation_link = page.frame_locator("iframe").get_by_role("link", name="Confirm registration now").get_attribute(
		'href')
	page.goto(activation_link)
	page.wait_for_load_state("domcontentloaded")
	page.wait_for_load_state("networkidle")
	page.wait_for_timeout(2000)
	return True


def create_business_profile(page, profile_info):
	return True


def create_profile_person(page, profile_info):
	login_with(page, profile_info["email"])
	page.wait_for_url("https://portal-dev.dev.otc.workpage.io/setup/person/fill-profile-information")
	if profile_info["profile_type"] == "Private":
		page.locator("text =\"Private person\"").click()
	else:
		page.locator("text =\"Business person\"").click()
	page.locator("form span:has-text(\"Salutation Please select Mr. Ms. Diverse\") select").select_option("Mr")
	page.get_by_placeholder("Academic title").fill("AUTO_BE")
	page.get_by_placeholder("Pseudonym").fill(profile_info["email"].split("@")[0] + "AutoPseudo")
	if profile_info["profile_type"] == "Business":
		page.locator("[placeholder=\"VAT ID\"]").fill("AutoVAT")
	page.locator("button:has-text(\"Next\")").click()
	page.locator("button:has-text(\"Next\")").click()
	return True


def create_profile_company(page, profile_info):
	account_activation(page, "company", profile_info["email"])
	login_with(page, profile_info["email"])
	# page.wait_for_url("https://portal-dev.dev.otc.workpage.io/setup/company/create_profile")
	page.locator("fieldset:has-text(\"Salutation Please select Mr. Ms. Diverse\") select").select_option("Di")
	page.get_by_placeholder("Street").fill(profile_info["email"].split("@")[0])
	page.get_by_placeholder("House no.").fill(profile_info["email"].split("@")[0])
	page.get_by_placeholder("Zip").fill(profile_info["email"].split("@")[0])
	page.get_by_placeholder("City").fill("Berlin")
	page.locator(
		"fieldset:has-text(\"*Country Please select Albania Algeria Andorra Argentina Armenia Australia Austr\") select").select_option(
		"Germany")
	page.get_by_role("button", name="Next").click()
	page.get_by_role("button", name="Next").click()
	# page.wait_for_url("https://portal-dev.dev.otc.workpage.io/home")
	page.wait_for_load_state("domcontentloaded")
	page.wait_for_load_state("networkidle")
	page.get_by_role("button", name="Select package").nth(1).click()
	page.wait_for_load_state("domcontentloaded")
	page.wait_for_load_state("networkidle")
	page.get_by_role("button", name="Next").click()
	page.wait_for_load_state("domcontentloaded")
	page.wait_for_load_state("networkidle")
	page.wait_for_timeout(500)
	page.get_by_role("button", name="Next").click()
	page.wait_for_load_state("domcontentloaded")
	page.wait_for_load_state("networkidle")
	if profile_info["profile_type"] == "comp_credit_card":
		page.locator("strong:has-text(\"Credit card\")").click()
		page.wait_for_load_state("domcontentloaded")
		page.wait_for_load_state("networkidle")
		page.wait_for_timeout(1000)
		page.keyboard.press("Tab")
		page.keyboard.press("Tab")
		page.wait_for_timeout(300)
		page.keyboard.type("42424242424242420131123")
	else:
		page.locator("strong:has-text(\"SEPA direct debit\")").click()
		page.wait_for_load_state("domcontentloaded")
		page.wait_for_load_state("networkidle")
		page.wait_for_timeout(1000)
		# page.locator("iframe >> nth = 1").fill("DE89370400440532013000")
		# page.frame_locator("iframe[name=\"__privateStripeFrame57410\"]").get_by_placeholder(
		#	"DE00 0000 0000 0000 0000 00").fill("DE89370400440532013000")
		page.keyboard.press("Tab")
		page.wait_for_timeout(300)
		page.keyboard.type("DE89370400440532013000")
	page.get_by_role("button", name="Subscribe").click()
	page.wait_for_load_state("domcontentloaded")
	page.wait_for_load_state("networkidle")
	page.wait_for_timeout(1000)


def select_subscription(page):
	return True


def upload_image(page):
	return True


def subscription_pay_cc(page):
	return True


def subscription_pay_sepa(page):
	return True
