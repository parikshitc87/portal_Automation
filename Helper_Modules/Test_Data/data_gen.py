import random
from datetime import datetime
from unique_names_generator import get_random_name

basic_string_array = ['testing', 'Lorem', 'Ipsum', 'Automation']
password = 'Avaco000'

private_person_email = 'pvtperosn1@pk.avaco.io'
business_person_email = ''
company_account_email = 'automatedcomp2@pk.avaco.io'
contact_account_email = ''
follower_account_email = ''
employee_account_email = ''
search_string_contact1 = "contact1"
search_string_private_person = "private1"
search_string_business_person = "business123"
search_string_company = "automated comp1"
groupcreator = "groupcreator@pk.avaco.io"
contact_messenger_emails = {
	"sender": "compavaco1@mail7.io",
	"receiver": "personavaco1@mail7.io"
}


def name():
	random.shuffle(basic_string_array)
	return basic_string_array[0]


def last_name():  # hhmmss
	return ddmmyyhhmmss().split()[1].replace(':', '')


def unique_string():
	return time_stamp_formatted()


def hh_mm_ss():
	return last_name()


def ddmmyyhhmmss():
	now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
	return str(now)


def time_stamp():  # dd/mm/yyyy hh:mm:ss:cs (centiseconds)
	now = datetime.now().strftime("%d/%m/%Y %H:%M:%S:%f")[:-4]
	print(get_random_name())
	return str(now)


def time_stamp_formatted():
	return time_stamp().replace("/", "").replace(":", "").replace(" ", "")


time_stamp_formatted()


def email():
	return time_stamp_formatted() + '@pk.avaco.io'


def yopmail_email():
	return time_stamp_formatted() + '@yopmail.com'


def post_text():
	random.shuffle(basic_string_array)
	return basic_string_array[0] + ' ' + basic_string_array[1] + ' ' + basic_string_array[
		2] + ' ' + time_stamp_formatted()


def first_of_next_month():
	temp_ddmmyyhhmmss = ddmmyyhhmmss()
	month = temp_ddmmyyhhmmss.split(' ')[0].split('/')[1]  # mm from [dd][mm][yy]
	day = '1'
	year = temp_ddmmyyhhmmss.split(' ')[0].split('/')[2]  # yy from [dd][mm][yy]

	if month == 12:
		month = '1'
		year = str(int(year) + 1)

	else:
		month = str(int(month) + 1)

	return month + '/' + day + '/' + year
