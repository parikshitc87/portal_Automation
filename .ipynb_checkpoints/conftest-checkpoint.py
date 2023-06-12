import pytest

from Helper_Modules.Test_Data import data_gen


@pytest.fixture
def set_up(page):
	# root = tkinter.Tk()
	# root_ndim_x = root.winfo_screenwidth()
	# root_ndim_y = root.winfo_screenheight()
	page.goto('https://portal-dev.dev.otc.workpage.io')
	# page.set_viewport_size({"width": 1280, "height": 720})
	# page.goto('')
	# page.set_viewport_size({'width': root_ndim_x / 1, 'height': root_ndim_y / 1})
	page.locator('text = User').fill("demo")
	page.locator('text = Password').press("Tab")
	page.locator('text = Password').fill("portal")
	page.locator('text = Password').press("Enter")
	page.wait_for_load_state("domcontentloaded")
	page.set_default_timeout(20000)
	page.wait_for_load_state('networkidle')

	yield page


@pytest.fixture
def login_private_person(set_up):
	page = set_up
	with page.expect_popup() as popup_info:
		page.click(":nth-match(:text('Log in'), 2)")
	popup = popup_info.value
	popup.wait_for_load_state("domcontentloaded")
	page.locator("button:has-text(\"Close\")").nth(1).click()
	page.set_default_timeout(20000)
	popup.wait_for_selector('input:below(:text("Email"))', timeout=20000).click()
	popup.wait_for_selector('input:below(:text("Email"))').fill(data_gen.private_person_email)
	popup.keyboard.press("Tab")
	popup.locator("input[name=\"Password\"]").fill("Avaco000")
	popup.wait_for_selector("button").click()
	page.wait_for_load_state("networkidle")
	page.wait_for_load_state("domcontentloaded")
	yield page


@pytest.fixture
def login_business_person(set_up):
	page = set_up
	with page.expect_popup() as popup_info:
		page.click(":nth-match(:text('Log in'), 2)")
	popup = popup_info.value
	popup.wait_for_load_state("domcontentloaded")
	page.locator("button:has-text(\"Close\")").nth(1).click()
	page.set_default_timeout(20000)
	popup.wait_for_selector('input:below(:text("Email"))', timeout=20000).click()
	popup.wait_for_selector('input:below(:text("Email"))').fill(data_gen.business_person_email)
	popup.keyboard.press("Tab")
	popup.locator("input[name=\"Password\"]").fill("Avaco000")
	popup.wait_for_selector("button").click()
	page.wait_for_load_state("networkidle")
	page.wait_for_load_state("domcontentloaded")
	yield page


@pytest.fixture
def login_company(set_up):
	page = set_up
	with page.expect_popup() as popup_info:
		page.click(":nth-match(:text('Log in'), 2)")
	popup = popup_info.value
	popup.wait_for_load_state("domcontentloaded")
	page.locator("button:has-text(\"Close\")").nth(1).click()
	page.set_default_timeout(20000)
	popup.wait_for_selector('input:below(:text("Email"))', timeout=20000).click()
	popup.wait_for_selector('input:below(:text("Email"))').fill(data_gen.company_account_email)
	popup.keyboard.press("Tab")
	popup.locator("input[name=\"Password\"]").fill("Avaco000")
	popup.wait_for_selector("button").click()
	page.wait_for_load_state("networkidle")
	page.wait_for_load_state("domcontentloaded")

	yield page


@pytest.fixture
def login(set_up, email):
	page = set_up
	with page.expect_popup() as popup_info:
		page.click(":nth-match(:text('Log in'), 2)")
	popup = popup_info.value
	popup.wait_for_load_state("domcontentloaded")
	page.locator("button:has-text(\"Close\")").nth(1).click()
	page.set_default_timeout(10000)
	popup.wait_for_selector('input:below(:text("Email"))', timeout=15000).click()
	popup.wait_for_selector('input:below(:text("Email"))').fill(email)
	popup.keyboard.press("Tab")
	popup.locator("input[name=\"Password\"]").fill("Avaco000")
	popup.wait_for_selector("button").click()
	page.wait_for_load_state("networkidle")
	page.wait_for_load_state("domcontentloaded")

	yield page
