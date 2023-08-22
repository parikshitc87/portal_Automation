import random
from datetime import datetime
from unique_names_generator import get_random_name
from unique_names_generator.data import STAR_WARS, ANIMALS, COLORS

basic_string_array = ['testing', 'Lorem', 'Ipsum', 'Automation']
password = 'Avaco000'

private_person_email = 'pvtperosn1@pk.avaco.io'
business_person_email = 'autobusiness2@pk.avaco.io'
company_account_email = 'automatedcomp2@pk.avaco.io'
contact_account_email = ''
follower_account_email = ''
employee_account_email = ''
search_string_contact1 = "automated contact1"
search_string_private_person = "private1"
search_string_business_person = "business123"
search_string_company = "automated comp1"
groupcreator = "groupcreator@pk.avaco.io"
contact_messenger_emails = {
	"sender": "compavaco1@mail7.io",
	"receiver": "personavaco1@mail7.io"
}
webconf_creator = "webconfcreator@pk.avaco.io"


def random_company_name():
	temp = get_random_name(combo=[COLORS, STAR_WARS, ANIMALS]).split()[:2]
	return temp[0] + '-' + temp[1]


def random_name():
	return get_random_name(combo=[COLORS, STAR_WARS, ANIMALS]).split()[:1]


valid_emails = [
	"firstname.lastname@domain.com", "abc-d@mail.com", "abc.def@mail.com", "abc@mail.com",
	"abc_def@mail.com", "abc.def@mail.cc", "abc.def@mail-archive.com", "abc.def@mail.org", 'abc.def@mail.com'
]
invalid_emails = [
	"test", "#@%^%#$@#$@#.com", "@example.com", "Joe Smith <email@example.com>", "email@example@example.com",
	".email@example.com", "email.@example.com",
	"email..email@example.com", "email@example.com (Joe Smith)", "email@example", "email@-example.com",
	"email@111.222.333.44444", "email@example..com",
	"Abc..123@example.com", "”(),:;<>[\\]@example.com", "just”not”right@example.com",
	"this\\ is\"really\"not\\allowed@example.com", "test @test.com", "john.doe@.net"
]

profile_information = {
	"company_name": random_company_name(),
	"first_name": random_name(),
	"last_name": random_name(),
	"street": random_name(),

}


def name():
	return get_random_name().split()[0]


def last_name():  # hhmmss
	return get_random_name().split()[1]


def unique_string():
	return time_stamp_formatted()


# def hh_mm_ss():
# 	return last_name()


def ddmmyyhhmmss():
	now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
	return str(now)


def time_stamp():  # dd/mm/yyyy hh:mm:ss:cs (centiseconds)
	now = datetime.now().strftime("%d/%m/%Y %H:%M:%S:%f")[:-4]
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


###################xxxxxXXXX######File location infos
heavy_file_location = "Helper_Modules/Test_Files/Heavy_Files/big_excel.xls"
heavy_image_location = "Helper_Modules/Test_Files/Heavy_Files/big_jpg.jpg"
