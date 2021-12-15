import requests 
import unittest

class MyTest(unittest.TestCase):

	def test_get_onliner(self):
		onliner_test_list = {"https://ab.onliner.by", "https://r.onliner.by","https://catalog.onliner.by"}
		for i in onliner_test_list:
			check_site_status(i, 200)

	def test_get_vk(self):
		check_site_status("https://www.vk.com", 200)

	def test_get_mail(self):
		check_site_status("https://www.mail.ru", 200)

def check_site_status(url, status_code):
	r = requests.get(url)
	assert r.status_code == status_code


if __name__=='__main__':
	unittest.main()


	# def create 
	# def get
	# def update
	# def get
	# def delete
	# def delete
	