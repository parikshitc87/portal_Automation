class SearchPage:
    search_result_test_contact1 = "[data-test-id=\"ClickOutside\"] >> text= automated contact1"
    search_results_filter_private_person = ""


def search_results_target(search_string):
    return f"[data-test-id=\"ClickOutside\"] >> text={search_string}"
