from playwright.sync_api import expect

from Helper_Modules.Common_Functions.portal import login_with
from Helper_Modules.Test_Data import data_gen
from Page_Elements.login_page_elements import LoginPage


# @pytest.mark.regression
def test_event_form_validations_1(set_up):  # Registers a person account
	page = set_up