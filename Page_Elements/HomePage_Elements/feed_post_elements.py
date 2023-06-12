class FeedPage:
	feed_post_emoji_button = 'text = Emoji'
	post_textbox = "[placeholder=\"Share something\"]"
	post_button_person_profile = 'button >> text = Post >> nth = 0'  # for person profile login
	post_button_company_profile = 'button >> text = Post'  # for company profile login
	top_post_kebab_menu_button = "text = Like Comment Share >> button >> nth=3"
	top_post_share_button = "text = Share >> nth = 0"
	adhoc_switch = "input[type=\"checkbox\"]"
	conference_post_tab = '[data-test-id="PageNavMenuItem"] >> nth = 1'
	top_post_comment_button = "text = Comment"
	top_post_direct_link = ""
	top_post_profile_link = ""
	top_post_delete_option = "text = Delete post"
	top_post_edit_option = ""
	comment_box = ""
	comment_post_button = ""
	comment_text = ""
	comment_delete = ""
	search_box = "[placeholder=\"Search Portal\"] >> nth = 1"
	search_button = ""
	search_location_box = "[placeholder=\"Place\"] >> nth = 1"
	news_feed_link = 'text = Newsfeed Newsfeed'
	contacts_link = 'text = Contacts Contacts'
	groups_link = 'text=Groups >> nth=0'
	employees_link = 'text = Employees Employees'
	events_link = '.site-menu-icon.feather.feather-calendar >> nth=0'
	web_conference_link = 'text=Web conferences Web conferences Web conferences >> svg >> nth=0'
	shop_settings_link = 'Shop Shop'
	purchases_link = 'text = Purchases Purchases Purchases'
	attach_images = 'button:has-text("Image")'
	attach_files = "//*[@id='docControl']"
	interests_settings_cog = 'text =Hits by interests Define your interests! Configure your interests to enable the ' \
	                         '>> a circle'
	interests_help_button = 'text =Hits by interests Define your interests! Configure your interests to enable the >>' \
	                        'button '
	requests = 'button:has-text("Requests") >> nth = 0'
	delete_pop_up_confirmation_yes = "text = Yes"
	pop_up_confirmation_no = 'button:has-text("No") >> nth = 1'
	operational_notification_post_deleted_success = 'text = Post Deleted'
	share_popup_share_button = '.flex.items-center.justify-end.w-full .button-primary >> nth = 0'
	share_success_operational_notification = 'text = Post shared'
	cross_on_homepage_video_popup = "text=Structure of the portal Open in window >> button"

	### ERRORS ###
	post_textbox_file_too_big_error = 'text = The maximum file size for documents is 50,000 kB'
	post_textbox_image_too_big_error = 'text = The maximum file size for images is 10,000 kB'
	no_text_entered_error = "text = Add some text or upload an image to create a wallpost."

	### Tooltips ###

	def post_settings_tooltip_elements_are_visible(page):
		return	page.locator("header:has-text(\"Post Settings\")").get_by_role("figure").locator("svg").is_visible() and \
			page.get_by_role("heading", name="Post Settings").is_visible() and \
			page.get_by_role("heading", name="Who is able to see this post?").is_visible() and \
			page.get_by_role("heading", name="Turn notifications on/off").is_visible() and \
			page.get_by_text("By turning on notifications, the users who follow you will receive a notificatio").is_visible() and \
			page.get_by_role("heading", name="Public").locator("svg").is_visible() and \
			page.get_by_role("heading", name="Public").is_visible() and \
			page.get_by_text("This post is visible to everyone - inside and outside the portal.").is_visible() and \
			page.get_by_role("heading", name="My contacts").locator("svg").is_visible() and \
			page.get_by_role("heading", name="My contacts").is_visible() and \
			page.get_by_text("This post is only visible for connected contacts.").is_visible() and \
			page.get_by_role("heading", name="Only me").locator("svg").is_visible() and \
			page.get_by_role("heading", name="Only me").is_visible() and \
			page.get_by_text("This post is not visible to anyone but yourself.").is_visible()




	def conference_post_tooltip_elements_are_visible(page):
		return page.locator("header:has-text(\"Web conferences\")").get_by_role("figure").locator("svg").is_visible() and \
            page.get_by_role("heading", name="Web conferences").is_visible() and \
            page.locator("header:has-text(\"Web conferences\")").get_by_role("button").is_visible() and \
			page.get_by_role("heading", name="What are web conferences?").is_visible() and \
			page.get_by_text("For companies there is the possibility to create a web conference by mail on the").is_visible() and \
			page.get_by_text("An example of a company: A telecommunications company wants to present new produ").is_visible() and \
			page.get_by_role("heading", name="How do you create a web conference?").is_visible() and \
			page.get_by_text("Web conferences can only be created for companies by clicking a button. The butt").is_visible() and \
			page.get_by_text("Users logged on to the portal can join the conference directly by clicking the “").is_visible() and \
			page.get_by_text("Please note that conferences you have previously created are no longer available").is_visible()






