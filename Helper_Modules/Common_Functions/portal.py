def logout(page):
    page.get_by_role("button", name="Profile").click()
    page.get_by_role("button", name="Log out").click()


def login_with(page, email):
    with page.expect_popup() as popup_info:
        page.click(":nth-match(:text('Log in'), 2)")
    popup = popup_info.value
    popup.wait_for_load_state("domcontentloaded")
    page.locator("button:has-text(\"Close\")").nth(1).click()
    page.set_default_timeout(20000)
    popup.wait_for_selector('input:below(:text("Email"))', timeout=20000).click()
    popup.wait_for_selector('input:below(:text("Email"))').fill(email)
    popup.keyboard.press("Tab")
    popup.locator("input[name=\"Password\"]").fill("Avaco000")
    popup.wait_for_selector("button").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")


