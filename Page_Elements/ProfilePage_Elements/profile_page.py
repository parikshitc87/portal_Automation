class ProfilePage:
    # edit_profile_button = "//*[@id=\"app\"]/div[1]/div[1]/section/div[2]/div/section/div[1]/div/aside/div/div/div[1]/div/section[1]/div[3]"
    edit_profile_button = 'button:near(.relative.py-2 .flex.justify-center)'
    profile_name = ""
    company_type = ""
    profile_short_info = ""
    post_textbox = '[placeholder=\"Share something\"]'
    add_contact_button = "button:has-text(\"Add contact\")"
    contact_sent_request_button = "button:has-text(\"Contact request sent\")"
    contact_cancel_request_confirmation = "text = cancel request"
    profile_feedTab = "[data-test-id=\"PageMenu\"] >> text=NewsFeed"
    profile_contactsTab = "[data-test-id=\"PageMenu\"] >> text=Contacts"

    ownProfile_contactsTab_invitationsReceivedSubTab = "text=\"Invitations received\""
    profile_contactsTab_contactsSubTab = "text=\"Contacts\" >> nth = 6"
    contactTab_searchBtn = "button.p-2.mx-1.button"
