from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=200)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://portal-master.my-portal.io/
    page.goto("https://portal-master.my-portal.io/")

    # Click text=This is an unpublished version of the portal Please show me that you have the ri >> [placeholder="User"]
    page.locator("text = User").click()
    # Fill text=This is an unpublished version of the portal Please show me that you have the ri >> [placeholder="User"]
    page.locator(
        "text=This is an unpublished version of the portal Please show me that you have the ri >> [placeholder=\"User\"]").fill(
        "demo")

    # Press Tab
    page.locator(
        "text=This is an unpublished version of the portal Please show me that you have the ri >> [placeholder=\"User\"]").press(
        "Tab")

    # Fill text=This is an unpublished version of the portal Please show me that you have the ri >> [placeholder="Password"]
    page.locator(
        "text=This is an unpublished version of the portal Please show me that you have the ri >> [placeholder=\"Password\"]").fill(
        "portal")
    page.locator(
        "text=This is an unpublished version of the portal Please show me that you have the ri >> [placeholder=\"Password\"]").fill(
        "portal")

    # Press Enter
    # with page.expect_navigation(url="https://portal-master.my-portal.io/site/register"):
    with page.expect_navigation():
        page.locator(
            "text=This is an unpublished version of the portal Please show me that you have the ri >> [placeholder=\"Password\"]").press(
            "Enter")
    # expect(page).to_have_url("https://portal-master.my-portal.io/?user=demo&password=portal")

    with page.expect_popup() as popup_info:
        page.click(":nth-match(:text('Log in'), 2)")
    popup = popup_info.value

    popup.wait_for_load_state("domcontentloaded")

    popup.wait_for_selector('input:below(:text("Email"))', timeout=10000).click()

    popup.wait_for_selector('input:below(:text("Email"))').fill("jw@pk.avaco.io")
    popup.keyboard.press("Tab")

    # Fill input[name="Password"]
    popup.locator("input[name=\"Password\"]").fill("Avaco000")

    # Click button:has-text("Log In")
    # with page1.expect_navigation(url="https://portal-master.my-portal.io/site/login-callback/?user=demo&password=portal&code=-BouceGCBKWukMtYUDYDwmSV1gZqktWQkIXfXllM-vQ&scope=openid%20profile%20api1%20AffiliateService%20ProfileService%20IdentityService%20WallPostServiceApi%20DataAggregationServiceApi%20PortalSearchServiceAPI%20PortalLikeServiceAPI%20ProfileNetworkServiceApi%20ChatServiceApi%20commentservice%20GroupServiceApi%20MatchingService%20OrderServiceApi%20CategoryServiceApi%20ShopService%20CartService%20CustomerServiceApi%20MultiShopDataAggregationServiceApi%20ArticleServiceApi%20PrivacyServiceApi%20NotificationServiceApi%20ProxyServiceApi%20PaymentService%20ShippingService%20InvoiceService%20ReportServiceApi%20AddressServiceApi%20EntityListApi%20FollowService%20InvitationServiceApi%20PortalLoggingServiceAPI%20SubscriptionService%20StatisticsServiceApi%20ContentManagementService%20CommunityService%20DonationService%20PortalCalendarService%20TaskService%20WebConferenceService%20EmailTemplateService%20SharingService%20UrlService%20EmploymentAgencyService%20WebsiteMetadataService%20offline_access&state=6bd4c4237c094ddd913f68059efbe3ee&session_state=7-mgSmnWpi-7dLj9PUWNioxdCcTbDvjii8qruLmev3c.JcM-r-7JqTIkfupnn9545g"):
    with popup.expect_navigation():
        popup.wait_for_selector("button").click()
    # expect(page1).to_have_url("https://portal-master.my-portal.io/site/login-callback?code=-BouceGCBKWukMtYUDYDwmSV1gZqktWQkIXfXllM-vQ&scope=openid%20profile%20api1%20AffiliateService%20ProfileService%20IdentityService%20WallPostServiceApi%20DataAggregationServiceApi%20PortalSearchServiceAPI%20PortalLikeServiceAPI%20ProfileNetworkServiceApi%20ChatServiceApi%20commentservice%20GroupServiceApi%20MatchingService%20OrderServiceApi%20CategoryServiceApi%20ShopService%20CartService%20CustomerServiceApi%20MultiShopDataAggregationServiceApi%20ArticleServiceApi%20PrivacyServiceApi%20NotificationServiceApi%20ProxyServiceApi%20PaymentService%20ShippingService%20InvoiceService%20ReportServiceApi%20AddressServiceApi%20EntityListApi%20FollowService%20InvitationServiceApi%20PortalLoggingServiceAPI%20SubscriptionService%20StatisticsServiceApi%20ContentManagementService%20CommunityService%20DonationService%20PortalCalendarService%20TaskService%20WebConferenceService%20EmailTemplateService%20SharingService%20UrlService%20EmploymentAgencyService%20WebsiteMetadataService%20offline_access&state=6bd4c4237c094ddd913f68059efbe3ee&session_state=7-mgSmnWpi-7dLj9PUWNioxdCcTbDvjii8qruLmev3c.JcM-r-7JqTIkfupnn9545g")

    # Close page
    popup.close()

    # Go to https://portal-master.my-portal.io/home?user=demo&password=portal
    page.goto("https://portal-master.my-portal.io/home?user=demo&password=portal")
    page.wait_for_timeout(150000)

    page.wait_for_load_state('networkidle')

    # ---------------------
    context.close()


with sync_playwright() as playwright:
    run(playwright)
