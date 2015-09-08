import time

from selenium import webdriver
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User


class TestFunctionalOverride(LiveServerTestCase):

    username = 'tuser'
    password = 'tpass'
    email = 'tuser@123.org'

    def setUp(self):
        User.objects.create_superuser(self.username, self.email, self.password)
        self.browser = webdriver.Firefox()
        self.browser.set_window_size(1400, 1000)
        self.browser.get(self.live_server_url + '/admin/')

    def tearDown(self):
        self.browser.quit()

    def login(self):
        username = self.browser.find_element_by_name('username')
        username.send_keys(self.username)
        userpwd = self.browser.find_element_by_name('password')
        userpwd.send_keys(self.password)
        userpwd.send_keys(Keys.RETURN)

    def test_override_button(self):
        self.login()
        time.sleep(1)
        self.browser.get(self.live_server_url + '/admin/edc_quota/testquotamodel/add/')
        time.sleep(1)
        self.browser.find_element_by_id('override_quota').click()
        time.sleep(1)
        element = self.browser.find_element_by_id('id_override_code')
        self.assertEqual(element.get_attribute('value'), '')
