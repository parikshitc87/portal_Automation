import pytest

from Helper_Modules.Common_Functions.portal import login_with
from Helper_Modules.Test_Data import data_gen


@pytest.fixture(scope='session')
def context_1(playwright):
    browser = playwright.chromium.launch(headless=False) #, slow_mo=2000)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://portal-dev.dev.otc.workpage.io')
    page.locator('text = User').fill("demo")
    page.locator('text = Password').press("Tab")
    page.locator('text = Password').fill("portal")
    page.locator('text = Password').press("Enter")
    page.wait_for_load_state("domcontentloaded")
    page.set_default_timeout(10000)
    page.wait_for_load_state('networkidle')

    yield page


@pytest.fixture(scope='session')
def context_2(playwright):
    browser = playwright.chromium.launch(headless=False) #, slow_mo=2000)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://portal-dev.dev.otc.workpage.io')
    page.locator('text = User').fill("demo")
    page.locator('text = Password').press("Tab")
    page.locator('text = Password').fill("portal")
    page.locator('text = Password').press("Enter")
    page.wait_for_load_state("domcontentloaded")
    page.set_default_timeout(10000)
    page.wait_for_load_state('networkidle')

    yield page


@pytest.fixture()
def pre_test_setup(context_1, context_2, browser):
    page1 = context_1
    page2 = context_2
    yield page1, page2




