class GroupPage:
    post_textbox = "[placeholder=\"Share something\"]"
    pinboard_tab = 'text = Pinboard'
    media_tab = 'text = Media >> nth = 0'
    members_tab = 'text = Members >>nth = 0'
    settings_tab = 'text = Settings >> nth = 4'
    invite_members_searchBox = '[placeholder = "Invite members"]'
    invite_button = 'text = Invite >> nth = 4'
    private_icon = "[data-test-id=\"StickyElement\"] line"
    closed_icon = "//*[@title = 'Closed group']"
    interact_with_group_text = 'text = Interact with this group!All members of this group can exchange information here'
    closed_group_default_text = 'text = This is a closed group. In order to see the posts, you need to be member of the'
    private_group_default_text = ''
    owner_view_elements_public = [post_textbox, pinboard_tab, media_tab, members_tab, settings_tab, invite_members_searchBox, invite_button]
    owner_view_elements_closed = [post_textbox, pinboard_tab, media_tab, members_tab, settings_tab, invite_members_searchBox, invite_button, closed_icon]
    owner_view_elements_private = [post_textbox, pinboard_tab, media_tab, members_tab, settings_tab, invite_members_searchBox, invite_button, private_icon]
    visitor_view_elements_public = [pinboard_tab, media_tab, members_tab, interact_with_group_text]
