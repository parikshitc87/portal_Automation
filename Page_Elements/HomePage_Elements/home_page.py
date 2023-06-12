class HomePage:
    own_profile_top_left = ''
    profile_icon_top_right = "text = profile >> nth =5"
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


    def open_top_profile_tray(page):
        page.get_by_role("button", name="Profile").click()


    def logout(page):
        page.get_by_role("button", name="Profile").click()
        page.get_by_role("button", name="Log out").click()


    class InterestsBlock:
        section_title = 'text = Hits by interests'
        default_text_title = 'text = Define your interests!'
        default_text_paragraph = 'text = Configure your interests to enable the portal to provide you with suitable matches.'
        red_hint_arrow = '#hint svg'

        def interests_tooltip_button(page):
            return page.get_by_role("heading", name="Hits by interests").locator("[data-test-id=\"Btn\"]")

        def interests_settings_gear_button(page):
            return page.get_by_role("link", name="Interests Settings")


