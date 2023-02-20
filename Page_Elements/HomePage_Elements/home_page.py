class HomePage:
    own_profile_top_left = ''
    profile_icon_top_right = "text = profile >> nth =1"
    # profile_icon_top_right = "button.relative.inline-block.transition-colors.duration-150.ease-in-out.focus:outline-none.helper-hover.hover:no-underline.w-full.h-full.text-gray-900.hover:text-gray-900.dark:text-white"
    profile_drawer_text_you_act_as = "text =You act as  >> nth = 1"
    profile_drawer_own_profile_link = '[data-test-id =\"Entity\"] >> nth = 2'
    company_profile_drawer_own_profile_link = '[data - test - id =\"Entity\"] >> nth = 1'
    logout_button = "button:has-text(\"Log out\") >> nth=2"
    search_box = "[placeholder=\"Search Portal\"] >> nth = 1"
    search_location_box = "[placeholder=\"Place\"] >> nth = 1"


def go_to_settings(page):
    page.get_by_role("button", name="Profile").click()
    page.get_by_role("link", name="Settings").click()


def logout(page):
    page.get_by_role("button", name="Profile").click()
    page.get_by_role("button", name="Log out").click()


def go_to_own_profile(page):
    page.get_by_role().click()
