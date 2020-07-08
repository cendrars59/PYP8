import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


class TestHomePage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(
            executable_path='/mnt/c/webdrivers/chromedriver.exe'
        )

    def tearDown(self):
        self.browser.close()

    def test_verify_logo(self):
        self.browser.get(self.live_server_url)
        time.sleep(5)
        # user opens the page and sees header section
        logo = self.browser.find_element_by_id("logo")
        source = logo.get_attribute("src")
        self.assertEquals(
            source,
            self.live_server_url
            + '/static/dist/assets/img/logo/logo_pur_beurre.png',
        )

    def test_verify_brand_value(self):
        self.browser.get(self.live_server_url)
        time.sleep(5)
        # user opens the page and sees header section
        title = self.browser.find_element_by_id("brand").text
        self.assertEquals(title, 'Pur beurre')

    def test_verify_h1_header_value(self):
        self.browser.get(self.live_server_url)
        time.sleep(5)
        # user opens the page and sees header section
        title = self.browser.find_element_by_id("main-title").text
        self.assertEquals(title, 'DU GRAS, OUI, MAIS DE QUALITÉ!')

    def test_redirection_to_login(self):
        mentions_url = self.live_server_url + reverse("login")
        self.browser.get(self.live_server_url)
        time.sleep(5)
        self.browser.find_element_by_id("selections-login").click()
        self.assertEquals(self.browser.current_url, mentions_url)

    def test_redirection_to_mentions(self):
        mentions_url = self.live_server_url + reverse("pages-mentions")
        self.browser.get(self.live_server_url)
        time.sleep(5)
        self.browser.find_element_by_id("legal-link").click()
        self.assertEquals(self.browser.current_url, mentions_url)
