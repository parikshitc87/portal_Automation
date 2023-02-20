import time


def yopmail_inbox_click_register_link(page, emailno):
    time.sleep(2)
    page.goto("https://yopmail.com/en/")
    page.get_by_role("button", name="Allow Necessary Cookies & Continue").click()
    page.get_by_placeholder("Enter your inbox here").fill(emailno)
    page.keyboard.press("Enter")
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state("networkidle")
    activation_link = page.frame_locator("iframe[name=\"ifmail\"]").get_by_role("link",
                                                                                name="Confirm registration now").get_attribute(
        'href')
    page.goto(activation_link)
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state("networkidle")







