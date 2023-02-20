class FeedPage:
    post_textbox = "[placeholder=\"Share something\"]"
    post_button_person_profile = 'button >> text = Post >> nth = 0'  # for person profile login
    post_button_company_profile = 'button >> text = Post >> nth = 1'  # for company profile login
    top_post_kebab_menu_button = "text = Like Comment Share >> button >> nth=3"
    top_post_share_button = "text = Share"
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
    attach_files = '#docControl button:has-text("File")'
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
