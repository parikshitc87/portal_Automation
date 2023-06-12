from playwright.sync_api import expect

from Helper_Modules.Test_Data import data_gen


def test_purchase_history_filters(login_private_person):
	page = login_private_person
	page.get_by_role("link", name="Purchases").click()
	flag = 0
	for element in ['All', 'New orders', 'In progress', 'Shipped', 'Completed']:
		if page.get_by_role("link", name=element).is_visible() and page.get_by_role("link", name=element).is_enabled():
			flag += 1
	if page.get_by_text("No Orders List Yet").is_visible():
		flag += 1
	assert flag is 6